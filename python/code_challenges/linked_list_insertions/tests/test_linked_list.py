import pytest
from linked_list.linked_list import LinkedList


def test_exists():
    assert LinkedList

#@pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


#@pytest.mark.skip("TODO")
#Can successfully instantiate an empty linked list
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


#@pytest.mark.skip("TODO")
#Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


#@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


#@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


#@pytest.mark.skip("TODO")
# Can properly insert multiple nodes into the linked list
# Can properly return a collection of all the values that exist in the linked list
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


#@pytest.mark.skip("TODO")
# Will return true when finding a value within the linked list that exists
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


#@pytest.mark.skip("TODO")
# Will return false when searching for a value in the linked list that does not exist
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert("lemon")

    assert not linked_list.includes("cucumber")


# @pytest.mark.skip("TODO")
# Can successfully add a node to the end of the linked list
def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"

# @pytest.mark.skip("TODO")
# Can successfully add multiple nodes to the end of a linked list
def test_append_multiple():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    linked_list.append("lemon")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> { lemon } -> NULL"

# @pytest.mark.skip("TODO")
# Can successfully insert a node before a node located in the middle of a linked list
def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
# Can successfully insert a node before the first node of a linked list
def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
# Can successfully insert after a node in the middle of the linked list
def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"

# @pytest.mark.skip("TODO")
# Can successfully insert a node after the last node of the linked list
def test_insert_after_last_node():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


# ------------------ Skipped Tests Below ------------------

@pytest.mark.skip("TODO")
def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


@pytest.mark.skip("TODO")
def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")
