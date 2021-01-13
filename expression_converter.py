from definitions import OPERATORS, OPERATOR_PREC_1, OPERATOR_PREC_2, OPERATOR_PREC_3

def expression_converter():
    postfix = []
    stack = ["#"]
    
    while(True):
        user_input = input("write a expression : ")
        user_input = user_input.replace(" ", "")

        repeat_trigger = False
        for input_char in user_input:
            if input_char.isdecimal():
                postfix += input_char
            elif input_char == "(":
                stack.append(input_char)
            elif input_char == ")":
                while(stack[-1] != "("):
                    postfix += stack.pop()
                stack.pop() #Remove '('
            elif input_char in OPERATORS:
                if stack[-1] not in OPERATORS:
                    stack.append(input_char)
                elif operator_comparator(input_char, stack[-1]):
                    stack.append(input_char)
                else:
                    while stack[-1] in OPERATORS and stack[-1] != "#" and not operator_comparator(input_char, stack[-1]):
                        postfix += stack.pop()
                    stack.append(input_char)
            else:
                repeat_trigger = True
                break

        if repeat_trigger:
            print("Type correct expression form!(We don't take unknown values.)")
            postfix.clear()
            stack = ["#"]
            continue
        else: break
        
    while stack[-1] != "#":
        postfix += stack.pop()

    return postfix

def operator_precedence(operator):
    if operator in OPERATOR_PREC_1:
        return 1
    if operator in OPERATOR_PREC_2:
        return 2
    if operator in OPERATOR_PREC_3:
        return 3

def operator_comparator(operator1, operator2):
    return operator_precedence(operator1) > operator_precedence(operator2)