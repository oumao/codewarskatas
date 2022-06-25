from stack import Stack 

string = "gninraeL nIdekniL tol a nraeL"
reversed_string = ""
stack = Stack() 
for ch in string:
    stack.push(ch)

while not stack.is_empty():
    reversed_string += stack.pop()

print(reversed_string)