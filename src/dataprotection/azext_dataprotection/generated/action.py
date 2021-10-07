# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddStorageSettings(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddStorageSettings, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'datastore-type':
                d['datastore_type'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter storage_settings. All possible keys are: '
                               'datastore-type, type'.format(k))
        return d


class AddBackupPolicy(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.backup_policy = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'policy-rules':
                d['policy_rules'] = v
            elif kl == 'datasource-types':
                d['datasource_types'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter backup_policy. All possible keys are: '
                               'policy-rules, datasource-types'.format(k))
        d['object_type'] = 'BackupPolicy'
        return d


class AddDataSourceInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.data_source_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'datasource-type':
                d['datasource_type'] = v[0]
            elif kl == 'object-type':
                d['object_type'] = v[0]
            elif kl == 'resource-id':
                d['resource_id'] = v[0]
            elif kl == 'resource-location':
                d['resource_location'] = v[0]
            elif kl == 'resource-name':
                d['resource_name'] = v[0]
            elif kl == 'resource-type':
                d['resource_type'] = v[0]
            elif kl == 'resource-uri':
                d['resource_uri'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter data_source_info. All possible keys are: '
                               'datasource-type, object-type, resource-id, resource-location, resource-name, '
                               'resource-type, resource-uri'.format(k))
        return d


class AddDataSourceSetInfo(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.data_source_set_info = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'datasource-type':
                d['datasource_type'] = v[0]
            elif kl == 'object-type':
                d['object_type'] = v[0]
            elif kl == 'resource-id':
                d['resource_id'] = v[0]
            elif kl == 'resource-location':
                d['resource_location'] = v[0]
            elif kl == 'resource-name':
                d['resource_name'] = v[0]
            elif kl == 'resource-type':
                d['resource_type'] = v[0]
            elif kl == 'resource-uri':
                d['resource_uri'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter data_source_set_info. All possible keys '
                               'are: datasource-type, object-type, resource-id, resource-location, resource-name, '
                               'resource-type, resource-uri'.format(k))
        return d


class AddSecretStoreBasedAuthCredentials(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.secret_store_based_auth_credentials = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'uri':
                d['uri'] = v[0]
            elif kl == 'secret-store-type':
                d['secret_store_type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter secret_store_based_auth_credentials. All '
                               'possible keys are: uri, secret-store-type'.format(k))
        d['object_type'] = 'SecretStoreBasedAuthCredentials'
        return d


class AddPolicyParameters(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.policy_parameters = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'data-store-parameters-list':
                d['data_store_parameters_list'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter policy_parameters. All possible keys are: '
                               'data-store-parameters-list'.format(k))
        return d
