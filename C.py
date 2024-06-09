def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    bits.reverse()
    return ''.join(bits)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    a = int(data[0])
    b = int(data[1])
    
    product = a * b
    binary_result = decimal_to_binary(product)
    
    print(binary_result)


main()
