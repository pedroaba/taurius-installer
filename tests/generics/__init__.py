import unittest
from typing import Any, Mapping


class CommonTestCase(unittest.TestCase):
    def assertDictContainsSubset(
        self,
        dictionary: dict | Mapping[Any, Any],
        subset: dict | Mapping[Any, Any],
        msg: str = None,
    ):
        if "assertDictContainsSubset" in super(CommonTestCase, self).__dict__:
            return super(CommonTestCase, self).assertDictContainsSubset(
                subset, dictionary, msg
            )

        dictionary_set = set(dict(dictionary))
        subset_set = set(dict(subset))
        if subset_set.issubset(dictionary_set):
            return True

        raise AssertionError(
            "The dictionary does not contains subset: {} \n {} \n\n -> key difference: {} \n -> values: {}".format(
                dictionary,
                subset,
                dictionary_set - subset_set,
                {
                    k: dictionary[k]
                    for k in set(dictionary_set) - set(subset_set)
                },
            )
        )
