from linkedlist import Node, SLinkedList, intersection

j = Node()

ending = SLinkedList()
ending.add_all(['a',50,Node('c')])
left = SLinkedList()
left.add_all([50.5,'foo',{'key':'value'}])
right = SLinkedList()
right.add_all(['virginia',[1,2,3],'marco','polo','green',1000,100000.5,SLinkedList.__dict__,'z'])
#print(right.at_index(-2).value)
right.get_tail().next = ending.head
left.get_tail().next = ending.head.next
print("expected: 50\nactual:")
print(intersection(left,right).value)

farleft = SLinkedList()
farleft.push(1).add_all([2,3])
farleft.get_at(-1).next = left.get_at(-2)

centrist = SLinkedList()
centrist.push(left.get_at(-1))
centrist.push('talkingpoints')
print("expected: c\nactual:")
print(intersection(farleft,centrist).value)

if([]):
  print("truthy")
else:
  print("falsy")

n1 = Node(5)
n2 = Node(5)
n3 = Node(6)
n4 = n3
n5 = Node(7)
n6 = Node(8)
n1.next = n3
n2.next = n3
print("test1")
print(n1 == n2)
print("test1b")
print(n1.equals(n2))
print("test2")
print(n3 == n4)
n3.next = n5
n4.next = n6
print("test3")
print(n3 == n4)
print("test4")
print(n3.next)

L = SLinkedList()
L.push(5).push(200).push(77)
print(L.to_s())
L.pop()
print(L.to_s())
print("\nlength\n")
print(L.length())

M = SLinkedList()
M.add_all([5,50,500,5000])
print(M.to_s())
print(M.get_tail().value)
print(M.get_at(0).value)
print(M.get_at(2).next.value)
print(M.get_at(-1).value)
try:
  print(M.get_at(10))
except IndexError as e:
  print("error fired succesfully")