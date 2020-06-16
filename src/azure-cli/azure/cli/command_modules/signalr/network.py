# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.mgmt.signalr.models import (
    PrivateEndpointACL,
    SignalRResource
    )


def add_network_rule(client, signalr_name, resource_group_name, connection_name, allow, deny):
    resource = client.get(resource_group_name, signalr_name)
    network_acl = resource.network_ac_ls
    if not network_acl.private_endpoints:
        network_acl.private_endpoints = []
    network_acl.private_endpoints.append(PrivateEndpointACL(name=connection_name, allow=allow, deny=deny))
    return client.update(resource_group_name, signalr_name, SignalRResource(network_ac_ls=network_acl))


def update_network_rules(client, signalr_name, resource_group_name, connection_name, public_network, allow, deny):
    resource = client.get(resource_group_name, signalr_name)
    network_acl = resource.network_ac_ls
    if public_network:
        network_acl.public_network.allow = allow
        network_acl.public_network.deny = deny
    elif connection_name:
        if network_acl.private_endpoints:
            matched_private_endpoints = [x for x in matched_private_endpoints if x.name == connection_name]
            for x in matched_private_endpoints:
                x.allow = allow
                x.deny = deny

    return client.update(resource_group_name, signalr_name, SignalRResource(network_ac_ls=network_acl))

def remove_network_rule(client, signalr_name, resource_group_name, connection_name):
    resource = client.get(resource_group_name, signalr_name)
    network_acl = resource.network_ac_ls
    if network_acl.private_endpoints:
        network_acl.private_endpoints = [x for x in network_acl.private_endpoints if x.name != connection_name]
    return client.update(resource_group_name, signalr_name, SignalRResource(network_ac_ls=network_acl))


def list_network_rules(client, signalr_name, resource_group_name):
    resource = client.get(resource_group_name, signalr_name)
    return resource.network_ac_ls
