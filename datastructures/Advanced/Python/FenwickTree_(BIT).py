"""
    Binary Indexed Tree
"""
def update_tree(bit,index,val):
    index += 1
    while index < len(bit):
        bit[index] += val
        index += index & -index # represent as sum of powers of 2
    return bit
def sum_till(bit,index):
    index += 1
    ans = 0
    while index > 0:
        ans += bit[index]
        index -= index & -index
        print index
    return ans
def main():
    s = [1,2,3,4,5,6,7,8,9,10]
    bit = [0]*11
    for i in range(10):
        update_tree(bit,i,s[i])
    print sum_till(bit,7)
main()
