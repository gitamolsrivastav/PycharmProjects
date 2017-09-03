class stack2Queue:

    def __init__(self):

        self.instack = []
        self .outstack = []


    def enqueue(self, element):
        return self.instack.append(element)

    def dequeue(self):

        if not self.outstack:
            while self.instack:
                return self.outstack.append(self.instack.pop())
        return self.outstack.pop()


