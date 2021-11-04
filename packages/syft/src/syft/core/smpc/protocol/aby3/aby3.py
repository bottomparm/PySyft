"""ABY3 Protocol.

ABY3 : A Mixed Protocol Framework for Machine Learning.
https://eprint.iacr.org/2018/403.pdf
"""
# stdlib
from functools import reduce
import secrets
import time
from typing import Any
from typing import List
from typing import Union
from uuid import UUID

# third party
import numpy as np

# relative
from .....ast.klass import get_run_class_method
from ....common import UID
from ....tensor.smpc.mpc_tensor import MPCTensor
from ....tensor.smpc.share_tensor import ShareTensor
from ....tensor.smpc.utils import get_nr_bits
from ...store.crypto_primitive_provider import CryptoPrimitiveProvider


class ABY3:
    """ABY3 Protocol Implementation."""

    def __eq__(self, other: Any) -> bool:
        """Check if "self" is equal with another object given a set of attributes to compare.

        Args:
            other (Any): Object to compare

        Returns:
            bool: True if equal False if not.
        """
        if type(self) != type(other):
            return False

        return True

    @staticmethod
    def bit_injection(x: MPCTensor, ring_size: int) -> MPCTensor:
        """Perform ABY3 bit injection for conversion of binary share to arithmetic share.

        Args:
            x (MPCTensor) : MPCTensor with shares of bit.
            ring_size (int) : Ring size of arithmetic share to convert.

        Returns:
            arith_share (MPCTensor): Arithmetic shares of bit in input ring size.

        Raises:
            ValueError: If input tensor is not binary shared.
            ValueError: If the exactly three parties are not involved in the computation.
        """
        # relative
        # relative
        from ....tensor import TensorPointer

        shape = x.shape
        parties = x.parties
        seed_id_locations = secrets.randbits(64)
        kwargs = {"seed_id_locations": seed_id_locations}
        path_and_name = x.child[0].path_and_name
        attr_path_and_name = f"{x.child[0].path_and_name}.bit_decomposition"

        if not isinstance(x.child[0], TensorPointer):
            decomposed_shares = [
                share.bit_decomposition(share, ring_size, False, **kwargs)
                for share in x.child
            ]
        else:
            decomposed_shares = []
            op = get_run_class_method(attr_path_and_name, SMPC=True)
            for share in x.child:
                decomposed_shares.append(op(share, share, ring_size, False, **kwargs))

        decomposed_shares = ABY3.pregenerate_pointers(
            parties, 1, path_and_name, seed_id_locations
        )

        # List which contains the share of a single bit
        res_shares: List[MPCTensor] = []

        bit_shares = [share[0] for share in decomposed_shares]
        bit_shares = zip(*bit_shares)  # type: ignore
        for bit_sh in bit_shares:
            mpc = MPCTensor(
                shares=bit_sh, shape=shape, parties=parties, ring_size=ring_size
            )
            res_shares.append(mpc)

        # TODO: Should modify to xor at mpc tensor level
        arith_share = reduce(lambda a, b: a + b - (2 * a * b), res_shares)

        return arith_share

    @staticmethod
    def full_adder(a: List[MPCTensor], b: List[MPCTensor]) -> List[MPCTensor]:
        """Perform bit addition on MPCTensors using a full adder.

        Args:
            a (List[MPCTensor]): MPCTensor with shares of bit.
            b (List[MPCTensor]): MPCTensor with shares of bit.

        Returns:
            result (List[MPCTensor]): Result of the operation.

        TODO: Should modify ripple carry adder to parallel prefix adder.
        """
        parties = a[0].parties
        parties_info = a[0].parties_info

        shape_x = tuple(a[0].shape)  # type: ignore
        shape_y = tuple(b[0].shape)  # type: ignore
        ring_size = 2 ** 32

        # For ring_size 2 we generate those before hand
        CryptoPrimitiveProvider.generate_primitives(
            "beaver_mul",
            nr_instances=64,
            parties=parties,
            g_kwargs={
                "a_shape": shape_x,
                "b_shape": shape_y,
                "parties_info": parties_info,
            },
            p_kwargs={"a_shape": shape_x, "b_shape": shape_y},
            ring_size=2,
        )

        ring_bits = get_nr_bits(ring_size)
        c = np.array([0], dtype=np.bool)  # carry bits of addition.
        result: List[MPCTensor] = []
        for idx in range(ring_bits):
            print("Bit Number :", idx)
            s_tmp = a[idx] + b[idx]
            s = s_tmp + c
            c = a[idx] * b[idx] + c * s_tmp
            result.append(s)
            time.sleep(3)
        return result

    @staticmethod
    def full_adder_spdz_compiler(
        a: List[MPCTensor], b: List[MPCTensor], c: [MPCTensor]
    ) -> List[MPCTensor]:
        # Specialized for 3 parties
        """Perform bit addition on MPCTensors using a full adder.

        Args:
            a (List[MPCTensor]): MPCTensor with shares of bit.
            b (List[MPCTensor]): MPCTensor with shares of bit.
            c (List[MPCTensor]): MPCTensor with shares of bit.

        Returns:
            result (List[MPCTensor]): Result of the operation.

        TODO: Should modify ripple carry adder to parallel prefix adder.
        """
        parties = a[0].parties
        parties_info = a[0].parties_info

        shape_x = tuple(a[0].shape)  # type: ignore
        shape_y = tuple(b[0].shape)  # type: ignore
        ring_size = 2 ** 32

        # For ring_size 2 we generate those before hand
        CryptoPrimitiveProvider.generate_primitives(
            "beaver_mul",
            nr_instances=128,
            parties=parties,
            g_kwargs={
                "a_shape": shape_x,
                "b_shape": shape_y,
                "parties_info": parties_info,
            },
            p_kwargs={"a_shape": shape_x, "b_shape": shape_y},
            ring_size=2,
        )

        ring_bits = get_nr_bits(ring_size)

        carry = np.zeros(a[0].mpc_shape, dtype=np.bool)  # carry bits of addition.
        beta_1 = np.zeros(a[0].mpc_shape, dtype=np.bool)
        gamma_1 = np.zeros(a[0].mpc_shape, dtype=np.bool)
        one = np.ones(a[0].mpc_shape, dtype=np.bool)

        result: List[MPCTensor] = []

        def majority(
            a: Union[MPCTensor, np.ndarray],
            b: Union[MPCTensor, np.ndarray],
            c: Union[MPCTensor, np.ndarray],
        ) -> MPCTensor:
            return (a + c + one) * (b + c) + b

        for idx in range(ring_bits):
            alfa = a[idx] + b[idx] + c[idx]
            beta = majority(a[idx], b[idx], c[idx])

            gamma = majority(alfa, beta_1, gamma_1)

            s = alfa + gamma_1 + beta_1

            beta_1 = beta
            gamma_1 = gamma
            import time
            time.sleep(1)
            result.append(s)
        return result

    @staticmethod
    def bit_decomposition(x: MPCTensor) -> List[MPCTensor]:
        """Perform ABY3 bit decomposition for conversion of arithmetic share to binary share.

        Args:
            x (MPCTensor): Arithmetic shares of secret.

        Returns:
            bin_share (List[MPCTensor]): Returns binary shares of each bit of the secret.

        TODO : Should be modified to use parallel prefix adder when multiprocessing
        functionality is integrated
        """
        # relative
        from ....tensor import TensorPointer

        nr_parties = len(x.parties)
        ring_size = 2 ** 32  # Should extract this info better
        ring_bits = get_nr_bits(ring_size)
        shape = x.shape
        parties = x.parties

        seed_id_locations = secrets.randbits(64)
        kwargs = {"seed_id_locations": seed_id_locations}
        path_and_name = x.child[0].path_and_name
        attr_path_and_name = f"{x.child[0].path_and_name}.bit_decomposition"

        if not isinstance(x.child[0], TensorPointer):
            decomposed_shares = [
                share.bit_decomposition(share, 2, True, **kwargs) for share in x.child
            ]
        else:
            decomposed_shares = []
            op = get_run_class_method(attr_path_and_name, SMPC=True)
            for share in x.child:
                decomposed_shares.append(op(share, share, 2, True, **kwargs))

        decomposed_shares = ABY3.pregenerate_pointers(
            parties, ring_bits, path_and_name, seed_id_locations
        )

        # List which contains the share of each share.
        # TODO: Shouldn't this be an empty list? and we append to it?
        res_shares: List[List[MPCTensor]] = [[] for _ in range(nr_parties)]

        for idx in range(ring_bits):
            bit_shares = [share[idx] for share in decomposed_shares]
            bit_shares = zip(*bit_shares)  # type: ignore
            for i, bit_sh in enumerate(bit_shares):
                mpc = MPCTensor(
                    shares=bit_sh, shape=shape, parties=parties, ring_size=2
                )
                res_shares[i].append(mpc)

        #bin_share = reduce(ABY3.full_adder, res_shares)
        bin_share = ABY3.full_adder_spdz_compiler(
            res_shares[0], res_shares[1], res_shares[2]
        )

        return bin_share

    @staticmethod
    def pregenerate_pointers(
        parties: List[Any], ring_bits: int, path_and_name: str, seed_id_locations: int
    ) -> List[List[List[ShareTensor]]]:
        generator = np.random.default_rng(seed_id_locations)
        # Skip the first ID ,as it is used for None return type in run class method.
        _ = UID(UUID(bytes=generator.bytes(16)))

        nr_parties = len(parties)
        resolved_pointer_type = [
            party.lib_ast.query(path_and_name) for party in parties
        ]

        """
        Consider bit decomposition.
        We create a share of share such that.
        Assume we are operating in ring_size 2**32(32 bits)
        Since we operate in n-out-of-n secret sharing, each party has a single share.
        Consider two parties such that a secret x is split as
        x = x1+x2
        To create share of shares,we use the intuition that the shares not held by party are made zero

                    Party1        Party2

        x1           x1             0

        x2           0               x2

        x_i_j denotes the shares held by jth party of ith share

        x_1_1 = x1
        x_1_2 = 0
        x_2_1 = 0
        x_2_2 = x2

        Party 1 = [x_1_1,x_2_1]
        Party 2  =[x_1_2,x_2_2]

        Now each party party has share of shares
        In bit decomposition, we split each bit and create share of shares

        Party 1 = [ [share of shares of first bit] ,[...second bit] ...[ nth bit]]

        Note: Count (share of shares for a particular bit) = number of parties
        """
        share_pointers: List[List[List[Any]]] = [[] for _ in range(nr_parties)]

        for _ in range(ring_bits * nr_parties):
            id_at_location = UID(UUID(bytes=generator.bytes(16)))
            for idx, party in enumerate(parties):
                result = resolved_pointer_type[idx].pointer_type(client=party)
                result.id_at_location = id_at_location
                share_pointers[idx].append(result)

        share_pointers = [
            [
                share_lst[i : i + nr_parties]  # noqa
                for i in range(0, len(share_lst), nr_parties)
            ]
            for share_lst in share_pointers
        ]

        return share_pointers
