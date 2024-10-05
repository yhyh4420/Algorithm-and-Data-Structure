# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 02:20:48 2024

@author: yehun_chang
"""

#%%
'''
Queue : 선입선출(First In First Out, FIFO) 구조
'''

# 원형 큐 구현(직선 큐는 많은 이동을 필요로 하기 때문)
class ArrayQueue:
    def __init__(self, capacity = 10): # capacity에 대한 별도 정의가 없으면 10으로 고정
        self.capacity = capacity
        self.front = 0  # 삭제가 일어나는 곳, queue의 앞
        self.rear = 0  # 삽입이 일어나는 곳, queue의 뒤
        self.array = [None]*capacity
        
    def isEmpty(self):
        # 삭제가 더이상 안일어나면 비어있는거, 즉 front index = rear index면 empty
        return self.front == self.rear
    
    def isFull(self): # queue가 꽉 차있는지, 가령 front가 9면 rear가 8이어야 하고 front가 0이면 rear가 9여야 함
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue(self, item): # rear 위치에 하나 추가하는거, rear index는 하나씩 더해야됨
        if not self.isFull():
            self.array[self.rear] = item
            self.rear = (self.rear+1) % self.capacity
        else:
            print('queue overflow')
            pass
    
    def dequeue(self):
        if not self.isEmpty():
            item = self.array[self.front]
            self.array[self.front] = None
            self.front = (self.front+1)%self.capacity
            return item
        else:
            print('queue underflow')
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else:
            print('que is empty')
            pass
    
    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity
    
    def display(self, msg):
        print(msg, end='[')
        for i in range(self.size()):
            print(self.array[(self.front+i) % self.capacity], end=' ')
        print(']')
#%%
import random
q = ArrayQueue()
q.display('초기상태')
while not q.isFull():
    q.enqueue(random.randint(1,100))
q.display('포화상태')
print('삭제순서 : [', end='')
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print(']')