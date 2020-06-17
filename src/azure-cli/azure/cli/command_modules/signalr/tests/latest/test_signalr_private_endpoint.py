# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
import unittest
from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer


class AzureSignalRServicePrivateEndpointScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(random_name_length=20)
    def test_signalr_private_endpoint(self, resource_group):
        signalr_name = self.create_random_name('signalr', 16)
        sku = 'Standard_S1'
        unit_count = 1
        location = 'eastus'

        self.kwargs.update({
            'location': location,
            'signalr_name': signalr_name,
            'sku': sku,
            'unit_count': unit_count,
            'vnet': 'vnet1',
            'subnet': 'subnet1',
            'private_endpoint': 'private_endpoint1',
            'private_endpoint_connection': 'private_endpoint_connection1'
        })

        signalr = self.cmd('az signalr create -n {signalr_name} -g {rg} --sku {sku}  -l {location}', checks=[
                     self.check('name', '{signalr_name}'),
                     self.check('location', '{location}'),
                     self.check('provisioningState', 'Succeeded'),
                     self.check('sku.name', '{sku}')
                 ])

        # Prepare network
        self.cmd('network vnet create -g {rg} -n {vnet} -l {location} --subnet-name {subnet}')
        self.cmd('network vnet subnet update --name {subnet} --resource-group {rg} --vnet-name {vent} --disable-private-endpoint-network-policies true')
        
        self.kwargs.update({
            'signalr_id': signalr['id']
        })

        # Create a private endpoint connection
        p_e = self.cmd('network private-endpoint create --resource-group {rg} --vnet-name {vent} --subnet {subnet} --name {private_endpoint}  --private-connection-resource-id {signalr_id} --group-ids signalr --connection-name {private_endpoint_connection} --location {location} --manual-request')

        # Test private link resource list
        p_e_c = self.cmd('signalr private-link-resource list -n {signalr_name} -g {rg}', checks=[
            self.check('length(@)', 1)
        ])

        self.kwargs.update({
            'private_endpoint_connection_id': p_e_c[0]['id']
        })

        # Test update network rules
        self.cmd('signalr network-rule update --public-network -n {signalr_name} -g {rg} --allow RESTAPI', checks=[
            self.check('')
        ])


