# center(width)= returns a centered version of the string with the specified width

# text = "hello"
# result = text.center(20)
# print(result)

# count(substring) = returns the number version of the string with the specified width

# text = "apple orange apple banana"
# count = text.count("apple")
# print(count)

# endswith(suffix) = description:returns true if the string ends with the specified suffix

# file_name = "muhammed fahis"
# result = file_name.endswith("fahis")
# print(result)

# find(substring) = count the space the word is starting

# sentence = "machine learning is fascinating"
# index = sentence.find("learning")
# print(index)

# the format() = method is a built in string 

# text = "this is {} and {}"
# formatted_text = text.format("one","two")
# print(formatted_text)

# text = "my name is {name} and iam {age} years old"
# formatted_text = text.format(name="john",age =25)
# print(formatted_text)

#index()

# sentence = "hello, world !"
# position = sentence.index("world")
# print("the world 'world' is found at position: ",position)

#isalnum() 

# alphanumeric_string = "abc123"
# print(alphanumeric_string.isalnum())

# non_alphanumeric_string = "abc123@"
# print(non_alphanumeric_string.isalnum())

#isascii()

# ascii_string = "hello"
# print(ascii_string.isascii())
# non_ascii_string = "你好"
# print(non_ascii_string.isascii())

#isdigit()

# numeric_string = "123"
# print(numeric_string.isdigit())

# non_numeric_string = "abc123"
# print(non_numeric_string.isdigit())

#isspace()

# space_string = "  "
# print(space_string.isspace()) #output:true
# non_space_string = "hello"
# print(non_space_string.isspace())

# istitle()

# title = "Hello, Iam Fahis"
# x = title.istitle()
# print(x)

#join()

# seperator = "_"
# words = ["this", "is", "a", "sentence"]
# joined_string = seperator.join(words)
# print(joined_string)

#split()

# text= "apple,banana,orange"
# fruit_list = text.split(",")
# print(fruit_list)

#maxsplit()

text = "apple,banana,orange"
fruit_list = text.split(",",maxsplit=1)
print(fruit_list)