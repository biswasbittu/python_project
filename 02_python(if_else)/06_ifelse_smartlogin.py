username="bittu98";
password=123;

input_username=input("Enter Valid Username: ");

if username == input_username:
    print("UserName Correct ");
    input_pwd = int(input("Now Enter Password: "));
    
    if password == input_pwd:
        print("Succefully Loged in")
    else:
        print("wrong Password")
else:
    print("Wrong username ")