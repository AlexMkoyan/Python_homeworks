################### 1 #####################
# def ssplit(inp1,el):
#     a = 0
#     b = 0
#     lst = []
#     for i in inp1:
#         b +=1 
#         if i == el:
#             lst.append(inp1[a:b-1])
#             a = b
#         if b == len(inp1):
#             lst.append(inp1[a:])  
#     return lst

# inp1 = "111*1111 222*2222 333*33 444*444"
# print(ssplit(inp1, " "))

################### 2 #####################
# def unique_keys(inp2):
#     return inp2.keys()

# inp2 = {"a":2, "b":1, "a":3, "c":5}
# print(unique_keys(inp2))

################### 3 ##################
def long_worlds(inp3):
    lst = inp3.split()
    out = []
    for i in lst:
        if len(i) >= 4:
            out.append(i)
    return out

inp3 = "sdfsdf sfsdfsdf sdfsfsfsf dd fff"
print(long_worlds(inp3))