# 3) დავალება: მომხმარებელს შემოატანიეთ რიცხვი და for loop-ის დახმარებით დაპრინტეთ რიცხვები 1-დან  მომხმარებლის მიერ შემოტანილი რიცხვის ჩათვლით.
# ტერმინალში გამოიტანეთ ამ რიცხვების ჯამი და საშუალო არითმეტიკული




x = int(input("Enter your namber: "))
sum = 0
for i in  range( 1, x + 1):
    sum = sum + i
    sash = sum // i


print("Sum of numbers is: " , (sum)) 
print("Arithmetic average is:" , (sash))



