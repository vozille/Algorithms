class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class list:
    def __init__(self):
        self.head = None
        self.start = None

    def push_back(self, val):
        temp = node(val)
        if self.start == None:
            self.start = temp
            self.head = temp
            self.start.next = self.head
            self.head.next = None
        else:
            self.head.next = temp
            self.head = temp

    def insert(self, pos, val):
        newnode = node(val)
        if pos == 0:
            temp = self.start
            self.start = newnode
            self.start.next = temp
        else:
            i = self.start
            try:
                while pos > 1:
                    pos -= 1
                    i = i.next
                temp = i.next
                i.next = newnode
                newnode.next = temp
            except AttributeError:
                self.push_back(val)

    def erase(self, pos):
        i = self.start
        tmp = self.start
        while pos > 1:
            pos -= 1
            tmp = i
            i = i.next
        prev = i
        i = i.next
        print i.data,prev.data,tmp.data
        prev.next = None
        tmp.next = i


    def print_list(self):
        i = self.start
        while True:
            print i.data
            if i.next == None:
                break
            i = i.next
