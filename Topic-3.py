print("Welcome to Lâm's Calculator Program.")
print("This program will calculate the sum X of X1 and X2")

print("Please enter number X1: ", end="")
while True:
    try:
        X1 = float(input(""))
    except ValueError:
        print("I said NUMBER, you fucking understand? Now enter number X1 once again: ", end="")
        continue
    else:
        break

print("Please enter number X2: ", end="")
while True:
    try:
        X2 = float(input(""))
    except ValueError:
        print("I said NUMBER, you dumb fuck. Now use your brain and enter number X2: ", end="")
        continue
    else:
        break

X = X1 + X2

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
