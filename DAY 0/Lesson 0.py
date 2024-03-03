from turtle import*
print("gamarjoba me var sofo, es chemi pirveli davalebaa")

#paimt a house

#step 1 - draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end square

#step 2- drowing a door
forward(70)
color("yellow")
begin_fill()
forward(60)
left(90)
forward(120)
left(90)
forward(60)
left(90)
forward(120)
left(90)
end_fill()
#end door

#step 3 - drowing a roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#end roof

#step 4 - drowing s window
# window 1
penup()
goto(10,130)
pendown()

color("blue")
begin_fill()
goto(60,130)
goto(60,160)
goto(10,160)
goto(10,130)
end_fill()
#end window 1

#window 2
penup()

begin_fill()
goto(140,130)
pendown()

goto(190,130)
goto(190,160)
goto(140,160)
goto(140,130)
end_fill()
#end window 2

#sakvamuri
penup()
begin_fill()
goto(190,220)
pendown()
goto(190,270)
goto(170,270)
goto(170,250)
goto(190,220)
end_fill()


exitonclick()

