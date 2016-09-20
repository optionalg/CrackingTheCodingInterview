#An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
#People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
#can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
#They cannot select which specificanimal they would like. Create the data structures to maintain this
#system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat. You may use the
#built-in LinkedList data structure
#Used arrays instead. 
class AnimalShelter():
    def __init__(self):
        self.catQ=Queue()
        self.dogQ=Queue()
        self.timeStamp=0

    def enQ(self,x):
        if x=='cat':
            self.catQ.enQ(self.timeStamp)
            self.timeStamp=self.timeStamp+1
        if x=='dog':
            self.dogQ.enQ(self.timeStamp)
            self.timeStamp=self.timeStamp+1

    def deQAny(self):
        if self.catQ.peek > self.dogQ.peek:
            self.dogQ.deQ()
        if self.catQ.peek < self.dogQ.peek:
            self.catQ.deQ()

    def deQDog(self):
        self.dogQ.deQ()

    def deQCat(self):
        self.catQ.deQ()