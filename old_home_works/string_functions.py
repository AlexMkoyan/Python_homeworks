def sstrip(mv,el):
    a = ""
    for i in mv:
        if i not in el:
            a = a+i
    return a

print(sstrip("aaaaaahellobbbbb","ab"))

def ssplit(mv,el):
    a = 0
    b = 0
    lst = []
    for i in mv:
        b +=1 
        if i == el:
            lst.append(mv[a:b-1])
            a = b
        if b == len(mv):
            lst.append(mv[a:])  
    return lst
print(ssplit("hello,my,friend",","))

up = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
low = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def uupper(mv):
    output = ""
    for i in mv:
        if i in low:
            output += i
        else:
            num = 0
            for j in up:
                if i == j:
                    output += low[num]
                num += 1
    return(output)
print(uupper("Barev"))

def llower(mv):
    output = ""
    for i in mv:
        if i in up:
            output += i
        else:
            num = 0
            for j in low:
                if i == j:
                    output += up[num]
                num += 1
    return(output)
print(llower("BaReV"))

def rreplace(txt,w1,w2):
    lst = ssplit(txt," ")
    output = ""
    for i in lst:
        if i != w1:
            output += i + " "
        else:
            output += w2 + " "
    return output
print(rreplace("London is the capital of the United Kingdom", "capital","mayraqaxaq"))

def ffind(text,w):
    num = 0
    lst = []
    for i in text:
        if i == w:
            lst.append(num)
        num += 1
    return lst
print(ffind("London is the capital of the United Kingdom", "o"))
            


