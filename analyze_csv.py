import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("discussion.csv")

# Count activities across all three columns
activity_counts = df[['Activity 1', 'Activity 2', 'Activity 3']].stack().value_counts()
top_activities = activity_counts.head(5)

# Count tools (split multi-tool entries)
tool_counts = df['Tool'].str.split(r",| and | or ").explode().str.strip().str.title().value_counts()
top_tools = tool_counts.head(5)

# Print results
print("\n🔍 Most Popular Activities:")
print(top_activities)

print("\n🛠️ Most Popular Tools to Learn:")
print(top_tools)

# Prepare data for plotting
activity_labels = top_activities.index.tolist()
activity_values = top_activities.values.tolist()

tool_labels = top_tools.index.tolist()
tool_values = top_tools.values.tolist()

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart for activities
axs[0].bar(activity_labels, activity_values, color='lightgreen', edgecolor='black')
axs[0].set_title("🔍 Most Popular Activities")
axs[0].set_xlabel("Activities")
axs[0].set_ylabel("Mentions")
axs[0].tick_params(axis='x', rotation=45)
for i, count in enumerate(activity_values):
    axs[0].text(i, count + 0.2, str(count), ha='center', va='bottom', fontsize=10)

# Bar chart for tools
axs[1].bar(tool_labels, tool_values, color='skyblue', edgecolor='black')
axs[1].set_title("🛠️ Most Popular Tools to Learn")
axs[1].set_xlabel("Tools")
axs[1].set_ylabel("Mentions")
axs[1].tick_params(axis='x', rotation=45)
for i, count in enumerate(tool_values):
    axs[1].text(i, count + 0.2, str(count), ha='center', va='bottom', fontsize=10)

# Layout and save
plt.tight_layout()
plt.savefig("activity_tool_summary.png", dpi=300, bbox_inches='tight')
plt.show()