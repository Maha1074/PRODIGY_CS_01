def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt', or 'exit' to quit): ").lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid option. Please choose 'encrypt' or 'decrypt'.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        encrypted_decrypted_message = caesar_cipher(message, shift, mode)
        print(f"The resulting message is: {encrypted_decrypted_message}")

if __name__ == "__main__":
    main()
