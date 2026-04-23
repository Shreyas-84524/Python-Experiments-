# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
# Experiment 10: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Subject": ["English", "Marathi", "Hindi-Sanskrit", "Mathematics", "Science&Technology", "Social Science"],
    "Marks": [71, 86, 94, 93, 91, 86]
}

df = pd.DataFrame(data)

ax = df.plot(x="Subject", y="Marks", kind="line", marker='o', legend=False, figsize=(10, 6))

plt.title("SSC Result Analysis (Academic Year 2022-2023)", pad=20)

info = "Shreyas Shigwan\n(English-71, Marathi-86 ,Hindi-Sanskrit -94, Mathematics-93,Science&Technology-91,Social Science-86)"

plt.text(2, 110, info, ha='center',
         bbox=dict(facecolor='white', edgecolor='black', linestyle='--'))

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.ylim(0, 125)

plt.grid(True)

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()