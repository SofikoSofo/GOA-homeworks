#  დავალება_2:    შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ ითვლის ამ რიცხვიდან 1-მდე.



user = input("Enter your number: ")
n = 0
i = int(user)
while i > n:    # პირობა სრულდება მანამდე,  სანამ   იუზერის მიერ შეყვანილი როცხვი 0 - ს არ გაუტოლდება 
    print(i)
    i = i - 1     # ამ ჩანაწერით ხდება იუზერის მიერ შეყვანილი როცხვის კლება ერთი ერთეულით
