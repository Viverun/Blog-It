#Personalized greeting generator
#Ask user for their name
name = input("Enter your name: ")
#Choose a personalized message 
greeting = input("Choose a personalized message: e.g. Hello, Hi, Good Day: ")
personalized_message = (f"{greeting}, {name}!")
#Display the personalized message
print(personalized_message)
print(f"{name}, How are you?")
print(f"{name} say hello")