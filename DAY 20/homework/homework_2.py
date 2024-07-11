#   დავალება:  1)   for loop-ის გამოყენებით დაპრინტეთ 5-ის და 3-ის ჯერადი რიცხვები 1-დან 100-ის ჩათვლით

for i in range (1,101):
    if i % 3==0 and i % 5==0:
        print(i)

#   დავალება:  2)  შექმენით ცარიელი სია. მომხმარებელს შეეკითხეთ სახელი და გვარი, რომელსაც დაამატებთ თქვენ მიერ შექმნილ სიაში. საბოლო შედეგი გამოიტანეთ ტერმინალში

list = []
name=(input("Enter your name: "))
surname=(input("Enter your surname: "))

list.append(name)
list.append(surname)
print(list)
