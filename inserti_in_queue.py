size=int(input("enter size of queue"))
q=[0]*size
front=-1
rear=-1

for i in range(len(q)):
    item=int(input("enter  value for inseting"))
    if rear==size-1:
        print("queue is over flow")
    elif front == -1 and rear == -1:
        front=rear=0
        q[rear]=item
    else:
        rear+=1
        q[rear]=item

print(q)