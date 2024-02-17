def encrypt_string(string, key):
    encrypted_string = ""
    for char in string:
        if char.isalpha():
            shift = ord(key[0]) % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                encrypted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            encrypted_char = char
        encrypted_string += encrypted_char
    return encrypted_string

def decrypt_string(encrypted_string, key):
    decrypted_string = ""
    for char in encrypted_string:
        if char.isalpha():
            shift = ord(key[0]) % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
            else:
                decrypted_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            decrypted_char = char
        decrypted_string += decrypted_char
    return decrypted_string

# Custom key
key = "k"

# Encrypt the string
string_to_encrypt = "I am swikar paudel"
encrypted_string = encrypt_string(string_to_encrypt, key)

# Print the encrypted string and the custom key
print("Encrypted string:", encrypted_string)
print("Custom key:", key)

# Decrypt the string
decrypted_string = decrypt_string(encrypted_string, key)

# Print the decrypted string
print("Decrypted string:", decrypted_string)
