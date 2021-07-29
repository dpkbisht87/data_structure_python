def eval_posfix(s):
    operators =['+', '-', '*', '/']
    stack = []
    i = 0
    # while len(s) > 0:
    for cur in s:
        if cur in operators:
            val2 = stack.pop()
            val1 = stack.pop()
            result = evaluate(int(val1), int(val2), cur)
            stack.append(result)
        else:
            stack.append(cur)
        i += 1
    return stack.pop()


def evaluate(val1, val2, cur):

    if cur =='+':
        return val1 + val2
    if cur =='-':
        return val1 - val2
    if cur =='*':
        return val1 * val2
    if cur =='/':
        return val1 / val2


if __name__ =='__main__':
    s='53+82-*'
    print(eval_posfix(s))