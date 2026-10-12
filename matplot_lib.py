import matplotlib.pyplot as plt
import numpy as np

#line chart
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x,y, color="blue", linestyle="--")
plt.title("Sample Plot")
plt.show()

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x,y, color="red", linestyle="-")
plt.title("Quadratic Plot")
plt.show()

#scatter plot

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x,y, color="green")
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

x = [1.3, 1.5, 1.7, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
y = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
plt.scatter(x,y, color="purple")
plt.title("Population vs GDP")
plt.xlabel("Population (in billions)")
plt.ylabel("GDP (in trillions)")
plt.show()

#bar chart

x = ['A', 'B', 'C', 'D', 'E']
y = [5, 7, 3, 8, 4]
plt.bar(x,y, color="orange")
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

x = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
y = [10, 15, 7, 12]
plt.bar(x,y, color="red")
plt.title("Bar Chart Example 2")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
y = [100, 120, 90, 150, 130]
plt.barh(x,y, color="blue")
plt.title("Horizontal Bar Chart Example")
plt.xlabel("Values")
plt.ylabel("Months")
plt.show()

#pie chart

labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]
plt.pie(sizes, labels=labels, explode=(0.1,0,0,0))
plt.title("Fruit Distribution")
plt.show()

x = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 20, 10]
plt.pie(sizes, labels=x, explode=(0.1,0,0,0))
plt.title("Programming Language Popularity")
plt.show()

#histogram

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=5, color="cyan")
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()  

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.hist(x, bins=5, color="magenta")
plt.title("Histogram Example 2")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

#3d plot

fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
ax.plot3D(x, y, z, 'green')
ax.set_title('3D Line Plot Example')
plt.show()

#subplot

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.subplot(2, 1, 1)
plt.plot(x, y, color="blue", linestyle="--")
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.subplot(2, 1, 2)
plt.plot(x, y, color="red", linestyle="-")
plt.show()

fig = plt.figure()
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.subplot(1, 2, 1)
plt.bar(x, y, color="orange")
labels = ["Python", "Java", "C++", "C"]
sizes = [34,40,23,45]
plt.subplot(1,2,2)
plt.pie(sizes, labels=labels, explode=(0,0,0,0.1))
plt.title("Programming language distribution")
plt.show()
