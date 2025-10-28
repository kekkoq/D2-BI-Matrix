import re
from collections import Counter

# Load the raw discussion text
with open("discussion.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# Split responses by name
responses = raw_text.split("Your preferred name:")
responses = ["Your preferred name:" + r.strip() for r in responses if r.strip()]

# Initialize counters
activity_counter = Counter()
tool_counter = Counter()

# Define irrelevant phrases to exclude
irrelevant_phrases = [
    "Why Does This Tool Appeal To You For Business Intelligence",
    "I Want To Learn About All Of Them But Choosing One",
    "Tool You Want To Learn",
    "Tool I Want To Learn"
]

# Extract activities and tools
for response in responses:
    # Extract activities
    activities = re.findall(r"Your preferred activity \d+: (.+)", response)
    activity_counter.update(activities)

    # Extract tool phrase
    tool_match = re.search(r"Tool YOU want to learn:\s*(.+)", response, re.IGNORECASE)

    if tool_match:
        raw_tools = tool_match.group(1).strip()

        # Skip irrelevant phrases or empty responses
        if any(raw_tools.lower().startswith(phrase.lower()) for phrase in irrelevant_phrases) or not raw_tools:
            continue

        # Split and clean tool names
        if "," in raw_tools or " and " in raw_tools:
            split_tools = re.split(r",| and ", raw_tools)
            cleaned_tools = [tool.strip().title() for tool in split_tools if tool.strip()]
            unique_tools = list(set(cleaned_tools))
            tool_counter.update(unique_tools)
        else:
            tool_counter.update([raw_tools.title()])

# Show results
print("🔍 Most Popular Activities:")
for activity, count in activity_counter.most_common(5):
    print(f"{activity}: {count}")

print("\n🛠️ Most Popular Tools to Learn:")
for tool, count in tool_counter.most_common(5):
    print(f"{tool}: {count}")

import matplotlib.pyplot as plt

# Get top 5 activities and tools
top_activities = activity_counter.most_common(5)
top_tools = tool_counter.most_common(5)

# Separate labels and counts
activity_labels = [activity for activity, count in top_activities]
activity_counts = [count for activity, count in top_activities]

tool_labels = [tool for tool, count in top_tools]
tool_counts = [count for tool, count in top_tools]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart for activities
axs[0].bar(activity_labels, activity_counts, color='lightgreen', edgecolor='black')
axs[0].set_title("🔍 Most Popular Activities")
axs[0].set_xlabel("Activities")
axs[0].set_ylabel("Number of Mentions")
axs[0].tick_params(axis='x', rotation=45)
for i, count in enumerate(activity_counts):
    axs[0].text(i, count + 0.1, str(count), ha='center', va='bottom', fontsize=10)

# Bar chart for tools
axs[1].bar(tool_labels, tool_counts, color='skyblue', edgecolor='black')
axs[1].set_title("🛠️ Most Popular Tools to Learn")
axs[1].set_xlabel("Tools")
axs[1].set_ylabel("Number of Mentions")
axs[1].tick_params(axis='x', rotation=45)
for i, count in enumerate(tool_counts):
    axs[1].text(i, count + 0.1, str(count), ha='center', va='bottom', fontsize=10)

# Layout and display
plt.tight_layout()
plt.savefig("popular_tools_chart.png")
plt.savefig("popular_tools_and_activities.png", dpi=300, bbox_inches='tight')
plt.show()