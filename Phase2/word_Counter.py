paragraph = input("Enter a paragraph: ")
word_list = paragraph.split()
word_count = 0
for word in word_list:
    if word in word_list:
        word_count += 1
    else:
        word_count = 0
print(f"the entered paragraph is made up by: {word_count} words")
