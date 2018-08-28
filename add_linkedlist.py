class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    root1 = l1
    root2 = l2
    root3 = ListNode(root1.val + root2.val)
    mylist = [root3]
    curr = root3
    i = 0
    print(root1, root2)
    while root1 != None or root2 != None:
        print(root1.val, root2.val)
        new_node = ListNode(root1.val + root2.val)
        root1 = root1.next
        root2 = root2.next
        print(new_node.val)
        mylist[i].next = new_node
        mylist.append(new_node)
        i +=1
        curr = new_node
        #
        #curr.next = new_node


    return root3

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

addTwoNumbers(l1, l2)
