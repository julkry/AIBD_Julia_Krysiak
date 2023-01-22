import pytest
import LinkedList

nodes = [
    ('AGH', 'Krakow', 1919),
    ('UJ', 'Krakow', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznan', 1919),
    ('PG', 'Gdansk', 1945)
]
typeAdd = [('start', "PG, Gdansk, 1945, \nUP, Poznan, 1919, \nUW, Warszawa, 1915, \nPW, Warszawa, 1915, "
                     "\nUJ, Krakow, 1364, \nAGH, Krakow, 1919, \n"),
           ('end', "AGH, Krakow, 1919, \nUJ, Krakow, 1364, \nPW, Warszawa, 1915, \nUW, Warszawa, "
                   "1915, \nUP, Poznan, 1919, \nPG, Gdansk, 1945, \n")]
drop = [
    (1, "UP, Poznan, 1919, \nUW, Warszawa, 1915, \nPW, Warszawa, 1915, \nUJ, Krakow, 1364, \nAGH, Krakow, 1919, \n"),
    (3, "PW, Warszawa, 1915, \nUJ, Krakow, 1364, \nAGH, Krakow, 1919, \n"),
    (2, "UW, Warszawa, 1915, \nPW, Warszawa, 1915, \nUJ, Krakow, 1364, \nAGH, Krakow, 1919, \n")]

remove = [('start', "UP, Poznan, 1919, \nUW, Warszawa, 1915, \nPW, Warszawa, 1915, \nUJ, Krakow, 1364, \nAGH, Krakow, "
                    "1919, \n"), ('end', "PG, Gdansk, 1945, \nUP, Poznan, 1919, \nUW, Warszawa, 1915, \nPW, Warszawa, "
                                         "1915, "
                                         "\nUJ, Krakow, 1364, \n")]


@pytest.mark.parametrize('type, expected', typeAdd)
def test_add_node_start(type, expected):
    linked_list = LinkedList.create_LinkedList()
    for node in nodes:
        currentNode = LinkedList.create_Node(node)
        if type == 'start':
            linked_list.AddAtStart(currentNode)
        if type == 'end':
            linked_list.AddAtEnd(currentNode)
    assert LinkedList.get_LinkedList(linked_list) == expected


@pytest.mark.parametrize('drop_no, expected', drop)
def test_drop(drop_no, expected):
    linked_list = LinkedList.create_LinkedList()
    for node in nodes:
        currentNode = LinkedList.create_Node(node)
        linked_list.AddAtStart(currentNode)
    assert LinkedList.get_LinkedList(linked_list.drop(drop_no)) == expected


@pytest.mark.parametrize('type, expected', remove)
def test_remove(type, expected):
    linked_list = LinkedList.create_LinkedList()
    for node in nodes:
        currentNode = LinkedList.create_Node(node)
        linked_list.AddAtStart(currentNode)
    if type == 'start':
        linked_list.RemoveAtStart()
    if type == 'end':
        linked_list.RemoveAtEnd()
    assert LinkedList.get_LinkedList(linked_list) == expected
