# 6)  დავალება: input() ფუნქციის დახმარებით მომხმარებელს შემოაქვს ორი რიცხვი a და b.  შექმენით ცარიელი სია. for ციკლის და range() ფუნქციის გამოყენებით ახალ სიაში  დაამატეთ ყველა რიცხვი რომელიც a და b რიცხვებს შორისაა ( range(a, b) )
#  .append() ფუნქციის დახმარებით
# შედეგი გამოიტანეთ ტერმინალში

a = int(input("Enter your first  munber: "))
b = int(input("Enter your second munber: "))

my_list = []
for i in range(a + 1, b):
    my_list.append(i)

print("Range of numbers is: " , (my_list)) 
