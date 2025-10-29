import pandas as pd

# Load the CSV
df = pd.read_csv("discussion.csv")

# Combine all activity columns and count frequencies
activity_counts = df[['Activity 1', 'Activity 2', 'Activity 3']].stack().value_counts()
most_popular_activity = activity_counts.idxmax()
activity_count = activity_counts.max()

# Split multi-tool entries and count frequencies
tool_counts = df['Tool'].str.split(r",| and | or ").explode().str.strip().str.title().value_counts()
most_popular_tool = tool_counts.idxmax()
tool_count = tool_counts.max()

# Show results
print(f"🔍 Most Popular Activity: {most_popular_activity} ({activity_count} mentions)")
print(f"🛠️ Most Popular Tool to Learn: {most_popular_tool} ({tool_count} mentions)")