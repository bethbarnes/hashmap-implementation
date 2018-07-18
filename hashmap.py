#!/usr/bin/env python

from linkedlist import Linked_List

#---------SOLUTION----------#

#define Hash Map class
class Hash_Map:
  hash_length = 26
  hash_arr = [None] * hash_length

#simple hashing function
  def hash(self, key):
    if type(key) is str:
      return ord(key[0]) % self.hash_length
    elif type(key) is int:
      return  ord(str(key)[0]) % self.hash_length

#add key and value to hash map
  def add_to_hash(self, key, val):
    hash_num = self.hash(key)
    #handle collisions
    if self.hash_arr[hash_num] is None :
      self.hash_arr[hash_num] = Linked_List()
    self.hash_arr[hash_num].add_LL_node(key, val)

#find key in hash map and return value
  def look_up(self, key):
    hash_num = self.hash(key)
    if self.hash_arr[hash_num] is None :
      raise KeyError(f'key ({key}) not found')
    else :
      return self.hash_arr[hash_num].find_node(key)


#--------TESTS--------#
def main():

  print('test - initializes empty hash map with no keys or values')

  inventory_hash = Hash_Map()

  try:
    inventory_hash.look_up('apple')
  except KeyError as e:
    assert e.args[0] == 'key (apple) not found'

  print('test - can hash strings and numbers as keys')

  assert inventory_hash.hash('pineapple') == 8
  assert inventory_hash.hash(267) == 24

  print('test - adds key and value to hash map, can lookup keys')

  inventory_hash.add_to_hash('apples', 30)
  inventory_hash.add_to_hash('oranges', 50)

  assert inventory_hash.look_up('apples') == 30
  assert inventory_hash.look_up('oranges') == 50

  print('test - handles collisions')

  inventory_hash.add_to_hash('bananas', 25)
  inventory_hash.add_to_hash('beans', 15)

  assert inventory_hash.look_up('bananas') == 25
  assert inventory_hash.look_up('beans') == 15


if __name__ == '__main__':
  main()
