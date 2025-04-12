try:
    f = open('text.txt', 'r')
    if f.name == 'text.txt':
        raise Exception

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Are you Serious?")
finally:
    print("Executing finally")