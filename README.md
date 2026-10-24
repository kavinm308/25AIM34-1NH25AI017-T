# 25AIM34-1NH25AI017-T
Problem Solving - Group 1 - Kavin AIML 3B


output of q1:
<img width="536" height="573" alt="image" src="https://github.com/user-attachments/assets/16a55717-529a-4f5f-ab9d-3acf70262a5f" />


output of q2:
<img width="535" height="587" alt="image" src="https://github.com/user-attachments/assets/61ca9337-17ce-4f71-b22d-1c10ac33924c" />


# Q1: Manual Verification of 8-bit 2's Complement Addition

## (a) 25 + (+18)

**Step 1: Convert decimal numbers to 8-bit binary.**

25 = 00011001  
18 = 00010010

**Step 2: Perform binary addition.**

```text
   00011001
 + 00010010
 -----------
   00101011
```

**Step 3: Convert the result to decimal.**

00101011 = 32 + 8 + 2 + 1 = 43

**Result:** 00101011 = 43

**Verification:** The manual result matches the Python program output.

**Overflow:** No overflow occurs because 43 is within the 8-bit signed range of -128 to +127.

---

## (b) (-25) + (-18)

**Step 1: Convert the positive numbers to 8-bit binary.**

25 = 00011001  
18 = 00010010

**Step 2: Find the 2's complement of each number.**

For -25:

```text
Binary:          00011001
1's complement:  11100110
Add 1:           11100111
```

For -18:

```text
Binary:          00010010
1's complement:  11101101
Add 1:           11101110
```

**Step 3: Perform binary addition.**

```text
    11100111
  + 11101110
  -----------
  1 11010101
```

Discard the carry beyond 8 bits.

Result = 11010101

**Step 4: Convert the result to decimal.**

Since the most significant bit is 1, the result is negative.

Find its magnitude using 2's complement:

```text
Original:         11010101
Invert the bits:  00101010
Add 1:            00101011
```

00101011 = 43

Therefore, 11010101 represents -43.

**Result:** 11010101 = -43

**Verification:** The manual result matches the Python program output.

**Overflow:** No overflow occurs because -43 is within the 8-bit signed range of -128 to +127.

---

# Q2: Manual Verification of Logical Shift Operations

## (a) Logical Left Shift of 10110110 by 2 Positions

**Step 1: Original 8-bit binary number**

10110110

**Step 2: Shift left by 1 position.**

Discard the leftmost bit and insert 0 at the right.

```text
10110110 → 01101100
```

**Step 3: Shift left by another position.**

```text
01101100 → 11011000
```

**Final Result:** 11011000

**Verification:** The manual result matches the Python program output. The final result contains 8 bits.

---

## (b) Logical Right Shift of 11010100 by 2 Positions

**Step 1: Original 8-bit binary number**

11010100

**Step 2: Shift right by 1 position.**

Discard the rightmost bit and insert 0 at the left.

```text
11010100 → 01101010
```

**Step 3: Shift right by another position.**

```text
01101010 → 00110101
```

**Final Result:** 00110101

**Verification:** The manual result matches the Python program output. The final result contains 8 bits.
