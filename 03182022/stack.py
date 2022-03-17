#@Author: Trevor Kleinstuber
#@Last Modified: 17 March 2022

from linkedlist import Node
class Stack:
  def __init__(self):
    self.head = None
    self.max_head = None

  def push(self, new_value):
    temp = self.head
    test = self.max_head
    if not isinstance(new_value, Node):
      new_value = Node(new_value)
    self.head = new_value
    self.head.next = temp
    if not test or test.value <= new_value.value:
      self.max_head = Node(new_value.value)
      self.max_head.next = test
    return self

  def pop(self):
    temp = self.head
    if temp == None:
      raise LookupError('Attempt to pop item from empty stack')
    else:
      self.head = temp.next
      self.max_head = self.max_head.next if temp.value == self.max_head.value else self.max_head
      temp.next = None
    return temp
  
  def max(self):
    return self.max_head.value

  def __len__(self):
    i = 0
    temp = self.head
    while temp:
      i += 1
      temp = temp.next
    return i
    
  def length(self):
    return len(self)

  def __iter__(self):
    temp = self.head
    while(temp):
      yield temp
      temp = temp.next

  def __getitem__(self, index):
    if not isinstance(index, int):
      raise TypeError('index not an Integer')

    if index < 0:
      index = len(self) + index
      if index < 0:
        raise IndexError

    temp = self.head
    if temp:
      while index and temp.next:
        index  -= 1
        temp = temp.next
      if index and not temp.next:
        raise IndexError

    return temp
    
  def get_at(self, index):
    return self[index]

  def __str__(self):
    string = "["
    temp = self.head
    while temp:
      string += str(temp.value)
      if temp.next:
        string += ", "
      temp = temp.next
    string += "]"
    return string
