from ..remote import RemoteModel


class DeviceViewerSwitchPortConfigSdnElementGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``BridgeDomain:`` none
    |  ``attribute type:`` string

    |  ``bridge_domain_dn:`` none
    |  ``attribute type:`` string

    |  ``AciTenant:`` none
    |  ``attribute type:`` string

    |  ``tenant_dn:`` none
    |  ``attribute type:`` string

    |  ``AciEpg:`` none
    |  ``attribute type:`` string

    |  ``epg_dn:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``StpPortState:`` none
    |  ``attribute type:`` string

    |  ``ifPortFast:`` none
    |  ``attribute type:`` string

    |  ``ifAdminStatus:`` none
    |  ``attribute type:`` string

    |  ``ifOperStatus:`` none
    |  ``attribute type:`` string

    |  ``adminoperred:`` none
    |  ``attribute type:`` string

    |  ``stpportstatered:`` none
    |  ``attribute type:`` string

    |  ``portfastred:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "ifName",
                  "ifNameSort",
                  "ifIndex",
                  "VlanIndex",
                  "VlanID",
                  "BridgeDomain",
                  "bridge_domain_dn",
                  "AciTenant",
                  "tenant_dn",
                  "AciEpg",
                  "epg_dn",
                  "RootBridgeAddress",
                  "RootVlanMemberID",
                  "StpPortState",
                  "ifPortFast",
                  "ifAdminStatus",
                  "ifOperStatus",
                  "adminoperred",
                  "stpportstatered",
                  "portfastred",
                  "ifPortControlInd",
                  )
