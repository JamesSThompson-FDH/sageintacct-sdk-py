"""
Sage Intacct accounts
"""
from typing import Dict

from .api_base import ApiBase


class AuditHistory(ApiBase):
    """Class for Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='AUDITHISTORY')
