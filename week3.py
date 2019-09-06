#week3, day13
list0 = [1,3,4, "A" , "B" ]
for w in list0:
    print(w)
list0 [0] = 7
print (list0 [0])
del list0 [2]
print(list0)

#week3, day14
thislist1 = ["A", "B", "C" , "B"]
print (thislist1[1:3])
if "A" in thislist1:
    print("Yes,'A'")
thislist2 = ["python"] * 3
print(thislist2)
a1 = ["Wejdan" , "Reem"]
a2 = ["Sara" , "Dalal"]
a3 = a1 + a2
print(a3)

#week3,day15
thislist3= [ "A", "B", "C"]
print(len(thislist3))
thislist3.append("F")
print(thislist3)
thislist3.insert(2, "D")
print(thislist3)
thislist3.remove("A")
print(thislist3)
thislist3.pop()
print(thislist3)

mylist= thislist3.copy()
print(mylist)

mylist2 = list(thislist3)
print(mylist2)
code = list(("Java" , "Python" , "C++"))
print(code)
thislist3.clear()
print(thislist3)

#week3,day16
x = ()
print(x)
y = (7,)
print(y)
thistuple = ("A" , 1.3 , 5 , "بايثون" )
print (thistuple)
print(thistuple[0:2])
#del thistuple
#print(thistuple)


#week3,day17
t = ("apple" , "banana" , "cherry")
if "apple" in t :
    print("Yes,'apple' is in the frius tuple")

    thistuple3 = ("Python" ,) * 4
    print(thistuple3)


thistuple4 = (1,2,3,4)
thistuple5 = (5,6)
thistuple6 = thistuple4 + thistuple5
print (thistuple6)
v1 =(3,4,5,6)
V1 = v1 + (1,2)
print(v1)
print(len(t))
thislistt = [77,8,9, "J" , "L"]
thistuple2 = tuple (thislistt)
print(t)
print(t[0])

#Quiz3,week3,day18,19

Quizlist = [1,2,3, "Wejdan" , "Ayed"]

print(len(Quizlist))

Quizlist.insert(5, "Alenzi")
print(Quizlist)

Quizlist.remove(3)
print(Quizlist)

Quizlist.pop()
print(Quizlist)

Quiztuple = ("java" , "Python" , "swift")
if "Python" in Quiztuple:
    print("Yes")








