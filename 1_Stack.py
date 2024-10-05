# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 19:56:10 2024

@author: yehun_chang
"""
#%%
'''
Stack 공부
Stack는 쌓는거, LIFO(Last in, First Out)
'''
capacity = 10 # 스택의 용량
array = [None] * capacity # 스택 정의, 길이가 capacity인 스택 만들어짐(array형태)
top = -1 # 상단의 index : 공백 상태로 초기화(-1은 비어있는거)

def isEmpty():  # 스택이 비었는지 안비었는지 확인, top이 -1이면 비어있는거고 아니면 안비어있는거임
    return top == -1

def isFull():  # 스택이 다 차있는지 확인, top이 capacity-1이면 다 차있는거임(list의 index는 0부터 시작하니까)
    return top == capacity-1

def push(e):  # 스택에 넣는 함수 정의, 만약 isFull=True면 못넣음
    if isFull():
        print('stack overflow') # Stack이 넘쳐흐르는 경고문구
        exit() # 프로그램 종료
    else:
        top += 1 # stack 맨 위 index를 +1 해줌
        array[top] = e # 더한 index에 e 복사
        
def pop():
    if isEmpty():
        print('stack underflow')  # stack에 아무것도 없어서 element를 못뺀다는 경고
        exit() # 프로그램 종료
    else:
        top -= 1 
        return array[top+1]
    
def peek():# pop과 유사하지만, pop은 element를 완전히 빼는건데 peek는 top이 뭔지 확인만 하는 거
    if isEmpty():
        print('empty stack')
        pass
    else:
        return array[top]
    
def size(): # stack의 size
    return top+1
#%%
'''
위에서 정의한 stack의 구성요소들을 한 class로 정의해보자
'''
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1
    
    def isFull(self):
        return self.top == self.capacity-1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, item):
        if self.isFull():
            print('stack oveflow')
            pass
        else:
            self.top += 1
            self.array[self.top] = item
            
    def pop(self):
        if self.isEmpty():
            print('stack underflow')
            pass
        else:
            self.top -= 1
            return self.array[self.top+1]
            
    def peek(self):
        if self.isEmpty():
            print('empty')
            pass
        else:
            return self.array[top]
    
    def size():
        return self.top + 1
#%%
'''만든 array class 테스트'''
a = ArrayStack(1000)
msg = input('문자열을 입력하세요:')
for c in msg:
    a.push(c)
    
while not a.isEmpty():
    print(a.pop(), end='')
#%%
'''
괄호 검사 함수 구현
괄호 : (), {}, []
괄호가 제대로 닫혀있는지 확인

조건 1. 왼괄호 개수와 오른괄호 개수가 동일
조건 2. 같은 종류의 경우 왼괄호가 오른괄호보다 먼저 출현
조건 3. 다른 종류의 괄호가 교차하면 안됨
'''

def check(code):
    stack = ArrayStack(1000) # stack capacity 설정
    for ch in code:
        if ch in ('(','{','['):
            stack.push(ch)  # 기준은 왼괄호, 왼괄호는 모두 stack에 쌓음
        elif ch in (')', '}', ']'): # 조건 2 체크, 오른괄호가 먼저 나오는지 확인하는 과정
            if stack.isEmpty():
                return False
            else:
                left = stack.pop() # 왼괄호를 pop해서 오른괄호랑 짝으로 구성되는지 확인
                if (left != '(' and ch == ')') or (left != '{' and ch == '}') or (left != '[' and ch == ']'):
                    return False
    return stack.isEmpty() # 최종적으로 pop이 끝나면 stack은 비어야 함
#%%
'''
python 내장 모듈 사용
'''
s = list()

msg = input('문자열을 입력하세요 : ')
for ch in msg:
    s.append(ch)  # list의 append가 stack의 push
print(f'리스트 pop 전 : {s}')

while len(s) != 0: # len은 stack의 size 함수와 동일
    print(s.pop(), end='')
#%%
'''
queue라이브러리를 사용해보자

queu라이브러리 : 스택, 큐, 우선순위 큐 등 제공'''
import queue

s = queue.LifoQueue(maxsize=20) # LifoQueue가 stack, maxsize 파라미터는 capacity

msg = '안녕하세요'
for ch in msg:
    s.put(ch) # queue 라이브러리에서 push역할이 put임

print('pop결과 출력 : ', end='')
while not s.empty():  # isEmpty 역할 수행
    print(s.get(), end='')
#%%
'''
스택은 운영체제에서도 중요한 역할을 수행
같은 일을 되풀이할 때 반복문도 되지만 순환이나 재귀로도 가능
**순환이란?
 - 함수가 자기 자신을 호출하여 문제를 해결하는 기법
 - 문제 자체가 순환적(팩토리얼, 하노이탑)이거나 순환적으로 정의되는 자료구조(이진트리)에 적합
 - 보통 반복문이 순환보다 함수 호출 소요가 적고 시스템 스택을 적게 사용하지만, 특정한 문제(이진트리, 퀵정렬)등에서 효율적임
'''
def factorial(x):
    if x == 1:
        return 1  # 순환식으로 함수를 구성할 때는 무조건 멈추는 포인트가 있어야 함
    else:
        return x*factorial(x-1)

def hanoi_tower_f(n, start, temp, finish):
    if n == 1:
        print(f'원판 1 : {start} -> {finish}')
    else:
        hanoi_tower(n-1, start, finish, temp)
        print(f'원판 {n} : {start} -> {finish}')
        hanoi_tower(n-1, temp, start, finish)

class hanoi_tower:
    def __init__(self, n, start, temp, finish):
        self.n = n
        self.start = start
        self.temp = temp
        self.finish = finish
        self.list = []
    
    def moving(self, n, start, temp, finish):
        if n == 1:
            self.list.append(f'원판 1 : {start} -> {finish}')
        else:
            self.moving(n-1, start, finish, temp)
            self.list.append(f'원판 {n} : {start} -> {finish}')
            self.moving(n-1, temp, start, finish)
    
    def answer(self):
        self.moving(self.n, self.start, self.temp, self.finish)
        return self.list
    
a = hanoi_tower(100,'A','B','C')
len(a.answer())
#%%













