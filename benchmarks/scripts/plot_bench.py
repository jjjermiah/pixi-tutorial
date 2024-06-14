import json
import matplotlib.pyplot as plt
from pathlib import Path
from dataclasses import dataclass

file_path = Path("results/hyperfine.json")


# Read and parse JSON data
with open(file_path, "r") as file:
    data = json.load(file)

@dataclass
class Benchmark:
    command: str
    mean: float
    stddev: float
    min: float
    max: float

    def __init__(self, benchmark_data: dict) -> None:
        self.command = benchmark_data["command"]
        self.mean = benchmark_data["mean"]
        self.stddev = benchmark_data["stddev"]
        self.min = benchmark_data["min"]
        self.max = benchmark_data["max"]

    def __str__(self):
        return f"{self.command} - Mean: {self.mean} Stddev: {self.stddev} Min: {self.min} Max: {self.max}"

    def label(self):
        return self.command.split()[0]


# Extracting data from the JSON structure
commands = data["results"]

benches = [Benchmark(bench) for bench in commands]

# Set font properties
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "Open Sans"
plt.rcParams["font.size"] = 12

# Creating the plot
fig, ax = plt.subplots(figsize=(16, 6))

# Extracting the labels and means
labels = [bench.label() for bench in benches]
means = [bench.mean for bench in benches]

# Horizontal bar chart for mean times with labeled exact seconds
bars = ax.barh(labels, means, capsize=5, color="#FFFF00", label="Mean ± σ")

# Adding labels and title
ax.set_xlabel("seconds", fontsize=14)
ax.set_title("Environment Creation Times (lower is better)", fontsize=16)


# Set the background color to dark gray
fig.patch.set_facecolor("#222426")
ax.set_facecolor("#2C2E31")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")


# Set the text color of the labels to white
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_color("white")
    label.set_fontsize(20)
plt.gca().invert_yaxis()

# # Set the bar order
# bar_order = [2, 0, 1]  # Example: [2, 0, 1] will place the third bar first, followed by the first and second bars
# ax.set_yticks(bar_order)

save_path = Path("results/benchmarks.png")
plt.savefig(save_path, facecolor=fig.get_facecolor(), bbox_inches="tight")
