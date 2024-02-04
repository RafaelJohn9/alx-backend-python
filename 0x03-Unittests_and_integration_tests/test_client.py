#!/usr/bin/env python3
"""
tests the client module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    testing the GithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json', return_value={'org': 'dummy'})
    def test_org(self, org, magic_mock):
        """
        tests if org is working well
        """
        org_client = GithubOrgClient(org)
        result = org_client.org
        self.assertEqual(result, {'org': 'dummy'})
        magic_mock.assert_called_once_with(f"https://api.github.com/orgs/{org}")
