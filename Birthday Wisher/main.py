import pandas as pd
import datetime
import smtplib


def send_mail(to,sub,msg):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("hack.jerry26@gmail.com","etapijvdmncrsfav")
    
    s.sendmail("hack.jerry26@gmail.com",to,f"Subject:{sub}\n\n{msg} ")
    
    print(f"mailsent {to}")
    s.quit()
    

if __name__=='__main__':
    df=pd.read_excel("E:\Programms\PYTHON\Projects\Birthday Wisher\data.xlsx")    
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    print(today)
    for index,item in df.iterrows():
        # print(index,item["Name"])
        bday=item["Birthday"].strftime("%d-%m")
        if(bday==today) and yearNow not in str(item["YEAR"]):
            send_mail(item["mail"],"HAPPY BIRTHDAY",item["Dialogue"])
            df.loc[index,"YEAR"]=str(df.loc[index,"YEAR"])+","+str(yearNow)
        df.to_excel(r"E:\Programms\PYTHON\Projects\Birthday Wisher\data.xlsx",index=False)