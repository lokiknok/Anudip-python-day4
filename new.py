print ("hello world ","my fav color is back ", "my fav number is 5 ","i love ice ",True)
# data types
#ouput statement vise #argument paramter - rec
color = int(input("choose colorblack 1, white 2,blue 3 : "))
print(color) 
height=int(input("enter height : "))
# love_things=bool(input("do you like ice cream : (true/false) : "))
# print(height)

score=int(input("Enter score : "))

if(score>=90):
    grade="A"
elif(score>=60):
    grade="B"
elif(score>=50):
    grade="Fail"
print(grade)

 # fro when known number of loop here use for loop 
for i in range (10,-2):
    print (i)

fruit_list=["banana","cumber","radish","tomato","pineapple"]
for c_f in range(len(fruit_list)):
    print(fruit_list[c_f])
for i in fruit_list:
    print(i)

while(True):
    num=int(input("guess the number : "))
    if(num==5):
        print(True)
        break
    else:
        print("again ")    
total=0
while(True):
    km=int(input("enter how many km to drive : "))
    total+=km
    if total<=100:
        print("ok Do ! ")
        continue
    print("Go to put petrol Dudu !!!!!!")
    break
def count():
    a=int(input("enter countdown: "))
    a-=1
    print(a)
    if a<=0:
        return
    count()
    
                                                      
count()

