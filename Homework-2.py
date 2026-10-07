paragraph = """Python is a popular programming language"""

print("Length of paragraph:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview:", paragraph[:50])

paragraph = paragraph.replace("Python", "PYTHON")
print("After replacement:", paragraph)

paragraph = paragraph.lower()
print("Lowercase:", paragraph)

paragraph = paragraph.strip()
print("After strip:", paragraph)

words = paragraph.split()
print("Words:", words)

if "course" in paragraph:
    print("The word 'course' is found in the paragraph.")

print("The course description is {} characters long and has {} words.".format(len(paragraph), len(words)))