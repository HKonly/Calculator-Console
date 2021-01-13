from definitions import OPERATORS

def calculator(post_ex):
    copy_ex = [] + post_ex
    while(len(copy_ex) > 1):
        i = 0
        while(i < len(copy_ex)):
            if(copy_ex[i] in OPERATORS):
                copy_ex[i-2] = calculate(copy_ex[i-2], copy_ex[i-1], copy_ex[i])
                copy_ex.pop(i)
                copy_ex.pop(i-1)
                i -= 2
            i += 1
    return float(copy_ex[0])

def calculate(operand1, operand2, operator):
    if(operator == '+') : return float(operand1) + float(operand2)
    if(operator == '-') : return float(operand1) - float(operand2)
    if(operator == '*') : return float(operand1) * float(operand2)
    if(operator == '^') : return float(operand1) ^ float(operand2)
    if(operator == '/') : return float(operand1) / float(operand2)