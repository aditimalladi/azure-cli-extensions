# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"


class DiskMode(str, Enum):

    persistent = "persistent"
    independent_persistent = "independent_persistent"
    independent_nonpersistent = "independent_nonpersistent"


class OsType(str, Enum):

    windows = "Windows"
    linux = "Linux"
    other = "Other"


class NICType(str, Enum):

    vmxnet3 = "vmxnet3"
    vmxnet2 = "vmxnet2"
    vmxnet = "vmxnet"
    e1000 = "e1000"
    e1000e = "e1000e"
    pcnet32 = "pcnet32"


class PowerOnBootOption(str, Enum):

    enabled = "enabled"
    disabled = "disabled"


class IPAddressAllocationMethod(str, Enum):

    unset = "unset"
    dynamic = "dynamic"
    static = "static"
    linklayer = "linklayer"
    random = "random"
    other = "other"


class SCSIControllerType(str, Enum):

    lsilogic = "lsilogic"
    buslogic = "buslogic"
    pvscsi = "pvscsi"
    lsilogicsas = "lsilogicsas"


class VirtualSCSISharing(str, Enum):

    no_sharing = "noSharing"
    physical_sharing = "physicalSharing"
    virtual_sharing = "virtualSharing"


class InventoryType(str, Enum):

    resource_pool = "ResourcePool"
    virtual_machine = "VirtualMachine"
    virtual_machine_template = "VirtualMachineTemplate"
    virtual_network = "VirtualNetwork"
