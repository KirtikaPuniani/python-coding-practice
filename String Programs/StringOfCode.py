#Execute the string of code
#Given a string containing python code, task is to execute it dynamically
#for eg: I/P: "x = 5\ny = 10\nprint(x + y)"  and   O/P: 15


#Using exec()
#exec() function allows is to execute dynamically generated python code stored in a string
code = "x = 5\ny = 10\nprint(x + y)"
exec(code)