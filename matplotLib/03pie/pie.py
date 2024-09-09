from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


plt.pie([40, 20, 30, 10], labels=["Python", "Java", "C++", "Ruby"], colors=["#008fd5", "#fc4f30", "#e5ae37", "#6d904f"], explode=[0.1, 0.1, 0, 0], autopct="%1.1f%%", shadow=True, startangle=90, wedgeprops={"edgecolor": "black"})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f