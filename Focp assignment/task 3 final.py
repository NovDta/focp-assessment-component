import random

print("Welcome to Pop Chat")
print("One of our operators will be pleased to help you today.")

operators=["Rene","Anna","Edward"]
phrases=["hmmmmmm","Oh","Tell me more","yes, I see","You should try working on this system","Thats interesting","No please"]
end=["help","ok","great","thanks","bye","goodbye","quit","exit"]

email_address=input("Enter your Poppleton email address: ")

def system():
    if email_address.count("@")==1:
        index=email_address.find("@")
        if email_address[index+1:]=="pop.ac.uk" and index>2:
            print(f"Hi,{email_address[:index]}! Thank you, and Welcome to popChat!")
            print(f"My name is {random.choice(operators)}, and it will be my pleasure to help you.")
           
            while True:
                ask=input("What is your Question? ")

                if "library" in ask:
                    print("The library is closed today.")

                elif "WiFi" in ask:
                    print("WiFi is excellent across the campus.")

                elif "deadline" in ask:
                    print("Your deadline has been extended by two working days.")

                elif ask in end:
                    print(f"Thanks, {email_address[:index]}, for using PopChat. See you again soon!")
                    exit()

                else:
                    print(random.choice(phrases))
     
        else:
            print("Invalid")
    else:
        print("Your email_address is invalid.")
        
system()

