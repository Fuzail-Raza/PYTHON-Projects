
Secure=(("s","$"),("and","$"),("a","@"),("o","0"),("i","1"),("I","|"))

def securePassword(password):
    global Secure
    for a , b in Secure:
        password=password.replace(a,b)
    return password

if __name__=="__main__":
    password=input("Enter Your Password")
    Secure_password=securePassword(password)
    print(Secure_password)
    
    
