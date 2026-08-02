from functools import reduce

numbers = [1,2,3,4,5]
print(list(map(lambda x: x*2, numbers)))
print(list(filter(lambda x: x%2==0, numbers)))
print(reduce(lambda x,y:x+y, numbers))

list1=[1,2,4,3,6,8]
# list2=[n for n in list1 if n%2==0]
list2=list(filter(lambda x: x%2==0,list1))
print(list2)

list3=list(filter(lambda x: x%2==1,list1))
print(list3)

list4=reduce(lambda x,y: x-y,list1)
print(list4)