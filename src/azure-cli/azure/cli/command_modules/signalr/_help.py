# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


helps['signalr'] = """
    type: group
    short-summary: Manage Azure SignalR Service.
"""

helps['signalr key'] = """
    type: group
    short-summary: Manage keys for Azure SignalR Service.
"""

helps['signalr cors'] = """
    type: group
    short-summary: Manage CORS for Azure SignalR Service.
"""

helps['signalr list'] = """
    type: command
    short-summary: Lists all the SignalR Service under the current subscription.
    examples:
        - name: List SignalR Service and show the results in a table.
          text: >
            az signalr list -o table
        - name: List SignalR Service in a resource group and show the results in a table.
          text: >
            az signalr list -g MySignalR -o table
"""

helps['signalr create'] = """
    type: command
    short-summary: Creates a SignalR Service.
    examples:
        - name: Create a SignalR Service with the Standard SKU and serverless mode.
          text: >
            az signalr create -n MySignalR -g MyResourceGroup --sku Standard_S1 --unit-count 1 --service-mode Serverless
"""

helps['signalr delete'] = """
    type: command
    short-summary: Deletes a SignalR Service.
    examples:
        - name: Delete a SignalR Service.
          text: >
            az signalr delete -n MySignalR -g MyResourceGroup
"""

helps['signalr show'] = """
    type: command
    short-summary: Get the details of a SignalR Service.
    examples:
        - name: Get the sku for a SignalR Service.
          text: >
            az signalr show -n MySignalR -g MyResourceGroup --query sku
"""

helps['signalr update'] = """
    type: command
    short-summary: Update an existing SignalR Service.
    examples:
        - name: Update unit count to scale the service.
          text: >
            az signalr update -n MySignalR -g MyResourceGroup --sku Standard_S1 --unit-count 50
        - name: Update service mode.
          text: >
            az signalr update -n MySignalR -g MyResourceGroup --service-mode Serverless
"""

helps['signalr restart'] = """
    type: command
    short-summary: Restart an existing SignalR Service.
    examples:
        - name: Restart a SignalR Service instance.
          text: >
            az signalr restart -n MySignalR -g MyResourceGroup
"""

helps['signalr key list'] = """
    type: command
    short-summary: List the access keys for a SignalR Service.
    examples:
        - name: Get the primary key for a SignalR Service.
          text: >
            az signalr key list -n MySignalR -g MyResourceGroup --query primaryKey -o tsv
"""

helps['signalr key renew'] = """
    type: command
    short-summary: Regenerate the access key for a SignalR Service.
    examples:
        - name: Renew the secondary key for a SignalR Service.
          text: >
            az signalr key renew -n MySignalR -g MyResourceGroup --key-type secondary
"""

helps['signalr cors add'] = """
    type: command
    short-summary: Add allowed origions to a SignalR Service
    examples:
        - name: Add a list of allowed origions to a SignalR Service
          text: >
            az signalr cors add -n MySignalR -g MyResourceGroup --allowed-origins "http://example1.com" "https://example2.com"
"""

helps['signalr cors list'] = """
    type: command
    short-summary: List allowed origions of a SignalR Service
"""

helps['signalr cors remove'] = """
    type: command
    short-summary: Remove allowed origions from a SignalR Service
    examples:
        - name: Remove a list of allowed origions from a SignalR Service
          text: >
            az signalr cors remove -n MySignalR -g MyResourceGroup --allowed-origins "http://example1.com" "https://example2.com"
"""
