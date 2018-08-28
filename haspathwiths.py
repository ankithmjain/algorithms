class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def hasPathWithGivenSum(t, s):
    #global mydict
    global found
    found = False
    mydict = {"sum": 0}
    if t is None:
        return False
    def cal_nodes(t, mydict):
        #print t.value
        global found
        mydict[t.value] = {'sum': t.value+ mydict["sum"]}
        #print mydict[t.value]["sum"]
        if t.left is None and t.right is None:
            if mydict[t.value]["sum"] == s:
                found = True
        #print mydict
        if t.left:
            cal_nodes(t.left, mydict[t.value])
        if t.right:
            cal_nodes(t.right, mydict[t.value])
    cal_nodes(t, mydict)
    return found

t = Tree(4)
t.left = Tree(1)
t.right = Tree(3)
t.left.left = Tree(-2)
t.left.left.right = Tree(3)
t.right.left = Tree(1)
t.right.right = Tree(2)
t.right.right.left = Tree(-2)
t.right.right.right = Tree(-3)

print hasPathWithGivenSum(t, 7)

def traverseTree(t):
    global mylist
    if not t:
        return []
    myqueue = [t]
    mylist = []
    while myqueue:
        curr = myqueue.pop(0)
        mylist.append(curr.value)
        if curr.left:
            myqueue.append(curr.left)
        if curr.right:
            myqueue.append(curr.right)
    return mylist


traverseTree(t)



