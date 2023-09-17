import art

def caesar_cipher(text, shift, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            if direction == 'encode':
                shifted_char_index = (char_index + shift) % 26
            else:
                shifted_char_index = (char_index - shift) % 26
            result += alphabet[shifted_char_index]
        else:
            result += char
    
    return result

def main():
    print(art.logo)
    
    while True:
        direction = input("To Encrypt, type 'encode'. To Decrypt, type 'decode': ").lower()
        
        if direction not in ['encode', 'decode']:
            print("Invalid command. Please enter 'encode' or 'decode'.")
            continue
        
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        
        encrypted_text = caesar_cipher(text, shift, direction)
        print(f"{direction.capitalize()}d Message: {encrypted_text}\n")
        
        repeat = input("Do you want to repeat this process? (Y/N): ").lower()
        if repeat != 'y':
            print(art.exit)
            break

if __name__ == "__main__":
    main()