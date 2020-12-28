from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class GridMastersNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``Counts:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "Counts",
                  )
