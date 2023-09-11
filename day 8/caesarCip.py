alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

flag=True

while flag:
    direction = input("To Encrypt Type 'encode' and to Decrypt Type 'decode':").lower()
    if direction=='encode' or direction=='decode':
        text=input("Type your message:").lower()
        shift=int(input("type the shift number:"))
        print("\n")
    else:
        print("Wrong Command\n")

    def cypher(text,shift,choice):
        if choice=='encode':
            encrypt_txt=""
            for char in text:
                if char in alphabet:
                    char_index=alphabet.index(char)
                    shifted_txt_index=(char_index+shift)%26
                    encrypt_char=alphabet[shifted_txt_index]
                    encrypt_txt+=encrypt_char
                else:
                    encrypt_txt+=char
            print(f"Encrypted Message:{encrypt_txt}\n\n")
        elif choice=='decode':

            decrypt_txt=""
            for char in text:
                char_index=alphabet.index(char)
                shifted_txt_index=(char_index-shift)%26
                decrypt_char=alphabet[shifted_txt_index]
                decrypt_txt+=decrypt_char
            print(f"Decrypted Message:{decrypt_txt}\n")  
    

    cypher(text,shift,direction)
    choice=input("Do you want to Repeat this process [Y,N]:").lower()
    
    if choice=="y":
        flag=True
    else:
        print("\nExit")
        print("*****Caesar Cipher****")
        flag=False
