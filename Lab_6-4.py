# Author: Caleb Moura

# Creating a list of 3 subjects
subjects = ["Geometry", "Chemistry", "AP Spanish"]

# Printing the original list
print("Original List:", subjects)

# Adding fourth subject to the end of the list
subjects.append("Computer Programming")

# Printing the list after adding a subject
print("List after adding a subject:", subjects)

# Finding the index of a specific subject in the list
subject_index = subjects.index("Chemistry")
print("Index of 'Chemistry':", subject_index)

# Sorting the list alphabetically
subjects.sort()

# Printing the list after sorting
print("List after sorting alphabetically:", subjects)

# Creating copy of the original list
subjects_copy = subjects.copy()

# Printing the copied list
print("Copied List:", subjects_copy)

# Sorting the copied list in reverse alphabetical order
subjects_copy.sort(reverse=True)

# Printing the copied list after reverse sorting
print("Copied List after reverse sorting:", subjects_copy)