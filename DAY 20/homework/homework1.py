

# 1 დაპრინტეთ მხოლოდ ლუწი რიცხვები


my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in my_list:
    if i % 2 == 0:
        print(i)


# 2 დაპრინტეთ 5ის ჯერადი რიცხვები

my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in my_list:
    if i % 5 == 0:
        print(i)

# 3 დაპრინტეთ რიცხვთა ჯამი

my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sum = 0

for i in my_list:
    sum = sum + i
print(sum)

# 4 დაპრინტეთ ლუწ რიცხვთა ჯამი

my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sum = 0

for i in my_list:
    if i % 2 == 0:
        sum = sum + i
print(sum)


# 5 დაპრინტეთ ახალი სია რომელშიც იქნება მხოლოდ კენტი რიცხვები

my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_list = []
 
for i in my_list:
    if i % 2 == 1:
        new_list.append((i))

print(new_list)

# 6 დაპრინტეთ ახალი სია რომელშიც იქნება 3ის და 5ის ჯერადი რიცხვები 

my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
new_list = []
 
for i in my_list:
    if i % 5 == 0 and i % 3 == 0 and i > 0:
         new_list.append((i))

print(new_list)