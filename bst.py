class bst:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert(node,key):
    if node is None:
        return bst(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minvalue(node):
    current=node
    while current.left is not None:
        current=current.left
    return current
def deletenode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=deletenode(root.left,key)
    elif key>root.key:
        root.right=deletenode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minvalue(root.right)
        root.key=temp.key
        root.right=deletenode(root.right,temp)
    return root
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.key,end=" ")
        inorder(node.right)


root=None
n=1
while n!=4:
    print("\n 1.insert node , 2.delete node 3.inorder traversal 4.exit")
    n=int(input())
    if n==1:
        x=int(input())
        root=insert(root,x)
    if n==2:
        x=int(input())
        root=deletenode(root,x)
    if n==3:
        print("inorder traversal is :")
        inorder(root)
    if n==4:
        break