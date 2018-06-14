print("Welcome to Lam's Calculator Program.")
print("This program will calculate the sum X of X1 and X2")

counter = 1

while True:
    try:
        if counter == 1:
            X1 = float(input("Please enter number X1: "))
        else:
            X1 = float(input("Now enter number X1 once again: "))
    except ValueError:
        print("I said NUMBER, you fucking understand? ", end="")
        counter += 1
        continue
    else:
        break

while True:
    try:
        if counter == 1:
            X2 = float(input("Please enter number X2: "))
        else:
            X2 = float(input("Now use your brain and enter number X2: "))
    except ValueError:
        print("I said NUMBER, you dumb fuck. ", end="")
        counter += 1
        continue
    else:
        break

X = float(X1) + X2

print("Caution: DANGER!!!")
print("Remember: NEVER FIND X.")
print("However, %s + %s = %s" % (X1 , X2 , X + 1))

def vOzer_check_def() :
    vOzer_check = str(input("Do you agree? Enter Y/N: "))
    while vOzer_check not in ["Y" , "N" , "y" , "n"] :
        vOzer_check = str(input("I said Y/N, are you stupid or something? Just enter Y or N: "))
    if vOzer_check in ["Y" , "y"] :
        print("LOL. You're really a vOzer. The right answer is: %s + %s = %s" % (X1 , X2 , X))
    elif vOzer_check in ["N" , "n"] :
        print("Hah. So you're not a true vOzer. Yes, the right answer is: %s + %s = %s" % (X1 , X2 , X))

vOzer_check_def()
