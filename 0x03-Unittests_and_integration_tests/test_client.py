#!/usr/bin/env python3
"""
tests the client module
"""
import unittest
from unittest.mock import patch, PropertyMock
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
    def test_org(self, org, magicMock):
        """
        tests if org is working well
        """
        org_client = GithubOrgClient(org)
        result = org_client.org
        self.assertEqual(result, {'org': 'dummy'})
        magicMock.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """
        test for the property_public_repos_url
        """
        with patch(
                   "client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock
                   ) as mock_property:
            # set desired return value
            mock_property.return_value = 10

            my_instance = GithubOrgClient("google")
            result = my_instance._public_repos_url

        self.assertEqual(result, 10)
