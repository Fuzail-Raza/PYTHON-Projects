
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
        msg=message.split(" ")
        message=""
        for i in msg:
            if len(i) >= 3:
                rotated_message = i[1:] + i[0]
                encrypted_message = f"abc{rotated_message}xyz"
                message+= encrypted_message.strip()+" "
            else:
                message+= (''.join(reversed(i))).strip()+" "
                # return message[::-1].strip()
        return message
    except Exception as e :
        print(e) 


def decrypt_message(message):
    '''To Decrypt:
       --- if message lenght is greater than 2 then remove three characters at first and three at last and  pop last letter and append it at first
       --- if lenght is less than 3 then reverse it'''
    try:
        msg=message.split(" ")
        message=""
        for i in msg:
            if len(i) >= 3:
                i = i[3:-3]
                i = i[-1] + i[:-1]
                message += i.strip()+ " "
            else:
                message+= i[::-1].strip()+ " "
        return message
    except Exception as e :
        print(e) 


while True:

    message=input("Enter Your Secret Message : ")

    encrypt=encrypt_message(message)
    print("Your Encrypted Message is : ",encrypt)
   
    print("Your Decrypted Message is : ",decrypt_message(encrypt))