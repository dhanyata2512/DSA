from StackDS import Stack
opened=['[','{','<','(']
closed=[']','}','>',')']

def expression_checker(exp):
    stack=Stack(10)
    for character in exp:
        if character in opened:
            stack.push(character)
        elif character in closed:
            new=stack.pop()
            if  closed.index(character) != opened.index(new):
                return 'Unbalanced'
    if stack.is_empty():
        return "Balanced"
    else:
        return "Unbalanced"
    

print(expression_checker("[w+d(r-m{a+f}+d)]")) 
print(expression_checker("{d+r<r-i[f-r}"))   
                 