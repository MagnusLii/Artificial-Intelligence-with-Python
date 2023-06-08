
sentence = "This is a sentence"



def my_split(sentence, separator):
    list = []
    string = ""
    for elem in sentence:
        if elem != separator:
            string += elem
        else:
            list.append(string)
            string = ""
    list.append(string)

 #   print(f"list:   {list}")
    return list


def my_join(sentence, joiner):
    parsed_sentence = ""
    for i in sentence:
        parsed_sentence += i + joiner
    

 #   print(f"parsed sent :   {parsed_sentence}")
    return parsed_sentence[:-1]

print(my_join(my_split(sentence, ' '), ','))
print(my_split(my_join(sentence, ' '), ','))