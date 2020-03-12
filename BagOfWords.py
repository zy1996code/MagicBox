# The Implementation of Bag of Words model.

import numpy as np
#Step 1: Tokenize a sentence
def word_extraction(sentence):
    words = sentence.split()
    cleaned_text = [w.lower() for w in words]
    return cleaned_text
#Step 2：Apply tokenization to all sentences
def tokenize(sentences):
    words = []
    for sentence in sentences:
        w = word_extraction(sentence)
        words.extend(w)
    words = sorted(list(set(words)))
    return words
#Step 3: Build vocabulary and generate vectors
def generate_bow(allsentences):
    vocab = tokenize(allsentences)
    print("Word List for Document \n{0} \n".format(vocab))
    for sentence in allsentences:
        words = word_extraction(sentence)
        bag_vector = np.zeros(len(vocab))
        for w in words:
            for i, word in enumerate(vocab):
                if word == w:
                    bag_vector[i] += 1

        print("{0}\n{1}\n".format(sentence, np.array(bag_vector)))

allsentences = ["Joe waited for the train", "The train was late", "Mary and Samantha took the bus",
"I looked for Mary and Samantha at the bus station",
"Mary and Samantha arrived at the bus station early but waited until noon for the bus"]

print(generate_bow(allsentences))
