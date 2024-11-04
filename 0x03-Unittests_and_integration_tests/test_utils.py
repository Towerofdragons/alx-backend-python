#!/usr/bin/env python3
"""
 unit test for utils.access_nested_map.
 Checks if utils.access_nested_map returns correctly.
"""

import unittest
import utils
from parameterized import parameterized
from typing import Any, Dict, List


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, map: Dict[Any, Any],
                               path: List[str],
                               expected_result: Any) -> None:
        self.assertEqual(utils.access_nested_map(map, path), expected_result)

    @parameterized.expand([
        ({}, ["a"], KeyError, "'a'"),
        ({"a": 1}, ["a", "b"], KeyError, "'b'")
    ])
    def test_access_nested_map_exception(self, map: Dict[Any, Any],
                                         path: List[str],
                                         expected_result: Any,
                                         msg: str) -> None:
        with self.assertRaises(expected_result) as cm:
            utils.access_nested_map(map, path)

        error = str(cm.exception)
        self.assertEqual(error, msg)


if __name__ == "__main__":
    unittest.main()
