list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

if list1 is list2:
    print("list1 and list2 are same")

if list1 is not list3:
    print("list1 and list3 are different")
