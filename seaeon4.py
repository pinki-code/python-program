# conditional statement :-
# age=17
# if(age>=18):
#    print("can apply for licence")
# else:
#  print("you can't apply for licence")



# example for traffic light :-

# light=input("enter the signal you see:")
# if(light=="red"):
#   print("stop")
# elif(light=="green"):
#   print("go")
# elif(light=="yellow"): 
#     print("wait")
# else:
#     print("you are fool")

# example of giving vote :-
# age = 17
#if(age >= 18):
#    print("i can give the vote")
# else:
#    print("i can't give the vote")



# example of student mark sheet :-
# mark = int(input("enter your mark:"))
# if(mark>=90):
#  grade="A"
# elif(mark>=80 and mark<90):
#   grade="B"
# elif(mark>=70 and mark<80):
#    grade="C"
# elif(mark>=60 and mark<70):
#  grade="D"
# elif(mark>=50 and mark<60):
#     grade="E"
# else:
#     grade="F" 
# print("grade of student is -", grade)


# example of list :-
#list=[45,67,34,90,67,78]
# print(list)        #[45,67,34,90,67,78]
# print(type(list))  #[class 'list']
# print(type[0])     #type[0]
# print(list[1])     #67
# print(type[2])     # type[2]
# print(len(list))   #6


# example of slicing :-


# marks=[32,76,98,67,56,90]
# print(marks[1:5])    #[76,98,67,56]
# print(marks[3:5])   #[67,56]
# print(marks[:5])    #[32,76,98,67.56,90]
# print(marks[3:])    #[,67,56,90]

# example of list method :-

# list=[1,5,4]
#list.append(7)
# print(list)
#list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list.insert(2,9)
# print(list)
# list.pop(2)
# print(list)

num=int(input("enter a number:"))
if(num%2)==0:
   print("num is even:")
else:
   print("num is odd:")
   
   
num1=int(input("enter the 1st numbewr:"))
num2=int(input("enter the 2nd number:"))
num3=int(input("enter the 3rd number:"))
if(num1>=num2 and num1>=num3):
   greatest=num1
elif(num2>=num1 and num2>=num3):
   greatest=num2
else:
   greatest=num3
   print("the greatest number is:"greatest)
