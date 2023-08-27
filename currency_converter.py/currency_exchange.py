

with open("E:\Programms\PYTHON\Projects\currency_converter.py\currencyrates.txt") as f:
    lines=f.readlines()

currency_dict={}
for line in lines:
    currency=line.split("\t")
    currency_dict[currency[0]]=currency[1]

amount=float(input("Enter Amount in PKR"))
to_convert_currenct=input("Enter Currency to COnvert")

print(f"{amount} PKR is equal to : {amount*float(currency_dict[to_convert_currenct])} {to_convert_currenct}")