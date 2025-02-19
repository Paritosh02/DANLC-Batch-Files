import numpy as np
import matplotlib.pyplot as plt
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

plt.figure(figsize=(7, 7))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'skyblue', 'lime', 'tan', 'plum'])
plt.title("Distribution of Montly Income by Source")
plt.show()