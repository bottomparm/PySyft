# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/common/action/beaver_action.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.tensor import (
    share_tensor_pb2 as proto_dot_core_dot_tensor_dot_share__tensor__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/node/common/action/beaver_action.proto",
    package="syft.core.node.common.action",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n1proto/core/node/common/action/beaver_action.proto\x12\x1csyft.core.node.common.action\x1a$proto/core/tensor/share_tensor.proto\x1a%proto/core/common/common_object.proto\"\xb8\x01\n\x0c\x42\x65\x61verAction\x12*\n\x03\x65ps\x18\x01 \x01(\x0b\x32\x1d.syft.core.tensor.ShareTensor\x12%\n\x06\x65ps_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12,\n\x05\x64\x65lta\x18\x03 \x01(\x0b\x32\x1d.syft.core.tensor.ShareTensor\x12'\n\x08\x64\x65lta_id\x18\x04 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3",
    dependencies=[
        proto_dot_core_dot_tensor_dot_share__tensor__pb2.DESCRIPTOR,
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_BEAVERACTION = _descriptor.Descriptor(
    name="BeaverAction",
    full_name="syft.core.node.common.action.BeaverAction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="eps",
            full_name="syft.core.node.common.action.BeaverAction.eps",
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
            name="eps_id",
            full_name="syft.core.node.common.action.BeaverAction.eps_id",
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
        _descriptor.FieldDescriptor(
            name="delta",
            full_name="syft.core.node.common.action.BeaverAction.delta",
            index=2,
            number=3,
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
            name="delta_id",
            full_name="syft.core.node.common.action.BeaverAction.delta_id",
            index=3,
            number=4,
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
    serialized_start=161,
    serialized_end=345,
)

_BEAVERACTION.fields_by_name[
    "eps"
].message_type = proto_dot_core_dot_tensor_dot_share__tensor__pb2._SHARETENSOR
_BEAVERACTION.fields_by_name[
    "eps_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_BEAVERACTION.fields_by_name[
    "delta"
].message_type = proto_dot_core_dot_tensor_dot_share__tensor__pb2._SHARETENSOR
_BEAVERACTION.fields_by_name[
    "delta_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["BeaverAction"] = _BEAVERACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BeaverAction = _reflection.GeneratedProtocolMessageType(
    "BeaverAction",
    (_message.Message,),
    {
        "DESCRIPTOR": _BEAVERACTION,
        "__module__": "proto.core.node.common.action.beaver_action_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.action.BeaverAction)
    },
)
_sym_db.RegisterMessage(BeaverAction)


# @@protoc_insertion_point(module_scope)
