class Solution(object):
    def minimizeXor(self, num1, num2):
        # Count set bits in num2
        set_bits_num2 = bin(num2).count("1")

        # Create x to minimize XOR
        result = 0

        # Step 1: Align leading set bits of num1 with x
        for i in range(31, -1, -1):  # Traverse bits from MSB to LSB
            if set_bits_num2 > 0 and (num1 & (1 << i)):  # If bit is set in num1 and we need set bits
                result |= 1 << i  # Set this bit in result
                set_bits_num2 -= 1  # Decrease required set bits

        # Step 2: Fill remaining set bits (if any) in the lowest positions
        for i in range(32):  # Traverse bits from LSB to MSB
            if set_bits_num2 > 0 and not (result & (1 << i)):  # If bit is not set in result
                result |= 1 << i  # Set this bit in result
                set_bits_num2 -= 1  # Decrease required set bits

        return result
