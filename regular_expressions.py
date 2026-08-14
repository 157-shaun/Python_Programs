import re
# pattern = r"Hello"
# text = "hello world"
# matching = re.match(pattern,text)
# print(bool(matching))

# pattern = r"world"
# text = "hello world"
# search = re.search(pattern,text)
# print(bool(search))


# pattern = r"\d+"
# text = "order 5 laptop, 10 desktop, 15 keyboard"
# matches = re.findall(pattern,text)
# print(matches)

# text = "the sky is blue"
# new_text = re.sub(r"blue","red",text)
# print(new_text)


# pattern = r"^hello"
# text = "shaun hello world"
# result = re.search(pattern,text)
# print(result)


# pattern = r"hello$"
# text = "world hello"
# result = re.search(pattern,text)
# print(result)

# text = "python_123"
# result = re.findall(r"[a-zA-Z_]",text)
# print(result)

# gmail="shaun593@gmail.com"
# result = re.findall(r"[a-zA-Z_.1-9@]",gmail)
# print(result)

gmail="shungeorge593@gmail.com"
pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$"
if re.fullmatch(pattern, gmail):
    print("Valid")
else:
    print("Invalid")