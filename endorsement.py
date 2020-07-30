class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# Working Solution
def remove_kth_from_end(head, k):
    start = head
    current = start
    previous = current
    count = 0
    if k == 0:
        return head
    while start.next != None:
        start = start.next
        if (count % k) == 0:
            previous = current
            current = start
            print(f"Previous became current: {previous.value}")
        # if start != None:
        print(f"Start moved 1: {start.value}")     
        count += 1
    if k - 1 > count:
        return head
    if previous != None:
        print(f"This is previous at end: {previous.value}")
    if current != None:
        print(f"This is current at end: {current.value}")
    
    if previous == head:
        new_head = head.next
        head.next = None
        return new_head
    if previous.next.next != None:
        after = previous.next.next
        remove = previous.next
        previous.next = after
        remove.next = None
    else:
        previous.next = None

    return head

def remove_kth_from_end2(head, k):
    start = head
    current = start
    previous = start
    count = 0
    if k == 0:
        return head
    while start.next != None:
        start = start.next
        if (count % k) == 0:
            previous = current
            current = start
        count += 1
    if k - 1 > count:
        return head
    if previous == head:
        new_head = head.next
        head.next = None
        return new_head
    if previous.next.next != None:
        after = previous.next.next
        remove = previous.next
        previous.next = after
        remove.next = None
    else:
        previous.next = None
    
    return head

one = ListNode(20)
two = ListNode(19)
three = ListNode(18)
four = ListNode(17)
five = ListNode(16)
six = ListNode(15)
seven = ListNode(14) 
eight = ListNode(13)
nine = ListNode(12)
ten = ListNode(11)
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten
k = 4
alternate_k = 0

x = remove_kth_from_end2(one, k)

one = ListNode(10)
two = ListNode(20)
three = ListNode(30)
four = ListNode(40)
five = ListNode(50)
one.next = two
two.next = three
three.next = four
four.next = five
k = 1

y = remove_kth_from_end2(one, k)

one = ListNode(200)
two = ListNode(100)
one.next = two
k = 2

z = remove_kth_from_end2(one, k)

one = ListNode(2)
two = ListNode(4)
three = ListNode(6)
one.next = two
two.next = three
k = 4

q = remove_kth_from_end2(one, k)

while x is not None:
    print(f"Linked List: {x.value}")
    x = x.next
print("\n")
while y is not None:
    print(f"Linked List: {y.value}")
    y = y.next 
print("\n")
while z is not None:
    print(f"Linked List: {z.value}")
    z = z.next 
print("\n")
while q is not None:
    print(f"Linked List: {q.value}")
    q = q.next