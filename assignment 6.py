# ques 1

num = []
for i in range (0,10):
    num.append(int(input("enter the no.")))
    print (num)

# ques 2

while true:
    print("true")

# ques 3

a=[]
b=[]
for i in range (0,4):
    number=int(input("enter the number"))
    a.append(number)
    print (a)
for i in a:
    b.append(i**2)
    print(b)

# ques 4

list=[3,"h",9.8]
intlist=[x for x in list if isinstance(x,int)]
print(intlist)
flist=[x for x in list if isinstance(x,float)]
print(flist)
strlist=[x for x in list if isinstance(x,str)]
print(strlist)

# ques 5

even=[]
odd=[]
for ki in range(1,101):
    if(i%2==0):
        even.append(i)
    else:
odd.append(i)
print(even)
print(odd)

#ques 6

for i in range(1,5):
    for l in range(1,i+1):
        print("*",end ="")
        print()

# ques 7

list={'rohit':19,'mohit':20,'sohit':21,}
search_age = input("provide age:")
search_age = int(search_age)
listofage={}
for name, age in list.items():
    if age == search_age:
        age = str(age)
        results = name + " " +age
        print (results)
        age2 = int(age)
        listofage[name] = listofage.get(name,0)+age2
        print (listofage)

# ques 8

l=[]
for i in range(0,5):
    num=int(input("enter the number"))
    l.append(num)
    print(l)
    12=[]
    a=int(input("enter the value to be deleted"))
    if a in 1:
        print (a)
        x=1.index(a)
        x=1.remove(a)
        print(1)




