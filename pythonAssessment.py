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


article_content = """
ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""

run_analysis = True
while run_analysis:
    target = "the"

    print(f"Occurrences of '{target}': {count_specific_word(article_content, target)}")
    print(f"Most Common Word: {identify_most_common_word(article_content)}")
    print(f"Average Word Length: {calculate_average_word_length(article_content):.2f}")
    print(f"Paragraph Count: {count_paragraphs(article_content)}")
    print(f"Sentence Count: {count_sentences(article_content)}")

    run_analysis = False