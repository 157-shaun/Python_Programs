tuple1=(1,2,3,"Python","program")
# print(tuple1[-1])
# b=tuple()
# print(type(b))

# print(1 in tuple1)
# print(tuple1.count(1))
# print(tuple1.index("Python"))
# c=(10,11,12,13)
# print(tuple1+c)



# set
# emptyset=set()
# myset={"apple","banana","cherry","Apple"}
# print(myset)
# for i in myset:
#     print(i)
# myset.add("Mango")
# print(myset)

# myset.remove("orange")
# print(myset)
# myset.discard("apple")
# print(myset)

# set1={1,2,3}
# set2={3,4,5}
# print(set1|set2)
# print(set1&set2)
# print(set1-set2)
# print(set1^set2)

# seta={1,2}
# setb={1,2,3}
# print(seta.issubset(setb))
# print(setb.issuperset(seta))

import copy
original_list=[1,2,[3,4]]
# shallowcopied_list=copy.copy(original_list)
# shallowcopied_list[1]=99
# print(original_list)
# print(shallowcopied_list)


# deepcopied=copy.deepcopy(original_list)
# deepcopied[1]=99
# print(deepcopied)
# print(original_list)

# a=3
# b=0
# c=a/b
# print(c)
try:
    a=3
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("This will always execute")
    
    