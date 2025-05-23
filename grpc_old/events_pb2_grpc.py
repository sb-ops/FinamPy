# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from FinamPy.proto_old import events_pb2 as FinamPy_dot_proto__old_dot_events__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in FinamPy/grpc_old/events_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EventsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEvents = channel.stream_stream(
                '/grpc.tradeapi.v1.Events/GetEvents',
                request_serializer=FinamPy_dot_proto__old_dot_events__pb2.SubscriptionRequest.SerializeToString,
                response_deserializer=FinamPy_dot_proto__old_dot_events__pb2.Event.FromString,
                _registered_method=True)


class EventsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEvents(self, request_iterator, context):
        """Event Service sends events after explicit subscription.
        Сервис событий. Отправляет события после вызова соответствующих методов подписки.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEvents': grpc.stream_stream_rpc_method_handler(
                    servicer.GetEvents,
                    request_deserializer=FinamPy_dot_proto__old_dot_events__pb2.SubscriptionRequest.FromString,
                    response_serializer=FinamPy_dot_proto__old_dot_events__pb2.Event.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.tradeapi.v1.Events', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('grpc.tradeapi.v1.Events', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Events(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEvents(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/grpc.tradeapi.v1.Events/GetEvents',
            FinamPy_dot_proto__old_dot_events__pb2.SubscriptionRequest.SerializeToString,
            FinamPy_dot_proto__old_dot_events__pb2.Event.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
