username = input("input user : ")
password = input('input password : ')

if username == "member" and password == "1234":
    print("login success")
    service = input("input number service(1-2)")
    if service == "1":
        print("wirdess")
    elif service == "2":
        print("deposit")
    else:
        print("number not found")
else:
    print("account not found")
