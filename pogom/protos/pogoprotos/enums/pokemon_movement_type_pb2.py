# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/pokemon_movement_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/pokemon_movement_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/enums/pokemon_movement_type.proto\x12\x10pogoprotos.enums*\xad\x01\n\x13PokemonMovementType\x12\x13\n\x0fMOVEMENT_STATIC\x10\x00\x12\x11\n\rMOVEMENT_JUMP\x10\x01\x12\x15\n\x11MOVEMENT_VERTICAL\x10\x02\x12\x14\n\x10MOVEMENT_PSYCHIC\x10\x03\x12\x15\n\x11MOVEMENT_ELECTRIC\x10\x04\x12\x13\n\x0fMOVEMENT_FLYING\x10\x05\x12\x15\n\x11MOVEMENT_HOVERING\x10\x06\x62\x06proto3')
)

_POKEMONMOVEMENTTYPE = _descriptor.EnumDescriptor(
  name='PokemonMovementType',
  full_name='pogoprotos.enums.PokemonMovementType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_STATIC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_JUMP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_VERTICAL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_PSYCHIC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_ELECTRIC', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_FLYING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVEMENT_HOVERING', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=67,
  serialized_end=240,
)
_sym_db.RegisterEnumDescriptor(_POKEMONMOVEMENTTYPE)

PokemonMovementType = enum_type_wrapper.EnumTypeWrapper(_POKEMONMOVEMENTTYPE)
MOVEMENT_STATIC = 0
MOVEMENT_JUMP = 1
MOVEMENT_VERTICAL = 2
MOVEMENT_PSYCHIC = 3
MOVEMENT_ELECTRIC = 4
MOVEMENT_FLYING = 5
MOVEMENT_HOVERING = 6


DESCRIPTOR.enum_types_by_name['PokemonMovementType'] = _POKEMONMOVEMENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
