# Python program to demonstrate insert operation in binary search tree
import sys
# A utility class that represents an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


# A utility function to do inorder tree traversal

def inorder(root):
    if root:
        #print root.val
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print (root.val)
        preorder(root.left)
        preorder(root.right)
        #print(root.val)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print (root.val)

def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if (root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if (root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root


def printKDistant(root, k):
    if root is None:
        return
    if k == 0:
        print (root.data,)
    else:
        printKDistant(root.left, k - 1)
        printKDistant(root.right, k - 1)


def distance_from_root(root, val):
    if root is None:
        return
    dist = 0
    if root.val == val:
        return dist + 1
    if val > root.val:
        dist = distance_from_root(root.right, val)
        return dist + 1
    if val < root.val:
        dist = distance_from_root(root.left, val)
        return dist +1
INF = 10000000
NEG_INF = -1000000

def isBalancedInt(root):
    if root == None:
        return -1;
    left = isBalancedInt(root.left)
    right = isBalancedInt(root.right)
    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1
    return max(left, right) + 1

# Driver program to test the above functions
# Let us create the following BST
#      50
#    /    \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
#insert(r, Node(90))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
print("Inorder")
inorder(r)
print ("Preorder")
preorder(r)
print ("Postorder")
postorder(r)
print ("distance")
print (distance_from_root(r, 70))
#printKDistant(r, 2)
print (isBalancedInt(r))
