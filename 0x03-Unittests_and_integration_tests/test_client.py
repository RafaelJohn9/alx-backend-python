#!/usr/bin/env python3
"""
tests the client module
"""
from fixtures import TEST_PAYLOAD
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
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

    @patch('client.get_json',
           return_value={"repos_url": "https://www.example.com"})
    def test_public_repos(self, mocked_method):
        """
        tests the public_repos method
        """
        instance = GithubOrgClient("dummy")
        result = instance.public_repos("1")
        self.assertEqual(result, [])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
        ])
    def test_has_license(self, repo_dict, license_key):
        """
        tests has_license static method
        """
        instance = GithubOrgClient("mock")
        expected = repo_dict["license"]["key"] == "my_license"
        self.assertEqual(instance.has_license(repo_dict, license_key),
                         expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    integration testing for GithubOrgClient
    """
    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get and provide fixtures."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: cls.org_payload),
            unittest.mock.Mock(json=lambda: cls.repos_payload),
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos_integration(self):
        """Integration test for GithubOrgClient.public_repos method."""
        test_instance = GithubOrgClient('test')
        result = test_instance.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)
