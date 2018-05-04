#!/usr/bin/python3

import matplotlib as mpl
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[6,7,8,9,10]

plt.figure()
plt.scatter(x[:2], y[:2], s=100, c='red', label="Tall Students")
plt.scatter(x[2:], y[2:], s=100, c='blue', label="Short Students")
plt.xlabel('The number of times child kicked a ball')
plt.ylabel('The grade of the student')
plt.title('Relationship between ball kicking and grades')
plt.legend(loc=4, frameon=False, title='legend')
legend=plt.gca().get_children()[-2]

plt.show()

