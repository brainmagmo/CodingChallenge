from linkedlist import Node
class Stack:
  def __init__(self):
    self.head = None

  def push(self, value):
    temp = self.head
    self.head = value if isinstance(value, Node) else Node(value)
    self.head.next = temp
    return self

  def pop(self):
    temp = self.head
    if temp == None:
      raise LookupError('Attempt to pop item from empty stack')
    else:
      self.head = temp.next
      temp.next = None
    return temp
  
  def max(self):
    temp = self.head
    if not temp:
      raise LookupError('Attempt to search empty stack')
    m = temp.value
    while temp:
      #print("debug")
      #print(temp)
      m = temp.value if temp.value > m else m
      #print(m)
      temp = temp.next
    return m

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
