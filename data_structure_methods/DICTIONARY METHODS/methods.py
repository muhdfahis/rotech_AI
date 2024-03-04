
# clear() = remove the element from the dictionary

# ai_topics = {'machine_learning':'ML','natural_language_processing':'NLP','computer_vision':'CV'}
# ai_topics.clear()
# print(ai_topics)

# copy()= copy the elements

# ai_topics = {'machine_learning':'ML','natural_language_processing':'NLP','computer_vision':'CV'}
# copied_topics = ai_topics.copy()
# print(copied_topics)

# fromkeys(keys,value): creates a new dictionary with specified keys and a default value

# topics = ['machine_learning','natural_language_processing','comoputer_vision']
# default_value = 'rotech'
# ai_dict = dict.fromkeys(topics,default_value)
# print(ai_dict)

# get() = to get a specific value using the keyname

# ai_topics = {'machine_learning':'ML','natural_language_processing':'NLP','computer_vision':'CV'}
# ml_value = ai_topics.get('machine_learning','not_found')
# print(ml_value)

# items() = returns a list containing a tuple for each key value pair

# ai_dict = {'algorithm':'a set of instruction to perform a task','neutral_network':'a model inspired by the human brain'}
# item_list = ai_dict.items()
# print(item_list)

# keys() = return the list of key values

# ai_dict = {'algorithm':'a set of instruction to perform a task','neutral_network':'a model inspired by the human brain'}
# keys_list = ai_dict.keys()
# print(keys_list)

# pop() = removes the specific element using key word

# ai_dict = {'algorithm':'a set of instruction to perform a task','neutral_network':'a model inspired by the human brain'}
# ai_dict.pop('algorithm')
# print(ai_dict)

# popitem() = removes the last added 

# ai_dict = {'algorithm':'a set of instruction to perform a task','neutral_network':'a model inspired by the human brain'}
# ai_dict.popitem()
# print(ai_dict)

# the setdefault()= method in python dictionaries is used to get the value of a specified key.if the key is already present in the
#                  dictionary, it return the corresponding

# student_scores = {'alice':85,'bob':90,'charlie':78}

# alice_score = student_scores.setdefault('alice',0)
# print(f"alice' s score:{alice_score}")

# david_score = student_scores.setdefault('david',0)
# print(f"david's score: {david_score}")

# print('modified dictionary:',student_scores)

#  update() = update dictionary to another dictionary

# student_scores = {'alice':85,'bob':90,'charlie':78}
# additional_scores = {student_scores = {'alice':85,'bob':90,'charlie':78}}

# student_scores.update(additional_scores)

# print(student_scores)

student_scores = {'alice':85,'bob':90,'charlie':98}
score_list = student_scores.values()

print (f"all scored:{score_list}")
