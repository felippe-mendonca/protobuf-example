# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\"/\n\x03\x46oo\x12\x15\n\rinteger_field\x18\x01 \x01(\x05\x12\x11\n\tstr_field\x18\x02 \x01(\t\"%\n\x03\x42\x61r\x12\x11\n\x03\x66oo\x18\x01 \x01(\x0b\x32\x04.Foo\x12\x0b\n\x03\x62\x61z\x18\x02 \x01(\tb\x06proto3')
)




_FOO = _descriptor.Descriptor(
  name='Foo',
  full_name='Foo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integer_field', full_name='Foo.integer_field', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_field', full_name='Foo.str_field', index=1,
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
  serialized_start=17,
  serialized_end=64,
)


_BAR = _descriptor.Descriptor(
  name='Bar',
  full_name='Bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foo', full_name='Bar.foo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baz', full_name='Bar.baz', index=1,
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
  serialized_start=66,
  serialized_end=103,
)

_BAR.fields_by_name['foo'].message_type = _FOO
DESCRIPTOR.message_types_by_name['Foo'] = _FOO
DESCRIPTOR.message_types_by_name['Bar'] = _BAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Foo = _reflection.GeneratedProtocolMessageType('Foo', (_message.Message,), dict(
  DESCRIPTOR = _FOO,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Foo)
  ))
_sym_db.RegisterMessage(Foo)

Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), dict(
  DESCRIPTOR = _BAR,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Bar)
  ))
_sym_db.RegisterMessage(Bar)


# @@protoc_insertion_point(module_scope)