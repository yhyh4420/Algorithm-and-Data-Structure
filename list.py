# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:40:15 2024

@author: yehun_chang
"""

#%%
'''
list : 가장 자유로운 선형 자료구조
list와 set의 차이점 : list는 순서가 있고 set은 순서가 없음

linked list
 1) 메모리에 흩어져 있는 요소를 링크로 연결해 하나로 관리하는 것, 링크의 수를 여러개로 늘리면 효율적으로 데이터를 관리할 수 있음
 2) 삽입, 삭제 용이(일반 리스트는 삽입 삭제 시 배열을 모두 뒤로 미루거나 앞으로 당겨야 하는데 linked list는 링크만 조절하면 됨)
'''

# 단순 연결 리스트 구현
# 먼저 노드부터 구현
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
    
    def append(self, node):
        if node not in self.link:
            node.link = self.link # node의 link가 self.link를 가리키게 함
            self.link = node
        else: pass
        
    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next
    
    
