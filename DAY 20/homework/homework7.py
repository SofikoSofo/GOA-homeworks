# 7) დავალება:  მოცემულია სია my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 15].
#  შექმენით პროგრამა რომელიც ამ სიას შეატრიალებს და შედეგად გამოიტანს შემდეგ სიას: 
# [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# მინიშნება: შექმენით ცარიელი სია.ასევე დაგჭირდებათ for ციკლი, რომლითაც გადაუვლით სიაs და ასევე append() ფუნქცია, რომლითაც ახალ სიაში დაამატებთ my_list-ს ელ;ემენტებს. ასევე დაგჭირდებათ slicing. შედეგი დაპრინტეთ ტერმინალში 

my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 15]
reversed_list = []

reversed_list = my_list[:: -1]

print(reversed_list)



