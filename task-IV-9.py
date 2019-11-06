node = []

def Node(number):
    node = [number]

def addNode(number):
    node.append(number)
    return node.sort()

root = Node(50)
root = addNode(30) 
root = addNode(20) 
root = addNode(40) 
root = addNode(70) 
root = addNode(60) 
root = addNode(80) 

print("Sorted tree \n", node)
# root.sorted()
