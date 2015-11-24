__author__ = 'Ajithkumarsekar'
list=[2,7,-12,4,100,241,92]
#Always strings should be under double quotations
print(list)

list.sort()
print("List after sorting[ list.sort()] \n",list)

list.sort(reverse=True)
print("List after sorting in Reverse order[ list.sort(reverse=True)]\n ",list)

print("To print list from paticular index[ list[1:3]]\n",list[1:3])

print("Minimum element on the list[min(list)]\n ",min(list))

print("Maximum elemeent on the list[ max(list)]\n ",max(list))

print("Length of the list[ len(list)] \n",len(list))

print("List.pop()removes the last element and returns it[ list.pop()]\n",list.pop())

list[2]=int(input("Enter the element you want to replace @ index 2:"))
print(list)

list1=['Kumar','Sekar','Python','Ruby']
print(list1)

print("Length of a string in a list[ len(list[3])]\n",len(list1[3]))

list0=[]
list0=list+list1
print("After concading two list [ list0=list+list]\n",list0)

list1.remove('Ruby')
print("To remove a element from the list[ list1.remove('Ruby') ]\n",list1)

list.extend(list1)
print("Appends the contents of seq to list [list.append(list)]\n",list)

