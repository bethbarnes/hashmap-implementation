#!/usr/bin/env python

class Node:
  def __init__(self, key=None, val=None):
    self.next_node = None
    self.key = key
    self.val = val

class Linked_List:
  def __init__(self):
    self.head = None

  def add_LL_node(self, key, val):
    new_node = Node(key, val)
    self.head = new_node
    if self.head is not None:
      previous_head = self.head
      new_node.next_node = previous_head

  def find_node(self, key):
    curr_node = self.head
    while curr_node:
      if curr_node.key == key:
        return curr_node.val
      curr_node = curr_node.next_node
    raise KeyError('key not found')

def main():
  myLL = Linked_List()
  myLL.add_LL_node('beth', 24)
  myLL.add_LL_node('mom', 55)
  myLL.add_LL_node('dad', 60)
  # print(myLL.head.next.val)
  # print(myLL.find_node('mom'))
  # myLL.find_node('dad')

if __name__ == '__main__':
  main()
