class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def insert(root, node):
    """"""
    if root is None:
        return node
    else:
        if node.value > root.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


# Driver program to test the above functions
# Let us create the following BST
#      50
#    /    \
#   30     70
#   / \    / \
#  20 40  60 80
root = Node(50)
insert(root, Node(30))
insert(root, Node(20))
#insert(r, Node(90))
insert(root, Node(40))
insert(root, Node(70))
insert(root, Node(60))
insert(root, Node(80))

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

#print("Preorder")
#preorder(root)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

#print("Postorder")
#postorder(root)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

#print("Inorder")
#inorder(root)

def distance_from_root(root, value):
    if root is None:
        return
    distance = 0
    print("current distance is ", distance, " root value is ", root.value)
    if root.value == value:
        return (distance + 1)
    if root.value < value:
        distance = distance_from_root(root.right, value)
        print("current distance from right is ", distance, " root value is ", root.value)
        return (distance + 1)
    if root.value > value:
        distance = distance_from_root(root.left, value)
        print("current distance from left is ", distance, " root value is ", root.value)
        return (distance + 1)



def trace_path_from_root(root, value, path_list=[]):
    if root is None:
        return
    if root.value == value:
        print(root.value)
        path_list.append(root.value)
        return value
    if value > root.value:
        print(root.value)
        path_list.append(root.value)
        trace_path_from_root(root.right, value, path_list)
    if value < root.value:
        print(root.value)
        path_list.append(root.value)
        trace_path_from_root(root.left, value, path_list)
    return path_list

mydict = trace_path_from_root(root, 80, [])
print("path trace", mydict)

def lca(root, value1, value2):
    value1_path = trace_path_from_root(root, value1, [])
    value2_path = trace_path_from_root(root, value2, [])
    print("value 1 path ", value1_path)
    print("value 2 path ", value2_path)
    while (value1_path != [] or value2_path != []):
        curr1 = value1_path.pop(0)
        curr2 = value2_path.pop(0)
        print("curr1 ", curr1, "curr 2", curr2)
        if curr1 != curr2:
            break
        lca = curr1
    return lca

lca_20_40 = lca(root, 20, 40)
print("LCA of 20 and 40 ", lca_20_40)


totaldistance = distance_from_root(root, 20)
print("Distance is", totaldistance)