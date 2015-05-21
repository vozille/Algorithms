import math
"""
if you are not me...
  tstart = tree start
  qstart = query start
  rest are self explanatory
"""

def middle(start,end):
    return start + (end-start)/2

def tree_create(arr,n):
    h = int(math.ceil(math.log(n,2)))
    stree = [0]*(2*2**h-1)
    fill(stree,0,n-1,arr,0)
    return stree
def fill(stree,tstart,tend,arr,index):
    if tstart == tend:
        stree[index] = arr[tstart]
        return arr[tstart]
    else:
        mid = middle(tstart,tend)
        stree[index] = fill(stree,tstart,mid,arr,index*2+1)+fill(stree,mid+1,tend,arr,index*2+2)
    return stree[index]

def get_sum(stree,n,qstart,qend):
    return get_sum_till(stree,0,n-1,qstart,qend,0)

def get_sum_till(stree,tstart,tend,qstart,qend,index):
    if qstart <= tstart and qend >= tend:
        return stree[index]
    if tend < qstart or tstart > qend:
        return 0
    mid = middle(tstart,tend)
    return get_sum_till(stree,tstart,mid,qstart,qend,index*2+1)+get_sum_till(stree,mid+1,tend,qstart,qend,index*2+2)

def update_val(arr,stree,n,i,new_value):
    difference = new_value - arr[i]
    arr[i] = new_value
    update_val_till(stree,0,n-1,i,difference,0)

def update_val_till(stree,tstart,tend,i,difference,index):
    if i < tstart or i > tend:
        return
    stree[index] += difference
    if tstart != tend:
        mid = middle(tstart,tend)
        update_val_till(stree,tstart,mid,i,difference,2*index+1)
        update_val_till(stree,mid+1,tend,i,difference,2*index+2)

def main():
  arr = [1,2,3,4,5]
  n = len(arr)
  s = tree_create(arr,n)
  print get_sum(s,n,0,2)
  update_val(arr,s,n,1,10)
  print get_sum(s,n,0,2)
main()
