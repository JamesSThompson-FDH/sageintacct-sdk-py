"""
Sage Intacct charge card transaction entry
"""
from typing import Dict

from .api_base import ApiBase

class ChargeCardTransactionEntry(ApiBase):
    """Class for Charge Card Transaction Entry APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='CCTRANSACTIONENTRY')
