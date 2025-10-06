def solution(expressions):
    answer = []
    
    min_digit = 2
    for exp in expressions:
        for char in exp:
            if char.isdigit():
                min_digit = max(min_digit, int(char) + 1)
    
    n = list(range(min_digit, 10))
    
    for exp in expressions:
        a, operator, b, eq, c = exp.split()
        if 'X' not in (a,b,c):
            n = decision(a, operator, b, c, n)
                
    for exp in expressions:
        a, operator, b, eq, c = exp.split()
        
        if c == 'X':
            results = []
            for nn in n:
                a10 = convert_to_ten(nn,a)
                b10 = convert_to_ten(nn,b)
                
                if operator == '+':
                    c10 = a10 + b10
                elif operator == '-':
                    c10 = a10 - b10
                
                c_n = convert_to_n(nn, c10)
                if c_n not in results:
                    results.append(c_n)
            
            if len(results) == 1:
                c = results[0]
            else:
                c = '?'
            
            answer.append(f"{a} {operator} {b} = {c}")
    
    return answer

def decision(a, operator, b, c, n_list):
    valid_n = []
    for n in n_list:
        a10 = convert_to_ten(n, a)
        b10 = convert_to_ten(n, b)
        c10 = convert_to_ten(n, c)
        if operator == '+':
            if a10 + b10 == c10:
                valid_n.append(n)
        elif operator == '-':
            if a10 - b10 == c10:
                valid_n.append(n)
    return valid_n

def convert_to_ten(n, number):
    result = 0
    for p in range(1, len(number)+1):
        dig = int(number[-p])
        result = result + dig * (n ** (p-1))
    return result

def convert_to_n(n, number):
    if number == 0:
        return "0"
    reverseDigit = []
    while number > 0:
        reverseDigit.append(str(number % n))
        number = number//n
    return ''.join(reversed(reverseDigit))