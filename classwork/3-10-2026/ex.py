#implement queue using stack
class Stack:
    def __init__(self):
        self.values=[]
        self.top=-1

    def add(self,a):
        self.values.append(a)
        self.top+=1

    def delete(self):
        values=self.values.pop()
        self.top-=1

class Queue(Stack):
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def insert(self,a):
        self.stack1.add(a)

    def remove(self):
        if self.stack2.top==-1:
            while self.stack1.top!=-1:
                self.stack2.add(self.stack1.values.pop())
                self.stack1.top-=1
        self.stack2.delete()
