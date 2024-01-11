import math
class Plasma:

    def __init__(self):
        pass

    def bin_conversion(self, x):
        """
        Converts a decimal integer to binary. 
        """
        bin_number = ""
        bin_check = bin(x)
        
        for i in range(len(bin_check[2:])):
            if x % 2 == 0:
                bin_number = "0" + bin_number
            else:
                bin_number = "1" + bin_number
            
            x = x // 2
        
        return bin_number
    
    def dec_conversion(self, x) -> str:
        """
        Converts a binary number to a decimal number.
        """
        rev_x = x[::-1]
        c = 0

        xl = list(rev_x)
        new_xl = [eval(i) for i in xl]
        z = 0
        dec = 0
        for i in new_xl:
            z = (i * 2**c)
            c += 1
            dec += z
        return dec
    
    def hex_conversion(self, x):
        """
        Converts a binary number to a hexidecimal number.
        """
        dec = self.dec_conversion(x)
        hex_num = ""
        dec_hex = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        while dec > 0:
            rem = dec % 16
            hex_num += dec_hex[rem]
            dec = dec // 16
        hex_num = hex_num[::-1]
        return hex_num

    def hash_128(self, x) -> str:
        """
        Hashes the given string; the digest is 128 bits long.
        """
        salt_arr = {7:"salt", 14: "slat", 21: "salty"}
        if len(x) < 7:
            x += salt_arr[7]
        elif len(x) < 14:
            x += salt_arr[14]
        else:
            x += salt_arr[21]
        hash_val = [19, 34, 26, 90, 45, 78, 39, 89, 178, 20, 12, 210, 160, 145, 50, 233]
        # Determine (the amount of bits the hash is / 2) numbers from 0-255. To make the code more readable, I predetermined the numbers. These numbers determine the digest of a string. 
        ascii_val = [ord(char) for char in x] # Using list comprehension, convert the characters of the string into its number pair in ASCII.
        for i in ascii_val:
            for j in range(len(hash_val)):
                hash_val[j] = math.ceil(math.fmod((hash_val[j] * 50 + i), 251))
                # In these lines of code, for every character in the input, run the formula on every number in the hash_val list. 
        num = ''.join(self.bin_conversion(num) for num in hash_val)
        return self.hex_conversion(num[:128]) # num converts the decimal number we got from hash_val into binary and then converts into hexadecimal, and num[:128] makes sure our digest is exactly 128 bits long.
    
    def hash_64(self, x) -> str:
        """
        Hashes the given string; the digest is 64 bits long.
        """
        salt_arr = {7:"salt", 14: "slat", 21: "salty"}
        if len(x) < 7:
            x += salt_arr[7]
        elif len(x) < 14:
            x += salt_arr[14]
        else:
            x += salt_arr[21]
        # Exact same formula as hash_128 only the numbers were manipulated so it could fit into a 64-bit digest.
        hash_val = [17, 87, 65, 54, 92, 254, 156, 100]
        ascii = [ord(char) for char in x]
        for i in ascii:
            for j in range(len(hash_val)):
                hash_val[j] = math.ceil(math.fmod((hash_val[j] * 25 + i), 126))
        num = ''.join(self.bin_conversion(num) for num in hash_val)
        return self.hex_conversion(num[:64])
