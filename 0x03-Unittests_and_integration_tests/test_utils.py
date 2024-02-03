#!/usr/bin/env python3
"""
unittests for the utils module
"""
from parameterized import parameterized
from typing import (
        Mapping,
        Sequence,
        Any,
        Dict,
        Callable
        )
from unittest import TestCase
from unittest.mock import patch, Mock
import utils


class TestAccessNestedMap(TestCase):
    """
    tests the nested map function
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),                 # Test Case 1
            ({"a": {"b": 2}}, ("a",), {"b": 2}),   # Test Case 2
            ({"a": {"b": 2}}, ("a", "b"), 2)       # Test Case 3
            ])
    def test_access_nested_map(
                              self,
                              nested_map: Mapping,
                              path: Sequence,
                              result: Any
                              ) -> None:
        """tests the access_nested_map if its valid with
        correct path
        """
        expected_result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(
                                        self,
                                        nested_map: Mapping,
                                        path: Sequence
                                        ) -> None:
        """
        tests the exception raised by accss nested map
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
    tests the getjson function
    """
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        # Define test cases
        test_cases = [
            {
             "test_url": "http://example.com",
             "test_payload": {"payload": True}
             },
            {
             "test_url": "http://holberton.io",
             "test_payload": {"payload": False}
              }
        ]

        # Iterate through test cases
        for case in test_cases:
            with self.subTest(case=case):
                # Set up mock response
                mock_response = Mock()
                mock_response.json.return_value = case["test_payload"]
                mock_get.return_value = mock_response

                result = utils.get_json(case["test_url"])

                # Assert that requests.get was called exactly once
                mock_get.assert_called_once_with(case["test_url"])

                self.assertEqual(result, case["test_payload"])
                # Reset mock for the next iteration
                mock_get.reset_mock()
