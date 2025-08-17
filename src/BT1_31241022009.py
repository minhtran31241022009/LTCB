# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5,4
print("1) Num one:",num_one, ", Num two:", num_two)
# a)Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print("a) Total = ",total)
# b)Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print("b) Diff = ",diff)
# c)Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print("c) Product = ",product)
# d)Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print("d) Division = ",division)
# e)Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print("e) Remainder = ",remainder) #chia lay du dung %
# f)Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print("f) Exp = ",exp) #lay mu dung **
# g)Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("g) Floor Division = ",floor_division) #chia lay phan nguyen: //
# 2.The radius of a circle is 30 meters.
r = 30
print("2) r = ",r)
import math #nếu muốn dùng pi hay e... phải import trc
# a)Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = (r**2)*math.pi #math.pi là 3.14
print(f"a) Area of circle = {area_of_circle} m\u00b2") #đang là float
print(f"Area of circle (int) = {int(area_of_circle)} m\u00b2") #ép nó qua interger
# b)Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2*math.pi*r
print("b) Circumference of circle = ",circum_of_circle,"meters")
print("Circumference of circle (int) = ",int(circum_of_circle),"meters")
# c)Take radius as user input and calculate the area.
radius = int(input("c) Enter the radius: ")) #nhập số dô xong ép nó qua int
print("Radius of circle = ",radius,"meters")
aoc = (radius**2)*math.pi
print(f"Area of circle = {aoc} m\u00b2") #ghi đơn vị mũ là đv\u00b2
print(f"Area of circle (int) = {int(aoc)} m\u00b2") #sài cái f Hải chỉ
input("Press ENTER to exit") #cái này để lúc input dô nó ko tự out
