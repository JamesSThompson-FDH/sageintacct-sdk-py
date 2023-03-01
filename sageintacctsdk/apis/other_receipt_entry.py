"""
Sage Intacct other receipt entry 
"""
from typing import Dict

from .api_base import ApiBase


class OtherReceiptEntry(ApiBase):
    """Class for Other Receipt Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='OTHERRECEIPTENTRY')
