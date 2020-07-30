# Definition for singly-linked list.
class ListNode2:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        current = new_list
        # value1 = 0
        # value2 = 0
        carry = 0
        nodes1 = []
        nodes2 = []
        while l1 or l2 is not None:
            if l1:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0
            if l2:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0
            print(f"Value 1: {value1}, Value 2: {value2}")
            total = value1 + value2 + carry
            print(f"After *** Value 1: {value1}, Value 2: {value2}")
            merp = total % 10
            print(f"This is the total: {merp}")
            nodes1.append(value1)
            nodes2.append(value2)
            print(f"Nodes 1: {nodes1}, Nodes 2: {nodes2}")
            carry = total // 10
            print(f"Carry // 10: {carry}")
            current.next = ListNode(total % 10)
            print(f"Current Next Value: {current.next.val}")
            current = current.next
        if carry > 0:
            current.next = ListNode(carry)
        return new_list.next

def detectCycle(head: ListNode) -> ListNode:
    single = head
    double = head
    visited = set()
    while single:
        if double.next:
            double = double.next
        if single not in visited:
            visited.add(single)
        if single.next:
            single = single.next
        if double in visited:
            return double
        if double.next:
            double = double.next
        
        # if double.next.next:
        #     double = double.next.next
        # if single.next:
        #     single = single.next
        # if double is single:
        #     return single
        # if double.next:
        #     double = double.next
        
        
        # if double.next:
        #     double = double.next
        

    return ListNode(-1)

m_node1 = ListNode(3)
m_node2 = ListNode(2)
m_node3 = ListNode(0)
m_node4 = ListNode(-4)
m_node1.next = m_node2
m_node2.next = m_node3
m_node3.next = m_node4
m_node4.next = m_node1

m_node5 = ListNode(1)

m_node6 = ListNode(1)
m_node7 = ListNode(2)
m_node6.next = m_node7
m_node7.next = m_node6

x = detectCycle(m_node1)
# print(x.val)

x = detectCycle(m_node6)
# print(x.val)



node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node7 = ListNode(3) 
node4.next = node5
node5.next = node6
# node6.next = node7

node8 = ListNode(7)
node9 = ListNode(3)
node8.next = node9

node10 = ListNode(0)

node11 = ListNode(1)
node12 = ListNode(8)
node11.next = node12

node13 = ListNode(0)

node14 = ListNode(5)
node15 = ListNode(5)

solution = Solution()
# x = solution.addTwoNumbers(node1, node4)
# y = solution.addTwoNumbers(node10, node8)
# z = solution.addTwoNumbers(node11, node13)
# q = solution.addTwoNumbers(node14, node15)
# while x:
#     print(f"This is x: {x.val}")
#     x = x.next 
# while y:
#     print(f"This is y {y.val}")
#     y = y.next
# while z:
#     print(f"This is y {z.val}")
#     z = z.next
# while q:
#     print(f"This is y {q.val}")
#     q = q.next


def two_strings(s1, s2):
    char_set = set(s1)
    for c in s2:
        if c in char_set:
            return "YES"
    return "NO"

nums = [2, 7, 11, 15]
target = 9
def twoSum(nums: [int], target: int) -> [int]:
    quickness = set(nums)

    for num in nums:
        goal = target - num
        if goal in quickness:
            index1 = nums.index(num)
            index2 = nums.index(goal)
            return [index1, index2]


nums2 = [3,2,4]
target2 = 6
nums3 = [3, 3]
target3 = 6
nums4 = [2222222,2222222]
target4 = 4444444


def twoSum2(nums: [int], target: int) -> [int]:
    for i in range(len(nums)):
        goal = target - nums[i]
        index1 = i
        original = nums[i]
        nums[i] = target + 1
        quickness = set(nums) 
        if goal in quickness:
            index2 = nums.index(goal)
            return [index1, index2]
        nums[i] = original

def twoSum3(nums: [int], target: int) -> [int]:
    keys = [num for num in nums]
    values = [item for item in range(len(nums))]
    quickness = dict(zip(keys, values))
    for i in range(len(nums)):
        goal = target - nums[i]
        if goal in quickness:
            if i is not quickness[goal]:
                return [i, quickness[goal]]

def twoSum4(nums: [int], target: int) -> [int]:
    for i in range(len(nums)):
        goal = target - nums[i]
        for j in range(i + 1, len(nums)):
            if goal == nums[j]:
                print(i)
                return [i, j]

# x = twoSum4(nums, target)
# print(f"This is x: {x}")

# x = twoSum4(nums2, target2)
# print(f"This is x: {x}")

# x = twoSum4(nums3, target3)
# print(f"This is x: {x}")

# x = twoSum4(nums4, target4)
# print(f"This is x: {x}")

test1 = "abacabad"
test2 = "abacabaabacaba"
def first_not_repeating_character(s):
    counted_set = dict()
    for i in range(len(s)):
        letter = s[i]
        if letter in counted_set:
            counted_set[letter] += 1
        else:
            counted_set.setdefault(letter, 1)
     
    for letter in s:
        if counted_set[letter] is 1:
            return letter

    return "_"

       
x = first_not_repeating_character(test2)      
print(f"This is x: {x}")    
# print(f"This is repeating: {counted_set}")

head1 = [10, 20, 30, 40, 50]
k1 = 1

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def remove_kth_from_end(head, k):
    order = []
    current = head
    previous = current
    count = 0
    while current is not None:
        if count % k is 0:
            previous = current
        current = current.next

    print(f"Previous: {previous.val}, Current: {current.val}")

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

remove_kth_from_end(one, 0)   