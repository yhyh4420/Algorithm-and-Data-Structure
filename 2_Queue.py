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
            self.rear = (self.rear+1) % self.capacity
            self.array[self.rear] = item
        else:
            print('queue overflow')
            pass
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.capacity
            return self.array[self.front]
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
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.array[i % self.capacity], end=' ')
        print(']')
    
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity
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
#%%
'''
큐를 버퍼처럼 써보자
버퍼란? 오래된 데이터부터 삭제하는 enqueue방식 가지는 큐
ArrayQueue class의 enqueue2로 구현함
'''

a = ArrayQueue(8)

a.display('초기상태 : ')
for i in range(9):
    a.enqueue2(i)
    a.display('a 상태 : ')

a.enqueue2(9)
a.display('버퍼 적용 : ')
#%%
'''
덱이란? front와 rear 둘 다에서 삭제와 삽입이 가능한 자료구조
스택과 큐의 연산 둘 다 가능
본 구현에서는 '상속'(inheritance)의 개념을 사용할 것임
'''
class CircularDeque(ArrayQueue): # CircularDeque = 자식, ArrayQueue = 부모
    def __init__(self, capacity=10):
        super().__init__(capacity)  # 생성자는 상속 안되서 다시 만들어야 함. 부모의 생성자를 직접 호출
    
    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass
    
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else: pass
    
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass
#%%
dq = CircularDeque()
for i in range(9):
    dq.enqueue(i) if i%2 == 0 else dq.addFront(i)
dq.display('홀수는 front 짝수는 rear : ')

for i in range(2): dq.dequeue()
for i in range(2): dq.deleteRear()
dq.display('front 2회 삭제, rear 2회 삭제')
#%%
'''
파이썬은 queue모듈이 있다.
collections 모듈을 통해 deque를 호출할 수도 있다
'''
import collections

dq = collections.deque()

print('deque is not empty' if dq else 'deque is empty')
for i in range(9):
    if i % 2 == 0: dq.append(i) # rear로 삽입
    else: dq.appendleft(i) # front로 삽입
print(dq)

for i in range(2): dq.pop() # front 삭제
for i in range(3): dq.popleft() # rear 삭제
print(dq)
print('deque is not empty' if dq else 'deque is empty')
