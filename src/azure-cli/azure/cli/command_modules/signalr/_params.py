# pylint: disable=line-too-long
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.log import get_logger
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azure.cli.core.commands.parameters import (
    resource_group_name_type,
    get_location_type,
    get_resource_name_completion_list,
    tags_type,
    get_enum_type,
    get_three_state_flag
)
from ._actions import (
    UpstreamTemplateAddAction
)
from ._constants import (
    SIGNALR_RESOURCE_TYPE,
    SIGNALR_KEY_TYPE,
    SIGNALR_SERVICE_MODE_TYPE
)

from azure.cli.core import AzCommandsLoader

logger = get_logger(__name__)


def load_arguments(self: AzCommandsLoader, _):
    with self.argument_context('signalr') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('location',
                   arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('signalr_name', options_list=['--name', '-n'],
                   completer=get_resource_name_completion_list(SIGNALR_RESOURCE_TYPE),
                   help='Name of signalr service.')
        c.argument('tags', arg_type=tags_type)

    with self.argument_context('signalr create') as c:
        c.argument('sku', help='The sku name of the signalr service. E.g. Standard_S1')
        c.argument('unit_count', help='The number of signalr service unit count', type=int)
        c.argument('service_mode', help='The service mode which signalr service will be working on', choices=SIGNALR_SERVICE_MODE_TYPE)
        c.argument('allowed_origins', options_list=['--allowed-origins', '-a'], nargs='*', help='space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"')

    with self.argument_context('signalr update') as c:
        c.argument('sku', help='The sku name of the signalr service. E.g. Standard_S1')
        c.argument('unit_count', help='The number of signalr service unit count', type=int)
        c.argument('service_mode', help='The service mode which signalr service will be working on', choices=SIGNALR_SERVICE_MODE_TYPE)
        c.argument('allowed_origins', options_list=['--allowed-origins', '-a'], nargs='*', help='space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"')

    for scope in ['signalr create', 'signalr update']:
        with self.argument_context(scope, arg_group='Network Rule') as c:
            c.argument('default_action', arg_type=get_enum_type(['Allow', 'Deny']), help='Default action to apply when no rule matches.')

    with self.argument_context('signalr key renew') as c:
        c.argument('key_type', help='The name of access key to regenerate', choices=SIGNALR_KEY_TYPE)

    with self.argument_context('signalr cors add') as c:
        c.argument('allowed_origins', options_list=['--allowed-origins', '-a'], nargs='*', help='space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"')

    with self.argument_context('signalr cors remove') as c:
        c.argument('allowed_origins', options_list=['--allowed-origins', '-a'], nargs='*', help='space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"')

    # Network Rule
    for scope in ['signalr network-rule add', 'signalr network-rule update']:
        with self.argument_context(scope) as c:
            c.argument('connection_name', help='Name of private endpoint connection. `--connection-name` and `--public-network` are mutually exclusive.')
            c.argument('public_network', arg_type=get_three_state_flag(), help='The rules for public network. `--connection-name` and `--public-network` are mutually exclusive.')
            c.argument('allow', nargs='*', help='The allowed virtual network rule.')
            c.argument('deny', nargs='*', help='The denied virtual network rule.')

    with self.argument_context('signalr network-rule remove') as c:
        c.argument('connection_name', help='Name of private endpoint connection.')

    # Private Endpoint
    for item in ['approve', 'reject', 'show', 'delete']:
        with self.argument_context('signalr private-endpoint-connection {}'.format(item)) as c:
            c.argument('private_endpoint_connection_name', options_list=['--name', '-n'], required=False,
                       help='The name of the private endpoint connection associated with the SignalR Service.')
            c.extra('connection_id', options_list=['--id'], help='The ID of the private endpoint connection associated with the SignalR Service.')
            c.argument('resource_group_name', arg_type=resource_group_name_type, required=False)
            c.argument('signalr_name', options_list=['--name', '-n'],
                   completer=get_resource_name_completion_list(SIGNALR_RESOURCE_TYPE),
                   help='Name of signalr service.', required=False)
            c.argument('description', help='Comments for {} operation.'.format(item))

    # Upstream Settings
    with self.argument_context('signalr upstream update') as c:
        c.argument('template', action=UpstreamTemplateAddAction, nargs='+', help='Template item for upstream settings. Use key=value pattern to set properties. Supported keys are "url-template", "hub-pattern", "event-pattern", "category-pattern".')