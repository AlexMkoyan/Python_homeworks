def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'The expression must contain at least one sign ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except ValueError:
                raise ValueError('Expression must contain 2 integers and 1 sign')
            except ZeroDivisionError:
                raise ZeroDivisionError('Division by zero is not allowed')


if __name__ == '__main__':
    print(calculator('4+4'))
