def encode(plaintext):
    for i in range(len(plaintext)):
        if (plaintext[i] >= 'A' and plaintext[i] <= 'M') or (plaintext[i] >= 'a' and plaintext[i] <= 'm'):
            temp = ord(plaintext[i])
            temp += 13
            plaintext[i] = chr(temp)
        elif (plaintext[i] >='N' and plaintext[i] <= 'Z') or (plaintext[i] >= 'n' and plaintext[i] <= 'z'):
            temp = ord(plaintext[i])
            temp -= 13
            plaintext[i] = chr(temp)
    output = ""
    output = output.join(text)
    return output






while True:
    command = input("Options:\n 1)Alter string\n3)Exit\n")
    if command == '1':
        plaintext = input("Give string to encode or decode:\n")
        text = list(plaintext)
        encodedtext = encode(text)
        print(encodedtext)

    elif command == '3':
        exit()





# void rot13(char s[]){
#     int i;

#     for (i = 0; s[i] != '\0'; i++){
#         if ((s[i] >= 'A' && s[i] <= 'M') || (s[i] >= 'a' && s[i] <= 'm')){
#             s[i] += 13;
#         }
#         else if ((s[i] >='N' &&  s[i] <= 'Z') || (s[i] >= 'n' && s[i] <= 'z')){
#             s[i] -= 13;
#         }

#     }
# }