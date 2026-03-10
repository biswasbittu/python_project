stored_pwd="cyber_secure";
input_pwd=input("Give The currect Password: ");

attempts=1
 
 
if input_pwd == stored_pwd:
    print("Access granted ! you are in system");
else:
    if attempts>=3:
        print("Alert: You have Blocked")
    else:
        print("Wrong password")
    