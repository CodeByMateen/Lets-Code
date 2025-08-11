'''
Input: "hello world this is code slayer"
Output: "olleh world siht is edoc slayer"

Tumhe ek string di gayi hai jisme multiple words hain. Tumhe is string me har alternate word ko reverse karna hai, baaki words ko waise hi rehne dena hai.
'''

### my solution

sentence = "hello world this is code slayer"
reverse = ""
sentence_list = sentence.split()

for i, word in enumerate(sentence_list):
    if i%2==0:
        if i==0:
            reverse = reverse + word[::-1]
        else:
            reverse = reverse + " " + word[::-1]
    else:
        reverse = reverse + " " + word
            
print(reverse)

### gpt solution

def alternate_reverse(s):
    words = s.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i][::-1]
    return " ".join(words)

# Test karo
sentence = "hello world this is code slayer"
print(alternate_reverse(sentence))

### mine cleaner one

sentence = "hello world this is code slayer"
words = sentence.split()
result = []

for i, word in enumerate(words):
    if i % 2 == 0:
        result.append(word[::-1])
    else:
        result.append(word)

output = " ".join(result)
print(output)
