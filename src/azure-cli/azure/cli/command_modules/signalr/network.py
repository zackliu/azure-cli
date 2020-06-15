# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.mgmt.signalr.operations.signal_roperations import SignalROperations 


def add_network_rule(client: SignalROperations, signalr_name, resource_group_name, action='Allow', subnet=None,
                     vnet_name=None, ip_address=None):
    pass