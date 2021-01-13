OPERATOR_PREC_1 = ['+', '-']
OPERATOR_PREC_2 = ['*', '/']
OPERATOR_PREC_3 = ['^']

def expression_converter(user_input):
  user_input = user_input.replace(" ", "")
  postfix = []
  stack = []

  try:
    for input_char in user_input:
      if input_char.isdecimal() or input_char.isalpha():
        postfix.append(input_char)
      if (input_char in OPERATOR_PREC_1
          or input_char in OPERATOR_PREC_2
          or input_char in OPERATOR_PREC_3):
        stack.append(input_char)
  except Exception as e:
    print(e)

  return stack

def operator_precedence(operator):
  if operator in OPERATOR_PREC_1:
    return 1
  if operator in OPERATOR_PREC_2:
    return 2
  if operator in OPERATOR_PREC_3:
    return 3