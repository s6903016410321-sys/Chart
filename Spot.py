"""My First Chart - Matplotlib assignment (w14)
Plot 9 graphs in one figure. The figure title is "My First Chart"
and every graph has its own Title, X label and Y label.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

fig, axs = plt.subplots(3, 3, figsize=(14, 11))
fig.suptitle("My First Chart", fontsize=20, fontweight="bold")

# 1) Scatter plot with colour bar
x = rng.uniform(0, 100, 100)
y = rng.uniform(0, 100, 100)
c = rng.uniform(0, 100, 100)
sc = axs[0, 0].scatter(x, y, c=c, cmap="RdYlBu", s=15)
fig.colorbar(sc, ax=axs[0, 0], label="Value")
axs[0, 0].set(title="Scatter Plot", xlabel="X value", ylabel="Y value")

# 2) Bubble chart (random sizes / colours)
x = rng.uniform(0, 100, 100)
y = rng.uniform(0, 100, 100)
c = rng.uniform(0, 100, 100)
size = rng.uniform(50, 600, 100)
sc = axs[0, 1].scatter(x, y, c=c, s=size, cmap="jet", alpha=0.6)
fig.colorbar(sc, ax=axs[0, 1], label="Value")
axs[0, 1].set(title="Bubble Chart", xlabel="X value", ylabel="Y value")

# 3) Horizontal bar chart
labels = ["A", "B", "C", "D"]
values = [10, 1, 8, 2]
axs[0, 2].barh(labels, values, color="steelblue")
axs[0, 2].set(title="Horizontal Bar Chart", xlabel="Value", ylabel="Category")

# 4) Line chart with grid
t = np.array([100, 200, 300, 400, 500])
score = np.array([10, 20, 30, 40, 50])
axs[1, 0].plot(t, score, color="tab:blue")
axs[1, 0].grid(True, linestyle="--", alpha=0.6)
axs[1, 0].set(title="Sports Match Data", xlabel="Minutes", ylabel="Energy")

# 5) Two lines
x = [0, 1, 2, 3, 4]
axs[1, 1].plot(x, [1, 4, 1, 5, 3], label="Line 1", color="tab:blue")
axs[1, 1].plot(x, [4, 1, 5, 1, 6], label="Line 2", color="tab:orange")
axs[1, 1].legend()
axs[1, 1].set(title="Two Line Chart", xlabel="X", ylabel="Y")

# 6) Line chart with markers
x = [0.5, 1.0, 1.5, 2.0, 2.5]
y = [2, 5, 3, 1, 6]
axs[1, 2].plot(x, y, color="tab:blue", marker="o", markerfacecolor="red",
               markeredgecolor="darkred")
axs[1, 2].set(title="Line Chart with Markers", xlabel="X", ylabel="Y")

# 7) Histogram
data = rng.normal(loc=50, scale=10, size=1000)
axs[2, 0].hist(data, bins=15, color="steelblue", edgecolor="white")
axs[2, 0].set(title="Histogram", xlabel="Value", ylabel="Frequency")

# 8) Pie chart with an exploded slice
fruits = ["Apples", "Bananas", "Cherries", "Dates"]
share = [35, 25, 20, 20]
axs[2, 1].pie(share, labels=fruits, explode=(0.1, 0, 0, 0), startangle=90,
              frame=True)
axs[2, 1].set(title="Pie Chart (Exploded)", xlabel="Fruit", ylabel="Share (%)",
              xticks=[], yticks=[])

# 9) Pie chart with legend and percentages
axs[2, 2].pie(share, autopct="%1.0f%%", startangle=90, frame=True)
axs[2, 2].legend(fruits, title="Fruit Stuffs", loc="upper left", bbox_to_anchor=(0.95, 1.0), fontsize=8)
axs[2, 2].set(title="Pie Chart (Legend)", xlabel="Fruit", ylabel="Share (%)",
              xticks=[], yticks=[])

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("my_first_chart.png", dpi=150)
plt.show()