
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, target, value):
        if target.left == None:
            target.left = Node(value)
        elif target.right == None:
            target.right = Node(value)
        else:
            self.insert(target.left, value)

def preorder(target, isroot = True):
    online = []
    if target != None:
        online.append(target.value)
        if target.left != None:
            temp = preorder(target.left, False)
            for i in temp:
                online.append(i)
        if target.right != None:
            temp = preorder(target.right, False)
            for i in temp:
                online.append(i)
    if isroot:
        tempstr = ""
        for i in online:
            tempstr += "{}, ".format(i)
        tempstr = tempstr[:-2]
        return tempstr
    else:
        return online

def postorder(target, isroot = True):
    online = []
    if target != None:
        online.append(target.value)
        if target.right != None:
            temp = postorder(target.right, False)
            for i in temp:
                online.append(i)
        if target.left != None:
            temp = postorder(target.left, False)
            for i in temp:
                online.append(i)

    if isroot:
        tempstr = ""
        for i in online:
            tempstr += "{}, ".format(i)
        tempstr = tempstr[:-2]
        return tempstr
    else:
        return online

def inorder(target, isroot = True):
    online = []
    if target != None:
        if target.right != None:
            temp = inorder(target.right, False)
            for i in temp:
                online.append(i)
        online.append(target.value)
        if target.left != None:
            temp = inorder(target.left, False)
            for i in temp:
                online.append(i)

    if isroot:
        tempstr = ""
        for i in online:
            tempstr += "{}, ".format(i)
        tempstr = tempstr[:-2]
        return tempstr
    else:
        return online


tree = Tree(1)

while True:
    online = []
    print(preorder(tree.root, True))
    print(postorder(tree.root, True))
    print(inorder(tree.root, True))

    tree.insert(tree.root, input("What would you like to put in next?: "))
