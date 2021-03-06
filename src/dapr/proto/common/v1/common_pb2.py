# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dapr/proto/common/v1/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dapr/proto/common/v1/common.proto',
  package='dapr.proto.common.v1',
  syntax='proto3',
  serialized_options=_b('\n\nio.dapr.v1B\014CommonProtosZ(github.com/dapr/dapr/pkg/proto/common/v1\252\002\033Dapr.Client.Autogen.Grpc.v1'),
  serialized_pb=_b('\n!dapr/proto/common/v1/common.proto\x12\x14\x64\x61pr.proto.common.v1\x1a\x19google/protobuf/any.proto\"\xaf\x02\n\rHTTPExtension\x12\x36\n\x04verb\x18\x01 \x01(\x0e\x32(.dapr.proto.common.v1.HTTPExtension.Verb\x12I\n\x0bquerystring\x18\x02 \x03(\x0b\x32\x34.dapr.proto.common.v1.HTTPExtension.QuerystringEntry\x1a\x32\n\x10QuerystringEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"g\n\x04Verb\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04HEAD\x10\x02\x12\x08\n\x04POST\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\x0b\n\x07\x43ONNECT\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07\x12\t\n\x05TRACE\x10\x08\"\x96\x01\n\rInvokeRequest\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0c\x63ontent_type\x18\x03 \x01(\t\x12;\n\x0ehttp_extension\x18\x04 \x01(\x0b\x32#.dapr.proto.common.v1.HTTPExtension\"J\n\x0eInvokeResponse\x12\"\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0c\x63ontent_type\x18\x02 \x01(\tBb\n\nio.dapr.v1B\x0c\x43ommonProtosZ(github.com/dapr/dapr/pkg/proto/common/v1\xaa\x02\x1b\x44\x61pr.Client.Autogen.Grpc.v1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])



_HTTPEXTENSION_VERB = _descriptor.EnumDescriptor(
  name='Verb',
  full_name='dapr.proto.common.v1.HTTPExtension.Verb',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTIONS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACE', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=287,
  serialized_end=390,
)
_sym_db.RegisterEnumDescriptor(_HTTPEXTENSION_VERB)


_HTTPEXTENSION_QUERYSTRINGENTRY = _descriptor.Descriptor(
  name='QuerystringEntry',
  full_name='dapr.proto.common.v1.HTTPExtension.QuerystringEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dapr.proto.common.v1.HTTPExtension.QuerystringEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dapr.proto.common.v1.HTTPExtension.QuerystringEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=285,
)

_HTTPEXTENSION = _descriptor.Descriptor(
  name='HTTPExtension',
  full_name='dapr.proto.common.v1.HTTPExtension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verb', full_name='dapr.proto.common.v1.HTTPExtension.verb', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='querystring', full_name='dapr.proto.common.v1.HTTPExtension.querystring', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HTTPEXTENSION_QUERYSTRINGENTRY, ],
  enum_types=[
    _HTTPEXTENSION_VERB,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=390,
)


_INVOKEREQUEST = _descriptor.Descriptor(
  name='InvokeRequest',
  full_name='dapr.proto.common.v1.InvokeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='dapr.proto.common.v1.InvokeRequest.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dapr.proto.common.v1.InvokeRequest.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='dapr.proto.common.v1.InvokeRequest.content_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_extension', full_name='dapr.proto.common.v1.InvokeRequest.http_extension', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=543,
)


_INVOKERESPONSE = _descriptor.Descriptor(
  name='InvokeResponse',
  full_name='dapr.proto.common.v1.InvokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='dapr.proto.common.v1.InvokeResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='dapr.proto.common.v1.InvokeResponse.content_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=619,
)

_HTTPEXTENSION_QUERYSTRINGENTRY.containing_type = _HTTPEXTENSION
_HTTPEXTENSION.fields_by_name['verb'].enum_type = _HTTPEXTENSION_VERB
_HTTPEXTENSION.fields_by_name['querystring'].message_type = _HTTPEXTENSION_QUERYSTRINGENTRY
_HTTPEXTENSION_VERB.containing_type = _HTTPEXTENSION
_INVOKEREQUEST.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_INVOKEREQUEST.fields_by_name['http_extension'].message_type = _HTTPEXTENSION
_INVOKERESPONSE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['HTTPExtension'] = _HTTPEXTENSION
DESCRIPTOR.message_types_by_name['InvokeRequest'] = _INVOKEREQUEST
DESCRIPTOR.message_types_by_name['InvokeResponse'] = _INVOKERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HTTPExtension = _reflection.GeneratedProtocolMessageType('HTTPExtension', (_message.Message,), {

  'QuerystringEntry' : _reflection.GeneratedProtocolMessageType('QuerystringEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPEXTENSION_QUERYSTRINGENTRY,
    '__module__' : 'dapr.proto.common.v1.common_pb2'
    # @@protoc_insertion_point(class_scope:dapr.proto.common.v1.HTTPExtension.QuerystringEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPEXTENSION,
  '__module__' : 'dapr.proto.common.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.common.v1.HTTPExtension)
  })
_sym_db.RegisterMessage(HTTPExtension)
_sym_db.RegisterMessage(HTTPExtension.QuerystringEntry)

InvokeRequest = _reflection.GeneratedProtocolMessageType('InvokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEREQUEST,
  '__module__' : 'dapr.proto.common.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.common.v1.InvokeRequest)
  })
_sym_db.RegisterMessage(InvokeRequest)

InvokeResponse = _reflection.GeneratedProtocolMessageType('InvokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVOKERESPONSE,
  '__module__' : 'dapr.proto.common.v1.common_pb2'
  # @@protoc_insertion_point(class_scope:dapr.proto.common.v1.InvokeResponse)
  })
_sym_db.RegisterMessage(InvokeResponse)


DESCRIPTOR._options = None
_HTTPEXTENSION_QUERYSTRINGENTRY._options = None
# @@protoc_insertion_point(module_scope)
