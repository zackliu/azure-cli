# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.mgmt.signalr.models import (
    PrivateLinkServiceConnectionState
    )


def approve_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, description=None):
    return _update_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, True, description)


def reject_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, description=None):
    return _update_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, False, description)


def delete_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, description=None):
    return client.delete(private_endpoint_connection_name, resource_group_name, signalr_name)


def get_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, description=None):
    return client.get(private_endpoint_connection_name, resource_group_name, signalr_name)


def list_by_signalr(client, resource_group_name, signalr_name):
    return client.list(resource_group_name, signalr_name)


def _update_private_endpoint_connection(client, resource_group_name, signalr_name, private_endpoint_connection_name, is_approve_operation, description):
    private_endpoint_connection = client.get(private_endpoint_connection, resource_group_name, signalr_name)

    new_status = PrivateLinkServiceConnectionState(status='Approved', description=description) if is_approve_operation else PrivateLinkServiceConnectionState(status='Rejected', description=description)
    
    return client.update(private_endpoint_connection_name, resource_group_name, signalr_name,
                            private_endpoint=private_endpoint_connection.private_endpoint,
                            private_link_service_connection_state=new_status)

