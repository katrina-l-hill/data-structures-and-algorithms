import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


def test_head_next_insert_stuff_in_list():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("banana")
    assert linked.head.next.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple") is True


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")

def test_append():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    assert str(linked_list) == "{ 3 } -> { 2 } -> { 1 } -> NULL"

def test_insert_before_at_head():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.insert_before(3, 4)
    assert str(linked_list) == "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"

def test_insert_before_middle():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.insert_before(2, 4)
    assert str(linked_list) == "{ 3 } -> { 4 } -> { 2 } -> { 1 } -> NULL"

def test_insert_after_end():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.insert_after(1, 4)
    assert str(linked_list) == "{ 3 } -> { 2 } -> { 1 } -> { 4 } -> NULL"

def test_insert_after_middle():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.insert_after(2, 4)
    assert str(linked_list) == "{ 3 } -> { 2 } -> { 4 } -> { 1 } -> NULL"
