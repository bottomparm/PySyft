# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/sympc/share_tensor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


<<<<<<< HEAD
# syft absolute
from syft.proto.lib.sympc import session_pb2 as proto_dot_lib_dot_sympc_dot_session__pb2
=======
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
>>>>>>> e2cc8ccc9... 2nd cleanup
from syft.proto.lib.torch import tensor_pb2 as proto_dot_lib_dot_torch_dot_tensor__pb2
from syft.proto.lib.sympc import session_pb2 as proto_dot_lib_dot_sympc_dot_session__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/sympc/share_tensor.proto",
    package="syft.lib.sympc",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n"proto/lib/sympc/share_tensor.proto\x12\x0esyft.lib.sympc\x1a\x1cproto/lib/torch/tensor.proto\x1a\x1dproto/lib/sympc/session.proto"g\n\x0bShareTensor\x12+\n\x06tensor\x18\x01 \x01(\x0b\x32\x1b.syft.lib.torch.TensorProto\x12+\n\x07session\x18\x02 \x01(\x0b\x32\x1a.syft.lib.sympc.MPCSessionb\x06proto3',
    dependencies=[
        proto_dot_lib_dot_torch_dot_tensor__pb2.DESCRIPTOR,
        proto_dot_lib_dot_sympc_dot_session__pb2.DESCRIPTOR,
    ],
)


_SHARETENSOR = _descriptor.Descriptor(
    name="ShareTensor",
    full_name="syft.lib.sympc.ShareTensor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tensor",
            full_name="syft.lib.sympc.ShareTensor.tensor",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="session",
            full_name="syft.lib.sympc.ShareTensor.session",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=115,
    serialized_end=218,
)

_SHARETENSOR.fields_by_name[
    "tensor"
].message_type = proto_dot_lib_dot_torch_dot_tensor__pb2._TENSORPROTO
_SHARETENSOR.fields_by_name[
    "session"
].message_type = proto_dot_lib_dot_sympc_dot_session__pb2._MPCSESSION
DESCRIPTOR.message_types_by_name["ShareTensor"] = _SHARETENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShareTensor = _reflection.GeneratedProtocolMessageType(
    "ShareTensor",
    (_message.Message,),
    {
        "DESCRIPTOR": _SHARETENSOR,
        "__module__": "proto.lib.sympc.share_tensor_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.sympc.ShareTensor)
    },
)
_sym_db.RegisterMessage(ShareTensor)


# @@protoc_insertion_point(module_scope)
