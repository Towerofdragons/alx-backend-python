#!/usr/bin/env python3
"""
 unit test for utils.access_nested_map.
 Checks if utils.access_nested_map returns correctly.
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Any, Dict, List


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_correct_output(self, map: Dict[Any, Any],
                            path: List[str],
                            expected_result: Any) -> None:
        self.assertEqual(access_nested_map(map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
