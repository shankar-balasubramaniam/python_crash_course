# Define the dictionary with programming words and their meanings
glossary = {
    "variable": "A named value used to store data",
    "function": "A block of code that performs a specific task",
    "loop": "A control structure that repeats a set of instructions",
    "class": "A blueprint for creating objects with similar properties and methods",
    "module": "A file containing a set of functions or classes to be used in a program"
}

# Print each word and its meaning using separate print statements
# print("variable:", glossary["variable"])
# print("function:", glossary["function"])
# print("loop:", glossary["loop"])
# print("class:", glossary["class"])
# print("module:", glossary["module"])

# GLOSSARY 2
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")
