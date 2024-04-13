#  დავალება: შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს, იქამდე უნდა შეეკითხოს სანამ პაროლი სწორი არ იქნება.

password = "hello"
user = input("Enter your password: ")
while user != password:
    user = input("The password is incorrect. Please try again: ")

print("Welcome")