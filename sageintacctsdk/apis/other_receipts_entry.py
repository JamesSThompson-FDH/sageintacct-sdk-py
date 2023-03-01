"""
Sage Intacct other receipts entry 
"""
from typing import Dict

from .api_base import ApiBase


class OtherReceiptsEntry(ApiBase):
    """Class for Other Receipts Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='OTHERRECEIPTSENTRY')
