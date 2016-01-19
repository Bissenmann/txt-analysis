import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Necessary if you haven't downloaded nltk packages
# nltk.download()

# Put your own text file to analyze below
##text = open("sampleText.txt", "r")
##text.read()

sampleText = "“Dreams don't work unless you do.” Personal statement stil' underway, 2800 extra letters I need to get rid of. Here’s what it looks like at the moment: I launched my own graphic design business the day I turned up 16, the minimum legal age to be paid. Needless to say I was eager to start. My unyielding passion for design began at a young age but has developed and honed over the last few years. I used this personal strength as an opportunity to start something I would be proud of. So, for over a year and a half, I sold logos, animations and websites to companies and individuals online. I just created visual identities that enabled organisations to put their best face forward to their audience. But unlike most small online agencies, I tailored my designs exclusively to my client’s needs. I achieved this by examining thoroughly their business and industry in order to best visually interpret their company, thus to better communicate their values, and most importantly, to distinguish them from their competitors. This actually means that before designing and selling my products I figured out, along with my clients, what was the target audience we had to appeal to. Working with wide sets of data was not only incredibly exciting, it has also given me key informations about the markets I had to understand; and by deciphering these datas I strengthened my analysing skills. I have really enjoyed this marketing process of my job because it relied on my ability to interpret data in a meaningful way. Nonetheless, early this september I decided to put a stop to this thrilling and profitable business to better focus on my studies. I believe that having such an early approach to the business world is a priceless bonus for my career. Through prototyping websites for my clients, I also merged my appeal for programing to my business. With the magic of HTML and CSS, I could combine design, maths and interaction altogether. I see programing as a fantastic form of expression and I firmly believe it should be taught at school early on, like any other languages. I was born in the US, I have traveled in 21 countries and I have lived in Canada, Belgium and France. I am bilingual in French and English and fluent in Spanish. Moving in different countries in my youth has enabled me to discover a variety of cultures. I love to be internationally surrounded, it’s the way I’ve been growing. My current school offers me a broad cultural experience with the ability to connect with students from all around the world, and I would love to find this multicultural experience at University."

# Importing stop words ('useless' words) from the nltk corpus
stop_words = set(stopwords.words("english"))

words = word_tokenize(sampleText)

filteredText = [w for w in words if w not in stop_words]

print(filteredText)

# print(word_tokenize(sampleText))

# To print the most common words use

print("Most common words", sampleText.most_common(15))
