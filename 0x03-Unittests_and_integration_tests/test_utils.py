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
