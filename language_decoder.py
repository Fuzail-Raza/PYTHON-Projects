
# !!! Rules !!! :
#     To Encrypt:
#       --- if message lenght is greater than 2 then pop first letter and append it at last and  add three random characters at first and three at last 
#       --- if lenght is less than 3 then reverse it
#     To Decrypt:
#        --- if message lenght is greater than 2 then remove three characters at first and three at last and  pop last letter and append it at first
#        --- if lenght is less than 3 then reverse it



def encrypt_message(message):
    '''To Encrypt:
      --- if message lenght is greater than 2 then pop first letter and append it at last and  add three random characters at first and three at last 
      --- if lenght is less than 3 then reverse it'''
    if(message=="quit"):
        exit()
    try:
        if len(message) >= 3:
            rotated_message = message[1:] + message[0]
            encrypted_message = f"abc{rotated_message}xyz"
            return encrypted_message.strip()
        else:
            return (''.join(reversed(message))).strip()
            # return message[::-1].strip()

    except Exception as e :
        print(e) 


def decrypt_message(message):
    '''To Decrypt:
       --- if message lenght is greater than 2 then remove three characters at first and three at last and  pop last letter and append it at first
       --- if lenght is less than 3 then reverse it'''
    try:
        if len(message) >= 3:
            message = message[3:-3]
            last_char = message[-1]
            message = last_char + message[:-1]
            return message.strip()
        else:
            return message[::-1].strip()
    except Exception as e :
        print(e) 


while True:

    message=input("Enter Your Secret Message : ")
    encrypt=""
    msg=message.split(" ")
    for i in msg:
        encrypt+=encrypt_message(i)+" "

    print("Your Encrypted Message is : ",encrypt)
    encrypt=encrypt.split(" ")
    decrypt=""
    for i in encrypt:
        decrypt+=decrypt_message(i)+" "
    print("Your Decrypted Message is : ",decrypt)