class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

drinks = Node('drinks')
hot = Node('hot')
cold = Node('cold')
tea = Node('tea')
cofee = Node('cofee')
cola = Node('cola')
fanta = Node('fanta')

hot.left = tea
hot.right = cofee

cold.left = cola
cold.right = fanta

drinks.left = hot
drinks.right = cold

print(drinks.left.val)
