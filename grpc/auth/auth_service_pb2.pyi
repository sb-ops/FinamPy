"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AuthRequest(google.protobuf.message.Message):
    """Запрос авторизации"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECRET_FIELD_NUMBER: builtins.int
    secret: builtins.str
    """API токен (secret key)"""
    def __init__(
        self,
        *,
        secret: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["secret", b"secret"]) -> None: ...

global___AuthRequest = AuthRequest

@typing.final
class AuthResponse(google.protobuf.message.Message):
    """Информация об авторизации"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    token: builtins.str
    """Полученный JWT-токен"""
    def __init__(
        self,
        *,
        token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["token", b"token"]) -> None: ...

global___AuthResponse = AuthResponse

@typing.final
class TokenDetailsRequest(google.protobuf.message.Message):
    """Запрос информации о токене"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    token: builtins.str
    """JWT-токен"""
    def __init__(
        self,
        *,
        token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["token", b"token"]) -> None: ...

global___TokenDetailsRequest = TokenDetailsRequest

@typing.final
class TokenDetailsResponse(google.protobuf.message.Message):
    """Информация о токене"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATED_AT_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    MD_PERMISSIONS_FIELD_NUMBER: builtins.int
    ACCOUNT_IDS_FIELD_NUMBER: builtins.int
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время создания"""

    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Дата и время экспирации"""

    @property
    def md_permissions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MDPermission]:
        """Информация о доступе к рыночным данным"""

    @property
    def account_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Идентификаторы аккаунтов"""

    def __init__(
        self,
        *,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        md_permissions: collections.abc.Iterable[global___MDPermission] | None = ...,
        account_ids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "expires_at", b"expires_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["account_ids", b"account_ids", "created_at", b"created_at", "expires_at", b"expires_at", "md_permissions", b"md_permissions"]) -> None: ...

global___TokenDetailsResponse = TokenDetailsResponse

@typing.final
class MDPermission(google.protobuf.message.Message):
    """Информация о доступе к рыночным данным"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _QuoteLevel:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _QuoteLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[MDPermission._QuoteLevel.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        QUOTE_LEVEL_UNSPECIFIED: MDPermission._QuoteLevel.ValueType  # 0
        """Значение не указано"""
        QUOTE_LEVEL_LAST_PRICE: MDPermission._QuoteLevel.ValueType  # 1
        """Последняя цена"""
        QUOTE_LEVEL_BEST_BID_OFFER: MDPermission._QuoteLevel.ValueType  # 2
        """Бид аск"""
        QUOTE_LEVEL_DEPTH_OF_MARKET: MDPermission._QuoteLevel.ValueType  # 3
        """ Агрегированный стакан"""
        QUOTE_LEVEL_DEPTH_OF_BOOK: MDPermission._QuoteLevel.ValueType  # 4
        """Полный стакан"""
        QUOTE_LEVEL_ACCESS_FORBIDDEN: MDPermission._QuoteLevel.ValueType  # 5
        """Доступ запрещен"""

    class QuoteLevel(_QuoteLevel, metaclass=_QuoteLevelEnumTypeWrapper):
        """Уровень котировок"""

    QUOTE_LEVEL_UNSPECIFIED: MDPermission.QuoteLevel.ValueType  # 0
    """Значение не указано"""
    QUOTE_LEVEL_LAST_PRICE: MDPermission.QuoteLevel.ValueType  # 1
    """Последняя цена"""
    QUOTE_LEVEL_BEST_BID_OFFER: MDPermission.QuoteLevel.ValueType  # 2
    """Бид аск"""
    QUOTE_LEVEL_DEPTH_OF_MARKET: MDPermission.QuoteLevel.ValueType  # 3
    """ Агрегированный стакан"""
    QUOTE_LEVEL_DEPTH_OF_BOOK: MDPermission.QuoteLevel.ValueType  # 4
    """Полный стакан"""
    QUOTE_LEVEL_ACCESS_FORBIDDEN: MDPermission.QuoteLevel.ValueType  # 5
    """Доступ запрещен"""

    QUOTE_LEVEL_FIELD_NUMBER: builtins.int
    DELAY_MINUTES_FIELD_NUMBER: builtins.int
    MIC_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    CONTINENT_FIELD_NUMBER: builtins.int
    WORLDWIDE_FIELD_NUMBER: builtins.int
    quote_level: global___MDPermission.QuoteLevel.ValueType
    """Уровень котировок"""
    delay_minutes: builtins.int
    """Задержка в минутах"""
    mic: builtins.str
    """Идентификатор биржи mic"""
    country: builtins.str
    """Страна"""
    continent: builtins.str
    """Континент"""
    worldwide: builtins.bool
    """Весь мир"""
    def __init__(
        self,
        *,
        quote_level: global___MDPermission.QuoteLevel.ValueType = ...,
        delay_minutes: builtins.int = ...,
        mic: builtins.str = ...,
        country: builtins.str = ...,
        continent: builtins.str = ...,
        worldwide: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["condition", b"condition", "continent", b"continent", "country", b"country", "mic", b"mic", "worldwide", b"worldwide"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["condition", b"condition", "continent", b"continent", "country", b"country", "delay_minutes", b"delay_minutes", "mic", b"mic", "quote_level", b"quote_level", "worldwide", b"worldwide"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["condition", b"condition"]) -> typing.Literal["mic", "country", "continent", "worldwide"] | None: ...

global___MDPermission = MDPermission
