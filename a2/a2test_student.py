"""
Assignment 2: Quadtree Compression

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the test suite
"""

import pytest
from a2tree import QuadTreeNode, QuadTreeNodeEmpty, QuadTreeNodeLeaf
from a2tree import QuadTreeNodeInternal, QuadTree

"""
Test cases
"""


def test_split_quadrants_1():
    tree = QuadTree(0)
    lst = tree._split_quadrants([[1, 2], [3, 4]])
    result = [[[1]], [[2]], [[3]], [[4]]]
    assert lst == result


def test_split_quadrants_2():
    tree = QuadTree(0)
    lst = tree._split_quadrants([[1, 2], [3, 4], [5, 6]])
    result = [[[1]], [[2]], [[3], [5]], [[4], [6]]]
    assert lst == result


def test_split_quadrants_3():
    tree = QuadTree(0)
    lst = tree._split_quadrants([[1, 2, 3, 4]])
    result = [[[]], [[]], [[1, 2]], [[3, 4]]]
    assert lst == result


def test_restore_from_preorder_1():
    tree = QuadTree(0)
    tree.build_quad_tree([[1, 2], [3, 4]])
    preorder_string = tree.preorder()
    lst = preorder_string.split(',')
    node = QuadTreeNodeInternal()
    node.restore_from_preorder(lst, 0)
    assert node.children[2].value == tree.root.children[2].value


def test_restore_from_preorder_2():
    tree = QuadTree(0)
    tree.build_quad_tree([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    preorder_string = tree.preorder()
    lst = preorder_string.split(',')
    node = QuadTreeNodeInternal()
    node.restore_from_preorder(lst, 0)
    value1 = node.children[2].children[1].value
    value2 = tree.root.children[2].children[1].value
    assert value1 == value2


def test_restore_from_preorder_3():
    tree = QuadTree(0)
    tree.build_quad_tree([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    preorder_string = tree.preorder()
    lst = preorder_string.split(',')
    node = QuadTreeNodeInternal()
    num = node.restore_from_preorder(lst, 0)
    assert num == len(lst)


if __name__ == '__main__':

    pytest.main(['a2test_student.py'])
