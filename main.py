def calculate_modulo_exponentiation(A, B, C):
    result = pow(A, B, C)
    return result
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))
output1 = calculate_modulo_exponentiation(A, B, C)
output2 = calculate_modulo_exponentiation(A, B, C)
print("Output 1:", output1)

