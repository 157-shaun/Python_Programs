# file=open("tuple.py",'r')
# content=file.read()
# print(content)
# file.close()

# with open("function.py","r") as file:
    # content=file.read()
    # print(content)
    
# with open("function.py","r") as file:
#     #  content=file.readline()
#      print(file.readline())
#      print(file.readline())
     
# with open("function.py","r") as file:
#     content=file.readlines()
#     for i in content:
#         print

# with open("new_file.py","a") as file:
#     file.write("#Hello world\n")
#     file.write("hiii")

with open("aadhar backside.jpeg","rb") as sourcefile:
    content = sourcefile.read()
    
with open("destination.jpg","wb") as destinationfile:
    destinationfile.write(content)
    
    
    
