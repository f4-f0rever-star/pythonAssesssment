import re

# Counting Specific Word
def count_specific_word(text, search_word):
    if text == "":
        return 0
    
    text = text.lower()
    search_word = search_word.lower()

    words = re.findall(r"\b\w+\b", text)

    count = 0 
    for word in words:
        if word == search_word.lower():
            count += 1

    return count

# Identifying Most Common Word
def identify_most_common_word(text):
    if text == "":
        return None
    
    words = re.findall(r"\b\w+\b", text.lower())

    if len(words) == 0:
        return None
    
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    most_common = None
    highest_count = 0

    for word in word_count:
        if word_count[word] > highest_count:
            highest_count = word_count[word]
            most_common = word
    
    return most_common

# Calculating Average Word Length
def calculate_average_word_length(text):
    if text == "":
        return 0
    
    words = re.findall(r"\b\w+\b", text)
    
    if len(words) == 0:
        return 0
    
    total_length = 0
    for word in words:
        total_length += len(word)
    average = total_length / len(words)

    return average

# Counting Number of Paragraphs
def count_paragraphs(text):
    if text == "":
        return 1
    
    paragraphs = re.split(r"\n\s*\n", text.strip())
    
    count = 0
    i = 0

    while i < len(paragraphs):
        if paragraphs[i].strip() != "":
            count += 1
        i += 1

    return count

# Counting Number of Sentences
def count_sentences(text):
    if text == "":
        return 1
    
    sentences = re.findall(r"[.!?]+", text)
    return len(sentences)

with open("article.txt", "r") as file:
    article_content = file.read()


run_analysis = True
while run_analysis:
    target = "the"

    print(f"Occurrences of '{target}': {count_specific_word(article_content, target)}")
    print(f"Most Common Word: {identify_most_common_word(article_content)}")
    print(f"Average Word Length: {calculate_average_word_length(article_content):.2f}")
    print(f"Paragraph Count: {count_paragraphs(article_content)}")
    print(f"Sentence Count: {count_sentences(article_content)}")

    run_analysis = False