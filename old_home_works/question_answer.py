import random

r = 0
w = 0
num = 0
count_quest = 4

quest = ["2+2=?a1b2c3d4",
        "1+1=? . (a)1\n(b)2\n(c)3\n(d)4 . b",
        "3+3=? . (a)1\n(b)2\n(c)6\n(d)4 . c",
        "4+4=? . (a)1\n(b)2\n(c)3\n(d)8 . d",
        "What is the capital of France? . (a)Paris\n(b)Moscow\n(c)Ujan\n(d)Bern . a"]

quest = random.sample(quest, count_quest)

for i in quest:
    num +=1
    el = i.split(" . ")
    ms = input("Answer the question! Choosing any one letter from (a,b,c,d) list.\n%s\n%s\nAnswer: " %(el[0],el[1]))
    if ms == el[2]:
        r += 1
        print("Right answer")
    else: 
        w += 1
        print("Wrong answer")
    
    if num == count_quest:
        print("Final results!!!\nRight answers: %d\nWrong answers: %d" %(r,w))
