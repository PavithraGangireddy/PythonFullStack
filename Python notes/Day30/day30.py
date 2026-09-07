 #1.
import re
email = "student@gmail.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

#2.
import re
text = "I have 2 books and 5 pens."
result = re.findall(r"\d+", text)
print(result)

#3.
import re
text = "Python is difficult"
result = re.sub("difficult", "easy", text)
print(result)

#4.
import re
text = "I am learning Python"
result = re.search("Python", text)
if result:
    print("Pattern found")
else:
    print("Pattern not found")

#5.
import re
text = "Python is easy and Python is powerful"
result = re.finditer("Python", text)
for match in result:
    print(match.group(), match.start())

#6.
import re
text = "Apple,Banana,Orange"
result = re.split(",", text)
print(result)

#7.
import re
text = "Python JAVA SQL"
print(re.findall(r"[A-Z]", text))

#8.
import re
text = "Room 25"
print(re.findall(r"[0-9]", text))

#9.
import re
text = "Python is easy"
if re.search(r"^Python", text):
    print("Starts with Python")