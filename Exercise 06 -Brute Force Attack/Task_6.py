the_correct_password=12345
attempts=0

while attempts<5:
    password=int(input("enter the passsword"))
    
    if password== the_correct_password:
        print("the password you entered is correct")
    else:
        attempt+=1#the amount of attempt will keep on increasing 
        attempts_left=-5- attempts#will show the numbert of attempts left
        print("Access denied!,Try again.You have" ,attempts_left,"attempts remaining")

if attempts==5:
    print("you ran out of attempts")        
            