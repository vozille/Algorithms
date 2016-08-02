"""
    Binary Indexed Tree
"""
def update_tree(bit,index,val):
    index += 1
    while index < len(bit):
        bit[index] += val
        index += index & -index
    return bit
def sum_till(bit,index):
    index += 1
    ans = 0
    while index > 0:
        ans += bit[index]
        index -= index & -index
    return ans
def main():
    s = [1,2,3,4,5]
    bit = [0]*6
    for i in range(5):
        update_tree(bit,i,s[i])
    print sum_till(bit,1)
main()
