from stack import Stack


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "[{(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def reverse_string(input_str):
    s = Stack()
    result = ''
    for i in range(len(input_str)):
        s.push(input_str[i])

    while not s.is_empty():
        result += s.pop()

    return result

def convert_int_to_bin(dec_num):
  s = Stack()
  result = ''
  while dec_num != 0:
    remainder = dec_num % 2
    s.push(remainder)
    dec_num = dec_num // 2

  while not s.is_empty():
      result += str(s.pop())
  return result

# print("String : (((({})))) Balanced or not?")
# print(is_paren_balanced("(((({}))))"))

# print("String : [][]]] Balanced or not?")
# print(is_paren_balanced("[][]]]"))

# print("String : [][] Balanced or not?")
# print(is_paren_balanced("[][]"))

# input_str = "!evitacudE ot emocleW"
# print(reverse_string(input_str))

print(convert_int_to_bin(73))