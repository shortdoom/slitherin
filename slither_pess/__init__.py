from slither_pess.detectors.double_entry_token_possibility import DoubleEntryTokenPossiblity
from slither_pess.detectors.unprotected_setter import UnprotectedSetter
from slither_pess.detectors.nft_approve_warning import NftApproveWarning
from slither_pess.detectors.inconsistent_nonreentrant import InconsistentNonreentrant


def make_plugin():
    plugin_detectors = [DoubleEntryTokenPossiblity,UnprotectedSetter, NftApproveWarning, InconsistentNonreentrant]
    plugin_printers = []

    return plugin_detectors, plugin_printers
