# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\"@\n\x07Request\x12\x10\n\x08operand1\x18\x01 \x01(\x05\x12\x10\n\x08operand2\x18\x02 \x01(\x05\x12\x11\n\toperation\x18\x03 \x01(\t\"1\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t24\n\nCalculator\x12&\n\tCalculate\x12\x08.Request\x1a\t.Response\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=20
  _REQUEST._serialized_end=84
  _RESPONSE._serialized_start=86
  _RESPONSE._serialized_end=135
  _CALCULATOR._serialized_start=137
  _CALCULATOR._serialized_end=189
# @@protoc_insertion_point(module_scope)
