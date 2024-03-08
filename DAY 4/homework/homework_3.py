# davaleba:  დახაზეთ 3 სახლი, ეზოთი, მზე და ვარსკვლავები ( რაც უფრო მეტს იშრომებთ, უფრო დაგიფასდებათ )

from turtle import*

# grass
bgcolor("green")


# sky
penup()
goto(-800, 0)
pendown()
color("aqua")
begin_fill()
forward(1600)
left(90)
forward(500)
left(90)
forward(1600)
left(90)
forward(500)
left(90)
end_fill()

# sun
penup()
goto(-320, 290)
pendown()
color("yellow")
begin_fill()
circle(25)
end_fill()

# star
penup()
goto(-120, 300)
pendown()
color("yellow")
begin_fill()
circle(5)
end_fill()

penup()
goto(-220, 280)
pendown()
color("yellow")
begin_fill()
circle(5)
end_fill()

penup()
goto(-50, 180)
pendown()
color("yellow")
begin_fill()
circle(5)
end_fill()


# end star





#paimt a house

#step 1 - draw a square
width(7)
begin_fill()
color("CadetBlue")
penup()
goto(0, 0)
pendown()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

color("CadetBlue")
end_fill()
#end square

#step 2- drowing a door
forward(70)
color("DarkSeaGreen")
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

color("DarkOrange")
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

color("Ivory")
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

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#paimt a house

#step 1 - draw a square
width(7)

color("LemonChiffon")
penup()
begin_fill()
goto(200, 0)
pendown()
right(150)

right(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
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
goto(400,200)
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
goto(210,130)
pendown()

color("blue")
begin_fill()
goto(260,130)
goto(260,160)
goto(210,160)
goto(210,130)
end_fill()
#end window 1

#window 2
penup()

begin_fill()
goto(340,130)
pendown()

goto(390,130)
goto(390,160)
goto(340,160)
goto(340,130)
end_fill()
#end window 2

#sakvamuri
penup()
begin_fill()
goto(390,220)
pendown()
goto(390,270)
goto(370,270)
goto(370,250)
goto(390,220)
end_fill()

exitonclick()

