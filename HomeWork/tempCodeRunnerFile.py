
name = input("Give me your name: ")
age = input("Give me your age: ")
cuntry = input("Give me your cuntry: ")
print("Your name is..: " + name)
print("your age is..: " + age)
print("your cuntry is..: " + cuntry)
print('Hello ' + name)


def users(name):
    names = 'hello, {}' .format(name)
    return names

print(users('khaled'))
