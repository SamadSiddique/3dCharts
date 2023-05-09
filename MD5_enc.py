# Grammar rules
grammar = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'id']
}

# Parsing table
parsing_table = {
    0: {'(': 4, 'id': 5},
    1: {'+': 6, '$': 'accept'},
    2: {'+': 7, '*': 8, ')': 7, '$': 7},
    3: {'+': 10, '*': 10, ')': 10, '$': 10},
    4: {'(': 4, 'id': 5},
    5: {'+': 6, '*': 9, ')': 6, '$': 6},
    6: {'(': 4, 'id': 5},
    7: {'(': 4, 'id': 5},
    8: {'(': 4, 'id': 5},
    9: {'(': 4, 'id': 5},
    10: {'(': 4, 'id': 5}
}

# SLR parser function
def slr_parser(string):
    stack = [0]
    input_str = string.split()
    input_str.append('$')
    i = 0
    while True:
        state = stack[-1]
        symbol = input_str[i]
        if symbol not in parsing_table[state]:
            return "Error: Invalid symbol"
        action = parsing_table[state][symbol]
        if action == 'accept':
            return "Input string is valid"
        elif isinstance(action, int):
            stack.append(symbol)
            stack.append(action)
            i += 1
        else:
            prod = grammar[action][0]
            num_symbols = len(prod.split()) - 1
            for _ in range(2 * num_symbols):
                stack.pop()
            state = stack[-1]
            stack.append(action)
            stack.append(parsing_table[state][action])
        print(stack)

# Test the parser
string = "id + id * id"
slr_parser(string)
