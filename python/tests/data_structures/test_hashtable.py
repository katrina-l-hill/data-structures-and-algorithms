from cmath import exp
import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_missing_key():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("APPLE")
    expected = None
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable.buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_keys():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = list(hashtable.keys())
    actual.sort()
    expected = ["ahmad", "listen", "silent"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_hash():
    hashtable = Hashtable(1024)
    hash1 = hashtable.hash("ahmad")
    hash2 = hashtable.hash("hamda")
    hash3 = hashtable.hash("damha")
    assert hash1 == hash2 and hash2 == hash3


# @pytest.mark.skip("TODO")
def test_collisions():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("hamda", 40)
    hashtable.set("damha", 50)
    keyset = list(hashtable.keys())
    keyset.sort()
    actual = []
    for key in keyset:
        actual.append((key, hashtable.get(key)))
    expected = [("ahmad", 30), ("damha", 50), ("hamda", 40)]
    assert actual == expected
