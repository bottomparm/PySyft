/**
 * This file has been automatically generated by the [capnpc-ts utility](https://github.com/jdiaz5513/capnp-ts).
 */
import * as capnp from 'capnp-ts';
import { Struct as __S } from 'capnp-ts';
export declare const _capnpFileId: bigint;
export declare class DataBox extends __S {
  static readonly _capnp: {
    displayName: string;
    id: string;
    size: capnp.ObjectSize;
  };
  adoptValue(value: capnp.Orphan<capnp.Data>): void;
  disownValue(): capnp.Orphan<capnp.Data>;
  getValue(): capnp.Data;
  hasValue(): boolean;
  initValue(length: number): capnp.Data;
  setValue(value: capnp.Data): void;
  toString(): string;
}