print("Welcome to Lam's Calculator Program.")
print("This program will calculate the sum X of X1 and X2")

print("Please enter X1:")
X1 = float(input("X1 = "))

print("Please enter X2:")
X2 = float(input("X2 = "))

print("Caution: NEVER FIND X. However, X1 + X2 =" , X1 + X2 + 1)

def vOzer_check_def() :
    vOzer_check = str(input("Do you agree? Enter Y/N: "))
    while vOzer_check not in ["Y" , "N" , "y" , "n"] :
        vOzer_check = str(input("I said Y/N, are you stupid or something? Just enter Y or N: "))
    if vOzer_check in ["Y" , "y"] :
        print("LOL. You're really a vOzer. The right answer is:" , X1 + X2)
    elif vOzer_check in ["N" , "n"] :
        print("Hah. So you're not a true vOzer. The right answer is:" , X1 + X2)

vOzer_check_def()