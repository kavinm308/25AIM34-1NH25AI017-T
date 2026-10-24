def to_8bit_binary(n):
    return format(n & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def binary_addition(a, b):
    bin_a = to_8bit_binary(a)
    bin_b = to_8bit_binary(b)

    result = (int(bin_a, 2) + int(bin_b, 2)) & 0xFF
    result_binary = format(result, '08b')
    result_decimal = signed_value(result_binary)

    overflow = (a >= 0 and b >= 0 and result_decimal < 0) or \
               (a < 0 and b < 0 and result_decimal >= 0)

    print("\nFirst Operand :", a, "->", bin_a)
    print("Second Operand:", b, "->", bin_b)
    print("Binary Result :", result_binary)
    print("Decimal Result:", result_decimal)
    print("Overflow      :", "Yes" if overflow else "No")


print("8-BIT 2'S COMPLEMENT ADDITION")

print("\nExpression (a): 25 + (+18)")
binary_addition(25, 18)

print("\nExpression (b): (-25) + (-18)")
binary_addition(-25, -18)