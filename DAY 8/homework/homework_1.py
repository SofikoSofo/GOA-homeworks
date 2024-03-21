# დავალება 1:   მომხმარებელს შემოატანინეთ თავისი ნიშნები , შემდეგ კი გამოითვალეთ ამ ნიშნების საშუალო არითმეტიკული

match = int(input("Enter your result in mathematics:  "))
georgian_lg = int(input("Enter your result in native language:  "))
eng_lg = int(input("Enter your result in English language:  "))
result = ((match + georgian_lg + eng_lg )//3)

print("Your result is: " + str(result))
