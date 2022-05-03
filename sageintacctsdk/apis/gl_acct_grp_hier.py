"""
Sage Intacct accounts group heir
"""
from typing import Dict

from .api_base import ApiBase


class GLAcctGrpHier(ApiBase):
    """Class for Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLACCTGRPHIERARCHY')
