import unittest
from linked_challenges import *

class TestSumList(unittest.TestCase):

    def setUp(self) -> None:
        self.a = Node(2)
        self.b = Node(77)
        self.c = Node(6)
        self.d = Node(4)

        self.a.next = self.b 
        self.b.next = self.c
        self.c.next = self.d

    def test_sum_list(self):
        self.assertEqual(sum_list(self.a), 89)
    
    def test_find_item(self):

        self.assertFalse(find_item(self.a, 9))
        self.assertTrue(find_item(self.a, 4))

    def test_get_node(self):
       
        self.assertEqual(get_node(self.a, 2), 6)
        self.assertEqual(get_node(self.a, 7), None)
        self.assertNotEqual(get_node(self.a, 9), 77)

    def test_reverse_list(self):
       
        self.assertEqual(reverse_list(self.a), 4)

if __name__ == '__main__':
    unittest.main()