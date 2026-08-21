#Execute the string of code
#Given a string containing python code, task is to execute it dynamically
#for eg: I/P: "x = 5\ny = 10\nprint(x + y)"  and   O/P: 15


#Using exec()
#exec() function allows is to execute dynamically generated python code stored in a string
code = "x = 5\ny = 10\nprint(x + y)"      
exec(code)      #executes the string code as python code
#variables x and y are creeated, and their sum is printed


#Using evel
#eval function can execute a single expression stored in a string and return its result. It is more limited compared to exec but can be useful for evaluating expressions.
code = '5+10+16'
result = eval(code)
print(result)