# coding=utf-8
import unittest
from ai.models import SearchNode


class DummyProblem(object):
    def actions(self, state):
        return ['a1', 'a2', 'a3']

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == 'ia1'

    def cost(self, state1, action, state2):
        return 1


class TestSearchNode(unittest.TestCase):
    def setUp(self):
        self.problem = DummyProblem()
        self.node = SearchNode(state='i',
                               parent=None,
                               cost=0,
                               problem=self.problem,
                               depth=0)
        self.childs = self.node.expand()

    def test_expand_creates_node_for_each_action(self):
        self.assertEquals(len(self.childs), 3)

    def test_successors_have_correct_values(self):
        child = self.childs[0]
        self.assertEquals(child.state, 'ia1')
        self.assertIs(child.parent, self.node)
        self.assertEquals(child.action, 'a1')
        self.assertEquals(child.cost, 1)
        self.assertIs(child.problem, self.problem)
        self.assertEquals(child.depth, 1)

    def test_path(self):
        n1 = SearchNode(problem=self.problem, state='i', parent=None)
        n2 = SearchNode(problem=self.problem, action='a1', state='ia1', parent=n1)
        n3 = SearchNode(problem=self.problem, action='a2', state='ia1a2', parent=n2)

        path = [(None, 'i'), ('a1', 'ia1'), ('a2', 'ia1a2')]

        self.assertEquals(n3.path(), path)

    def test_equals(self):
        n1 = SearchNode(problem=self.problem, state='i', parent=None)
        n2 = SearchNode(problem=self.problem, state='i', parent=None)
        n3 = SearchNode(problem=self.problem, state='i', action='a1', parent=None)
        n4 = SearchNode(problem=self.problem, state='ia1', parent=None)

        self.assertTrue(n1 == n2)
        self.assertTrue(n1 == n3)
        self.assertFalse(n1 == n4)