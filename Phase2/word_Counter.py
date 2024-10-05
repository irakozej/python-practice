paragraph = input("Enter a paragraph: ")
word_list = paragraph.split()
word_count = 0
for word in word_list:
    if word in word_list:
        word_count += 1
    else:
        word_count[word] = 1
print(word_count)