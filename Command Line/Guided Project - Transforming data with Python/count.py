import read

df = read.load_data()
word_counts = {}

for headline in df["headline"]:
    words = headline.lower().split(" ")
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

print(word_counts)