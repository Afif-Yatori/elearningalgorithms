class Node:
    def __init__(self, nodevalue=None):
        self.nodevalue = nodevalue
        self.nextvalue = None #i realised at the end that i should have called nextvalue/prevvalue -> nextnode/prevnode instead but it was too late
        self.prevvalue = None

class DoubleList:
    def __init__(self):
        self.headnode = None

    def insert(self, startnode, nextnode): #it's basically the insert after node and insert at the end combined
        if startnode.nextvalue == None:
            startnode.nextvalue = nextnode
            nextnode.prevvalue = startnode
        else:
            a = startnode.nextvalue
            startnode.nextvalue = nextnode
            nextnode.prevvalue = startnode
            nextnode.nextvalue = a
            a.prevvalue = nextnode

    def changehead(self, node):
        if node == None:
            print("this node does not exist")
        else:
            a = self.headnode
            self.headnode = node
            self.headnode.nextvalue = a
            a.prevvalue = node

    def printlistrightoleft(self):
        printvalue = self.headnode
        while printvalue != None:
            print(printvalue.nodevalue)
            printvalue = printvalue.nextvalue

    def printlistlefttoright(self):
        printvalue = self.headnode
        while printvalue.nextvalue != None:
            printvalue = printvalue.nextvalue
        while printvalue != None:
            print(printvalue.nodevalue)
            printvalue = printvalue.prevvalue

    def removenode(self, node):
        if node == None:
            print("This node does not exist")
        elif node == self.headnode and self.headnode.nextvalue is not None:
            self.headnode = self.headnode.nextvalue
            self.headnode.prevvalue = None
        elif node == self.headnode and self.headnode.nextvalue is None:
            self.headnode = None
        else:
            curvalue = self.headnode
            while curvalue != node:
                curvalue = curvalue.nextvalue
            previous = curvalue.prevvalue
            next = curvalue.nextvalue
            previous.nextvalue = curvalue.nextvalue
            next.prevvalue = previous





mylist = DoubleList()
Nodea = Node("A")
mylist.headnode = Nodea
Nodeb = Node("B")
Nodec = Node("C")
Noded = Node("D")
mylist.insert(Nodea, Nodeb)
mylist.insert(Nodeb, Nodec)
mylist.removenode(Nodeb)
mylist.changehead(Noded)
mylist.printlistlefttoright()


