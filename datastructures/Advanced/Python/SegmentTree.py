import sys
sys.stdin = open("input.txt","r")
# Fully upgraded Segment Tree
import math
"""
if you are not me...
  tstart = tree start
  qstart = query start
  rest are self explanatory
"""

def middle(start,end):
    return start + (end-start)/2

def MintreeCreate(arr,n):
    h = int(math.ceil(math.log(n,2)))
    stree = [0]*(2*2**h-1)
    fillMin(stree,0,n-1,arr,0)
    return stree
def fillMin(stree,tstart,tend,arr,index):
    if tstart == tend:
        stree[index] = arr[tstart]
        return arr[tstart]
    else:
        mid = middle(tstart,tend)
        stree[index] = min(fillMin(stree,tstart,mid,arr,index*2+1),fillMin(stree,mid+1,tend,arr,index*2+2))
    return stree[index]

def MaxtreeCreate(arr,n):
    h = int(math.ceil(math.log(n,2)))
    stree = [0]*(2*2**h-1)
    fillMax(stree,0,n-1,arr,0)
    return stree
def fillMax(stree,tstart,tend,arr,index):
    if tstart == tend:
        stree[index] = arr[tstart]
        return arr[tstart]
    else:
        mid = middle(tstart,tend)
        stree[index] = max(fillMax(stree,tstart,mid,arr,index*2+1),fillMax(stree,mid+1,tend,arr,index*2+2))
    return stree[index]

def SumtreeCreate(arr,n):
    h = int(math.ceil(math.log(n,2)))
    stree = [0]*(2*2**h-1)
    fillSum(stree,0,n-1,arr,0)
    return stree
def fillSum(stree,tstart,tend,arr,index):
    if tstart == tend:
        stree[index] = arr[tstart]
        return arr[tstart]
    else:
        mid = middle(tstart,tend)
        stree[index] = (fillSum(stree,tstart,mid,arr,index*2+1)+fillSum(stree,mid+1,tend,arr,index*2+2))
    return stree[index]


def getSum(stree,n,qstart,qend):
    return getSumTill(stree,0,n-1,qstart,qend,0)

def getSumTill(stree,tstart,tend,qstart,qend,index):
    if qstart <= tstart and qend >= tend:
        return stree[index]
    if tend < qstart or tstart > qend:
        return 0
    mid = middle(tstart,tend)
    return getSumTill(stree,tstart,mid,qstart,qend,index*2+1)+getSumTill(stree,mid+1,tend,qstart,qend,index*2+2)

def getMin(stree,n,qstart,qend):
    return getMinTill(stree,0,n-1,qstart,qend,0)

def getMinTill(stree,tstart,tend,qstart,qend,index):
    if qstart <= tstart and qend >= tend:
        return stree[index]
    if tend < qstart or tstart > qend:
        return 10**50
    mid = middle(tstart,tend)
    return min(getMinTill(stree,tstart,mid,qstart,qend,index*2+1),getMinTill(stree,mid+1,tend,qstart,qend,index*2+2))

def getMax(stree,n,qstart,qend):
    return getMaxTill(stree,0,n-1,qstart,qend,0)

def getMaxTill(stree,tstart,tend,qstart,qend,index):
    if qstart <= tstart and qend >= tend:
        return stree[index]
    if tend < qstart or tstart > qend:
        return -10**50
    mid = middle(tstart,tend)
    return max(getMaxTill(stree,tstart,mid,qstart,qend,index*2+1),getMaxTill(stree,mid+1,tend,qstart,qend,index*2+2))

def updateVal(arr,stree,n,i,new_value):
    difference = new_value - arr[i]
    arr[i] = new_value
    updateValTill(stree,0,n-1,i,difference,0)

def updateValTill(stree,tstart,tend,i,difference,index):
    if i < tstart or i > tend:
        return
    stree[index] += difference
    if tstart != tend:
        mid = middle(tstart,tend)
        updateValTill(stree,tstart,mid,i,difference,2*index+1)
        updateValTill(stree,mid+1,tend,i,difference,2*index+2)

n,q = map(int,raw_input().split())
arr = map(int,raw_input().split())
MinSegmentTree = MintreeCreate(arr,n)
MaxSegmentTree = MaxtreeCreate(arr,n)
while q > 0:
    q -= 1
    left,right = map(int,raw_input().split())
    left -= 1
    right -= 1
    print getMax(MaxSegmentTree,n,left,right)-getMin(MinSegmentTree,n,left,right)
