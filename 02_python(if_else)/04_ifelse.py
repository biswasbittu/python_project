correct_username="bittu98";
correct_password="1234";


input_username=input("Enter your user Name:");
input_password=input("Enter your Password: ");

if input_username == correct_username and input_password == correct_password:
    print("succefully log in")
    
else:
    print("Failed to log in")