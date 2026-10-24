def left_shift(binary, positions):
    print("\nOriginal Binary Number:", binary)
    result = binary

    for i in range(positions):
        result = result[1:] + '0'
        print("After left shift", i + 1, ":", result)

    print("Final Result:", result)


def right_shift(binary, positions):
    print("\nOriginal Binary Number:", binary)
    result = binary

    for i in range(positions):
        result = '0' + result[:-1]
        print("After right shift", i + 1, ":", result)

    print("Final Result:", result)


print("LOGICAL LEFT SHIFT")
left_shift("10110110", 2)

print("\nLOGICAL RIGHT SHIFT")
right_shift("11010100", 2)