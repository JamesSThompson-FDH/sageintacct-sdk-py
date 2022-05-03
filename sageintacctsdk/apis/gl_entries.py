"""
Sage Intacct GL Entries
"""
from typing import Dict

from .api_base import ApiBase


class GLEntries(ApiBase):
    """Class for GL Entries APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='GLENTRY')
