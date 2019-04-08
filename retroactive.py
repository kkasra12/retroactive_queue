class queue:
    __data = []
    __past = [] # this will save the past operations
    __future = [] # this will save the forward operations
     # this attributes r private
    '''
    to decreese the data overload, only changes will be saved
    history = [[function,value],...]
    in dequeue function , the enqueue will be saved and visa versa
    '''
    '''
    to decrease the complexity of insertation, the code will use to lists(past, future)
    the code will pop from past and pushes to future and visa versa
    '''
    def __init__(self): # constructor function
        self.operations_map = {True: self.__dequeue, False:self.__enqueue}
        self.operations_map_name = {False: "dequeue", True:"enqueue"}
    def enqueue(self,val):
        try:
            self.__data.append(val)
            self.__past.append([True,val])
            return True
        except:
            return False
    def dequeue(self):
        if len(self.__data)!=0:
            val = self.__data.pop(0)
            self.__past.append([False,val])
            return val
        else:
            raise Exception("Queue is empty!!!")

    def __enqueue(self,val,index=None):
        self.__data=[val]+self.__data
        # self.__past.append([True,val]) 
        return True
    def __dequeue(self,val,index=-1):
        if len(self.__data)!=0:
            val = self.__data.pop(index)
            # self.__past.append([False,val])
            return val
        else:
            raise Exception("Queue is empty!!!")
    
    def enqueue_items(self,values):
        for v in values:
            self.enqueue(v)

    def backward(self, count=1):
        if len(self.__past)<=count:
            raise Exception("not enough pasts!!!")
        for _ in range(count):
            op = self.__past.pop(-1)
            self.operations_map[op[0]](op[1],index=-1)
            self.__future.append(op)
    def forward(self, count=1):
        if len(self.__future)<=count:
            raise Exception("not enough future!!!")
        for _ in range(count):
            op = self.__future.pop(-1)
            # print(op)
            self.operations_map[not op[0]](op[1],index=0)
            self.__past.append(op)

    def delete_history(self,t):
        if t<=0:
            raise Exception("rollback time must be bigger than 0")
        self.backward(t)
        print("##",self,"##",self.__future)
        deleted_item=self.__future.pop()
        self.show_his()
        self.forward(t-1)
        return str(self.operations_map_name[deleted_item[0]]+"("+str(deleted_item[1])+")")

    def __len__(self):
        return len(self.__data)
    def __str__(self):
        return str(self.__data)
    def show_his(self):
        print("##",self.__past,"\n--",self.__future)

if __name__ == "__main__":
    a = queue()
    a.enqueue_items([1,2,3,4,5,6,7,8,9,0])
    print("length of queue:", len(a))
    print("data in queue:", a)
    print("dequeue:", a.dequeue())
    print("dequeue:", a.dequeue())
    print("enqueue(10):", a.enqueue(10))
    print("dequeue:", a.dequeue())
    print("dequeue:", a.dequeue())
    print("dequeue:", a.dequeue())
    print("dequeue:", a.dequeue())
    print("enqueue(11):", a.enqueue(11))

    print("data in queue:", a)
    print("rolling back 3 times...")
    a.backward(3)
    print("data in queue:", a)
    a.show_his()
    print("travel to future one time")
    a.forward()
    print("data in queue:", a)
    a.show_his()
    print("deleting 4 query ago:",a.delete_history(4))
    print("data in queue:", a)
