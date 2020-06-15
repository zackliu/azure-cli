# pylint: disable=line-too-long
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
from azure.mgmt.signalr.models import UpstreamTemplate
from knack.util import CLIError

class UpstreamTemplateAddAction(argparse._AppendAction):
    def __call__(self, parser, namespace , values, option_string=None):
        kwargs = {}
        for item in values.split():
            try:
                key, value = item.split('=', 1)
                kwargs[key] = value
            except ValueError:
                raise CLIError('usage error: {} KEY=VALUE [KEY=VALUE ...]'.format(option_string))
        return UpstreamTemplate(**kwargs)
