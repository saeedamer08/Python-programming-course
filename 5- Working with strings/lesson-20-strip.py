s = "Python course is now available"
secret = str.maketrans('abcABC', 'ABCabc')
y = str.upper(s)


print(s.translate(secret))
print("------")
print(s)
print(y)
