def isBalanced(expression):
    if len(expression) % 2 != 0:
        return "NO"

    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    mapping = {opening[0]:closing[0],
               opening[1]:closing[1],
               opening[2]:closing[2]}

    if expression[0] in closing:
        return "NO"

    if expression[-1] in opening:
        return 'NO'

    closing_queue = []
    for letter in expression:
        if letter in opening:
            closing_queue.append(mapping[letter])
        elif letter in closing:
            if not closing_queue:
                return 'NO'

            if closing_queue[-1] == letter:
                closing_queue.pop()
                
            else:
                return 'NO'

    return 'YES'


if __name__ == "__main__":

    expr = '{{}}[][()]([])}'
    if isBalanced(expr) : print('YES')
    if not isBalanced(expr) : print('NO')
