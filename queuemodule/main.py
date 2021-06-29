import queue as q

customq = q.Queue(maxsize=4)
print(customq.empty())
customq.put(1) #enq
customq.put(2)
customq.put(3)
customq.put(4)
print(customq.full())
print(customq.get()) # deq
print(customq.qsize())



 #same for mu;tiprocessing
 #from multiprocessing import queue
