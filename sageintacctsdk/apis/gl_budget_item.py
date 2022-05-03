"""
Sage Intacct GL Budget Item
"""
from typing import Dict

from .api_base import ApiBase


class GLBudgetItem(ApiBase):
    """Class for Accounts APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLBUDGETITEM')
