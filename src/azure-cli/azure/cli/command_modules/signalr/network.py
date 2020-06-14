
from azure.mgmt.signalr.operations.signal_roperations import SignalROperations 


def add_network_rule(client: SignalROperations, signalr_name, resource_group_name, action='Allow', subnet=None,
                     vnet_name=None, ip_address=None):
    client.get