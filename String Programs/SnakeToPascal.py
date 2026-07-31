#Convert Snake case to Pascal case
#Given a string in snake_case, the task is to convert in into PascalCase here each word dtarts with an upper case and there are no underscores.
#Eg: I/P: hello_everyone_iam_happy and O/P: HelloEveryoneIAmHappy



#Using split and capitalize
string = 'hello_everyone_iam_happy'
result = ''.join(word.capitalize() for word in string.split('_'))   
#split('_') splits the string into individual words at each underscore. Join() joins the list of words without any separator.
print(result)



#Using str.title() and replace()
string = 'hello_everyone_iam_happy'
result = string.replace("_", " ").title().replace(" ", "")
print(result)