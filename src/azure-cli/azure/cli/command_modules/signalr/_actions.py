# pylint: disable=line-too-long
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse


class UpstreamTemplateAddAction(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            FooRule = namespace._cmd.get_models('FooRule')
            name, metric, operation, value = values.split()
            return FooRule(
                name=name,
                metric=metric,
                operation=operation,
                value=value
            )
        except ValueError:
            raise CLIError('usage error: {} NAME METRIC OPERATION VALUE'.format(option_string))