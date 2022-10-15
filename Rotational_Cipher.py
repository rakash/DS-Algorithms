## 3.1 - Rotational Cipher

def rotationalCipher(strings, factor):
    out = ''
    
    for c in strings:
        if c.isnumeric():
            out += str((int(c) + factor) % 10)
        elif c.isupper():
            t = (ord(c) - ord('A') + factor) % 26
            out += chr(ord('A') + t)
        elif c.islower():
            t = (ord(c) - ord('a') + factor) % 26
            out += chr(ord('a') + t)
        else:
            out += c
    return out

input_1 = "All-convoYs-9-be:Alert1."
rotation_factor_1 = 4
expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
print(rotationalCipher(input_1, 4))

input_2 = "abcdZXYzxy-999.@"
rotation_factor_2 = 200
expected_2 = "stuvRPQrpq-999.@"
print(rotationalCipher(input_2, 200))