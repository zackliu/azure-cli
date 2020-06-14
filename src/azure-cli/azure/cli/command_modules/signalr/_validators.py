# pylint: disable=line-too-long
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

def _query_account_rg(cli_ctx, account_name):
    """Query the storage account's resource group, which the mgmt sdk requires."""
    scf = storage_client_factory(cli_ctx)
    acc = next((x for x in scf.storage_accounts.list() if x.name == account_name), None)
    if acc:
        from msrestazure.tools import parse_resource_id
        return parse_resource_id(acc.id)['resource_group'], scf
    raise ValueError("Storage account '{}' not found.".format(account_name))

def validate_private_endpoint_connection_id(cmd, namespace):
    if namespace.connection_id:
        from azure.cli.core.util import parse_proxy_resource_id
        result = parse_proxy_resource_id(namespace.connection_id)
        namespace.resource_group_name = result['resource_group']
        namespace.account_name = result['name']
        namespace.private_endpoint_connection_name = result['child_name_1']

    if namespace.account_name and not namespace.resource_group_name:
        namespace.resource_group_name = _query_account_rg(cmd.cli_ctx, namespace.account_name)[0]

    if not all([namespace.account_name, namespace.resource_group_name, namespace.private_endpoint_connection_name]):
        raise CLIError('incorrect usage: [--id ID | --name NAME --account-name NAME]')

    del namespace.connection_id