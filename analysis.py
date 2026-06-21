import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_data.csv")

print("Dataset:")
print(data)

# Average marks
avg = data["Marks"].mean()

print("\nAverage Marks:", avg)

# Highest marks
highest = data["Marks"].max()

print("Highest Marks:", highest)

# Bar Chart
plt.bar(data["Name"], data["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")

plt.xticks(rotation=45)

plt.show()

# Scatter Plot
plt.scatter(data["Attendance"],data["Marks"])

plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")

plt.show()

# Correlation Heatmap

correlation=data[["Marks","Attendance"]].corr()

plt.imshow(correlation)

plt.colorbar()

plt.xticks([0,1],["Marks","Attendance"])
plt.yticks([0,1],["Marks","Attendance"])

plt.title("Heatmap")

plt.show()