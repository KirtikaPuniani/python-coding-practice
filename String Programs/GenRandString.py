#Generate random string until a given string is generated
#I/P: hello
#O/P: it will generate random strings until the string "hello" is generated.


#Genetic Algorithm
import string
import random
char = string.ascii_letters + string.digits + '.,!?;:'
target = 'Heyo'
string = ''.join(random.choice(char) for _ in range(len(target)))
iterations = 0
while string != target:
    print(string)
    
    i = random.randint(0, len(string) - 1)
    l = list(string)
    l[i] = random.choice(char)
    string1 = ''.join(l)
    
    if sum(a == b for a, b in zip(string1, target)) > sum(a == b for a, b in zip(string, target)):
        string = string1
        
    iterations += 1
    
print(string)
print(f"Target matched after {iterations} iterations")






