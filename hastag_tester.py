import re
from collections import Counter

def find_most_common_hashtags(texts):
    hashtags = []
    for text in texts:
        found_hashtags = re.findall(r'#(\w+)', text)
        hashtags.extend(found_hashtags)
    hashtag_counter = Counter(hashtags)
    most_common_hashtags = hashtag_counter.most_common()
    return most_common_hashtags

# Example list of strings containing hashtags
texts = [
    "Check out this cool #python library!",
    "I love #programming and #coding in #Python",
    "Just finished my project. #happy #coding"
]
new_strings = []

most_common_hashtags = find_most_common_hashtags(texts)
for hashtag, count in most_common_hashtags:
    if count >= 2:
        for x in texts:
            if hashtag in x:
                new_strings.append(x)

print(new_strings)