import random

inp = input("Enter your name: ")
file=open("questions.txt")
lines=file.read().split('\n')
file.close()

questions = []
while len(questions) < 5:
    ques = random.choice(lines)
    if ques not in questions:
        questions.append(ques)

md = {}
xp = 0
for el in questions:
    q, a = el.split("?")
    md[q] = a.split(",")

for q, a in md.items():
    print(q)
    ca= a[0]
    random.shuffle(a)
    cnt = 1
    for el in a:
        print(cnt, el)
        cnt += 1
    answer = input("input your answer: ")
    if answer== ca:
        print("Correct")
        xp +=1
    else:
        print("Incorrect. Correct answer was ", ca )
print("%s you got %d/%d" %(inp,xp, len(md)))


f = open("top.txt", "a")
out = inp + "-" + str(xp) + "\n" 
f.write(out)
f.close()

####### take results file and sort
fi=open("top.txt")
lines=fi.read().split('\n')
slist=sorted(lines[:-1],key = lambda x:x[-1]) 
fi.close()

ff = open("top.txt", "w")
for i in slist[::-1]:
    ff.write(i+"\n")
ff.close()




