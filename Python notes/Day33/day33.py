#1Line chart
import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
temperature = [30, 32, 31, 35, 34]
plt.plot(days, temperature)
plt.title("Temperature for 5 Days")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

#2.Bar chart
import matplotlib.pyplot as plt
x = ["A", "B", "C", "D"]
y = [20, 35, 25, 40]
plt.bar(x, y)
plt.title("Student Marks")
plt.show()

#3. scatter plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [20, 30, 25, 40, 35]
plt.scatter(x, y)
plt.title("Data Analysis")
plt.show()

#4.Histogram
import matplotlib.pyplot as plt
marks = [20, 30, 40, 50, 65, 70, 75, 80]
plt.hist(marks, bins=4)
plt.title("Marks Distribution")
plt.show()

#5.pie chart
import matplotlib.pyplot as plt
data = [40, 30, 20, 10]
labels = ["Python", "Java", "SQL", "HTML"]
plt.pie(data, labels=labels, autopct="%1.1f%%")
plt.title("Skills")
plt.show()
