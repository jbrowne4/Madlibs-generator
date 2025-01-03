#open the story.txt file
with open("story.txt", "r") as f:
    story = f.read()

#placeholder for input words
words = set()
start_of_word = -1

#parameters for placeholders
target_start = "<"
target_end = ">"

#add user input in story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

#detect placeholder
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

#dictionary storing user answers
answers = {}

#ask user to enter words
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#sub user input
for word in words:
    story = story.replace(word, answers[word])

print(story)