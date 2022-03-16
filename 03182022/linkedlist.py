#@Author: Trevor Kleinstuber
#@Last Modified: 15 March 2022

class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

  #assuming nodes with same value are the same node
  def equals(self, other):
    return self == other or (isinstance(other, Node) and self.value == other.value)


class SLinkedList:
  def __init__(self):
    self.head = None

  def push(self, value):
    temp = self.head
    self.head = value if isinstance(value, Node) else Node(value)
    self.head.next = temp
    return self

  def pop(self):
    temp = self.head
    if temp != None:
      self.head = temp.next
      temp.next = None
    return temp

  def get_tail(self):
    tail = self.head
    if(not tail):
      return None

    else:
      while tail.next:
        tail = tail.next
    return tail

  def append(self, value):
    tail = self.get_tail()
    new_node = value if isinstance(value, Node) else Node(value)
    if tail:
      tail.next = new_node
    else:
      self.head = new_node
    return self

  def add_all(self, arr):
    tail = self.get_tail()
    if not tail:
      if not arr:
        return self

      else:
        self.head = arr[0] if isinstance(arr[0], Node) else Node(arr[0])
        arr = arr[1:]
        tail = self.head
    for item in arr:
      new_node = item if isinstance(item, Node) else Node(item)
      tail.next = new_node
      tail = tail.next
    return self

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

  def insert_at(self, value, index):
    new_node = value if isinstance(value, Node) else Node(value)
    l = self.length()
    if index == 0 or index == -l:
      return self.push(value)

    else:
      temp = self.get_at(index - 1)
      tempnext = temp.next
      temp.next = new_node
      new_node.next = tempnext
      return self

  def remove_at(self, index):    
    l = self.length()
    if index == 0 or index == -l:
      return self.pop()

    else:
      prev = self.get_at(index - 1)
      temp = prev.next
      prev.next = temp.next
      temp.next = None
      return temp

  def to_s(self):
    string = "Singly linked list:\n"
    if self.head:
      temp = self.head
      i = 0
      while temp.next:
        string += "Value of node at index" + str(i) + ": " + str(temp.value) + "\n"
        temp = temp.next
        i += 1
      string += "Value of node at index" + str(i) + ": " + str(temp.value) +"\n"
    else:
        string = "Empty list"
    return string

def intersection(list1, list2):
  delta = len(list1) - len(list2)
  current1 = list1.head
  curren2 = list2.head
  while(delta>0):
    current1 = current1.next
    delta -= 1
  while(delta<0):
    curren2 = curren2.next
    delta += 1
  while(not current1.equals(curren2)):
    current1 = current1.next
    curren2 = curren2.next
  return current1

# def find_intesection(l1, l2):
#   # if(not(isinstance(l1, SLinkedList) and isinstance(l2, SLinkedList))):
#   #   raise TypeError
#   this = l1.head
#   while(this != None):
#     this.checked = True
#     this = this.next
#   that = l2.head
#   while(not that.checked):
#     that = that.next
#   r = None
#   if(that.checked):
#      r = that
#   this = l1.head
#   while(this != None):
#     this.checked = False
#     this = this.next
#   return r