####1
# lst = [1,2,3,"hkuhukh",4,"sdfdsf"]
# def cnt_num(inp):
#     cnt = 0
#     for i in inp:
#         if type(i) == int:
#             cnt += i 
#     return cnt
# print(cnt_num(lst))

###2
# def cnt_str(*args):
#     cnt = 0
#     for i in args:
#         if type(i) == str:
#             cnt += 1 
#     return cnt
# print(cnt_str(1,2,3,"dfsdf",4,"dfds"))

# ###3
# def mean_num(*args):
#     num = 0
#     for i in args:
#         num += i
#     return num/len(args)
# print(mean_num(1,2,3,4,5))

###4
# def aa(num1,num2):
#     out = {"Addition":num1 + num2,"Subtraction":num1 - num2}
#     return out
# print(aa(5,7))

###5
# up = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# low = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# def uupper(mv):
#     output = ""
#     for i in mv:
#         if i in low:
#             output += i
#         else:
#             num = 0
#             for j in up:
#                 if i == j:
#                     output += low[num]
#                 num += 1
#     return(output)
# print(uupper("Barev"))

###6
# def llower(mv):
#     output = ""
#     for i in mv:
#         if i in up:
#             output += i
#         else:
#             num = 0
#             for j in low:
#                 if i == j:
#                     output += up[num]
#                 num += 1
#     return(output)
# print(llower("BaReV"))

###7
# def ttitle(inp):
#     return inp[0].upper()+inp[1:]
# print(ttitle("barev"))

###8
# def hak(inp):
#     return inp[::-1]
# print(hak("barev"))

###9
# def mijakayq(a,b,c):
#     out = ""
#     for i in range(len(a)):
#         if i >= b and i <= c:
#             out += a[i]
#     return out
# print(mijakayq("barev",1,3))

###10
# def max_word(inp):
#     lst = []
#     sp = inp.split()
#     for i in sp:
#         lst.append(len(i))
#     res = lst.index(max(lst))
#     return sp[res]
# print(max_word("London is the capital of the United Kingdom"))

###11
# def let_count(inp):
    # r = 0
    # l = ""
    # for i in inp:
    #     p = inp.count(i)
    #     if i.isalpha() and p > r:
    #         r = p
    #         l = i
    # return l + "-" + str(r)
# print(let_count("London is the capital of the United Kingdom"))

###12
# def word_letter(inp):
#     w = max_word(inp)
#     ml = let_count(w)
#     return ml
# print(word_letter("London is the capital of the United Kingdom"))

###13
# def el(txt,nm):
#     return txt[nm] +","+ txt[-nm]
# print(el("United",2))

###15
# def isPolyndrom(mstr):
#     out = None
#     if mstr == mstr[::-1]:
#         out = "True"
#     else:
#         out = "False"
#     return out
# print(isPolyndrom("oso"))

###17
# def sum_numbers(nm):
#     inp = str(nm)
#     return int(inp[0]) * int(inp[-1])
# print(sum_numbers(236))

###18
# def count_str(inp):
#     num = 0
#     for i in inp:
#         if type(i) == str:
#             num += 1
#     return num
# print(count_str([1,"k","t",8,7,"a"]))

###19
# def max_num(inp):
#     mx = 0
#     for i in inp:
#         if type(i)== int or type(i)== float and i > mx:
#             mx = i
#     return mx
# print(max_num([1,"k","t",8,7.8,"a"]))

###20
# def nm(inp):
#     nm = []
#     for i in inp:
#         if type(i)==int  and i/10 >= 1 and i%2==0:
#             nm.append(i)
#     return nm
# print(nm([1,"k","t",80,7,25,"a",22]))

###21
# def a(inp):
#     sm = 0
#     ct = 0
#     for i in inp:
#         if type(i)==int  or type(i)==float:
#             sm += i
#             ct += 1
#     return sm/ct
# print(a([1,"k","t",80,7,25,"a",22]))

###22
# def lst(inp):
#     out = []
#     for i in inp:
#         out.append(len(i))
#     return out
# print(lst(["a","aa","aaa"]))

###23
# def srt(inp):
#     all = inp
#     for i in range(1, len(all) - 1):
#         for j in range(len(all)-i):
#             if all[j] < all[j+1]:
#                 all[j],all[j+1] = all[j+1],all[j]
#     return all
# print(srt([3,1,5,5,5646,646,54,65,654,56,4,1,2121,8]))

###24
# def srt(inp):
#     all = inp
#     for i in range(1, len(all) - 1):
#         for j in range(len(all)-i):
#             if len(all[j]) < len(all[j+1]):
#                 all[j],all[j+1] = all[j+1],all[j]
#     return all
# print(srt(["sfsf","sdsdju","sfdgdgdgdhfg","y","jnj"]))

###26
# def a(inp):
#     cnt = 0
#     sent = None
#     for i in inp:
#         nv = i.split()
#         if len(nv)>cnt:
#             cnt = len(nv)
#             sent = i
#     return sent

###27
# def num_let(inp):
#     num = 0
#     for i in inp:
#         if i.isdigit() and int(i) > num:
#             num = int(i)
#     return num
# print(num_let("kjkjhjknjkn ljjkjk8jk jknkjjkn 9jnkn "))

