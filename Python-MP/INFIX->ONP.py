
def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

# def is_left_associative(operator):
#     return True

def infix_to_onp(expression):
    stack = []
    result = []

    i = 0
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue
        if char.isalnum():  # Check for numbers
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while len(stack)>0 and priority(char) <= priority(stack[-1]) :
                result.append(stack.pop())
            stack.append(char)

        i += 1

    while len(stack) > 0:
        result.append(stack.pop())

    return ''.join(result)


expression1 = "5+(1-3)*4/2"
print(expression1)
print(infix_to_onp(expression1))
