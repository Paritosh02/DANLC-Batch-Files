import numpy as np
import matplotlib.pyplot as plt

segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

plt.figure(figsize=(7, 7))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'skyblue', 'lime', 'tan'])
plt.title("Distribution of Company Revenue by Business Segment")
plt.show()