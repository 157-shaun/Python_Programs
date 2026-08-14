# my_dict={'name':'Shaun','age':23,'email':'shaungeorge593@gmail.com','name':'George'}
# print(my_dict)
# empty={}
# empty=dict()

# person=dict(name='shaun',age=23,email='shaungeorge593@gmail.com')
# print(person)

# students={"student1":{"name":'shaun',"age":23},"student2":{"name":"George","age":28}}
# print(students)

# student={"name":"John","age":45}
# # print(student["name"])
# student["age1"]=50
# print(student)

students={"student1":{"name":'shaun',"age":23},"student2":{"name":"George","age":28}}
# print(students["student2"]["name"])
# students.pop("student1")
# print(students)
# del students["student1"]
# print(students)

students.popitem()
print(students)
print(students.keys())
print(students.values())
print(students.items())


# print(students.get("student3"))
# print(students["student3"])
# numbers=[1,2,3]
# letters=['a','b','c']
# paired=list(zip(numbers,letters))
# print(paired)
# for num,letter in zip(numbers,letters):
    # print(f"number = {num}, letters={letter}")
    
# person=dict(zip(numbers,letters))
# print(person)

# zipped = zip(numbers,letters)
# numberslist,letterslist = zip(*zipped)
# print(numberslist)
# print(letterslist)

