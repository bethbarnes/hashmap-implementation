#!/usr/bin/env python

#---------SOLUTION----------#

#define Node class
class Node:
  def __init__(self, key=None, val=None):
    self.next_node = None
    self.key = key
    self.val = val

#define Linked List class
class Linked_List:
  def __init__(self):
    self.head = None

#add new node to head
  def add_LL_node(self, key, val):
    new_node = Node(key, val)
    if self.head is not None:
      previous_head = self.head
      new_node.next_node = previous_head
    self.head = new_node

#iterate through Linked List to find node
  def find_node(self, key):
    curr_node = self.head
    while curr_node:
      if curr_node.key == key:
        return curr_node.val
      curr_node = curr_node.next_node
    raise KeyError('key not found')


#--------TESTS--------#
def main():

  print('test - creates nodes with passed in key, value and next properties')

  new_node = Node('John', 22)
  assert new_node.key == "John"
  assert new_node.val == 22
  assert new_node.next_node is None

  print('test - initializes empty Linked List')

  my_LL = Linked_List()
  assert my_LL.head is None

  print('test - can add nodes to Linked List')

  my_LL.add_LL_node('Jane', 24)

  assert my_LL.head.key == 'Jane'

  my_LL.add_LL_node('Robert', 36)
  my_LL.add_LL_node('Jason', 35)

  assert my_LL.head.key == 'Jason'
  assert my_LL.head.next_node.key == 'Robert'
  assert my_LL.head.next_node.next_node.key == 'Jane'

  print('test - can find nodes in Linked List by key')

  assert my_LL.find_node('Robert') == 36
  assert my_LL.find_node('Jason') == 35
  assert my_LL.find_node('Jane') == 24

  print('test - throws error if key not found in Linked List')

if __name__ == '__main__':
  main()
