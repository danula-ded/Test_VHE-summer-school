def evaluate_rpn(expression):
    # Разбиваем строку на токены
    tokens = expression.split()
    
    # Инициализируем стек
    stack = []
    
    # Проходим по всем токенам
    for token in tokens:
        if token.isdigit():  # Если токен - число
            stack.append(int(token))
        else:  # Если токен - оператор
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # Используем целочисленное деление, как указано в задаче
                stack.append(a // b)
    
    # Результат будет единственным элементом в стеке
    return stack[0]

def main():
    import sys
    input = sys.stdin.read
    expression = input().strip()
    result = evaluate_rpn(expression)
    print(result)

if __name__ == "__main__":
    main()
