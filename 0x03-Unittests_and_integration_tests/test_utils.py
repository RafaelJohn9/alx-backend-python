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
from utils import memoize


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
    @parameterized.expand([
                           ("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})
                          ])
    def test_get_json(self, url: str, response_json: Dict):
        """
        tests validity of our api fetching function
        """
        mock_response = Mock()
        mock_response.json.return_value = response_json
        with patch(
                  "utils.requests.get",
                  return_value=mock_response
                  ) as mocked_get:
            output = utils.get_json(url)
        mocked_get.assert_called_once_with(url)
        self.assertEqual(output, response_json)


class TestMemoize(TestCase):
    """
    tests the memoization class
    """
    def test_memoize(self):
        """
        tests memoization decorator
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            instance = TestClass()
            result_1 = instance.a_property
            result_2 = instance.a_property

        mock_method.assert_called_once()
        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)
