import matplotlib.pyplot as plt

# Given results
file_sizes = [200, 400, 600, 800, 1000]  # MB

# Time taken in seconds for each language and file size
time_taken = {
    'C': [12, 20, 34, 45, 55],
    'C++': [15, 25, 36, 50, 60],
    'Java': [18, 30, 40, 55, 70],
    'R': [20, 35, 45, 60, 80],
    'Python': [25, 40, 53, 75, 100]
}

# Plotting the graph
plt.figure(figsize=(10, 6))

languages = list(time_taken.keys())
for i, language in enumerate(languages):
    plt.plot(file_sizes, time_taken[language], marker='o', label=language)

plt.xlabel('File Size (MB)')
plt.ylabel('Time Taken (sec)')
plt.title('Comparison of Time Taken to Convert Text Files to Upper Case')
plt.legend()
plt.grid(True)
plt.show()
