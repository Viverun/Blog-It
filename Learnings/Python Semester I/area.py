#Program to calculate area of Geometric figure:
#Ask user to select the figure they want to calculate the area for
ask_figure = input("Please select a geometric figure:(Circle, Rectangle, Square, Triangle...)\n").strip().lower()
if (ask_figure == "circle"):
#To calculate area of Circle
    radius = float(input("Please enter the radius of the Circle: "))
    Area = 3.14159*radius**2
    print("The area of circle is ", Area)
    
elif(ask_figure == "rectangle"):
    length = float(input("Enter the length of the Rectangle: "))
    breadth = float(input("Enter the breadth of the Rectangle: "))
    Area = length*breadth
    print("The area of Rectangle is ", Area)

elif(ask_figure == "triangle"):
    base = float(input("Enter the base of the Triangle: "))
    height = float(input("Enter the height of the Triangle: "))
    Area = height*base*0.5
    print("The area of Triangle is ", Area)

#DIBY