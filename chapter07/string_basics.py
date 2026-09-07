
first = "Hello"
second = "Python"

print(first + second)
print(first + " " + second)
print("Python! " * 3)
print("-" * 20)

# 문자열 + 문자열 -> 연결
# 문자열 * 정수 -> 반복

word = "python"
print(word[5])
print(word[2:6])

email = "student@example.com"
print(email[0])
print(len(email)-1)
print(email[18])

text = "Python"
print(text.upper())

text = "PYTHON"
print(text.lower())

name = "    우동현   "
print(name.strip())

message = "I like Java"
new_message = message.replace("Java","Python")
print(message)
print(new_message)

text = "banana"
print(text.find("na"))
print(text.count("a"))