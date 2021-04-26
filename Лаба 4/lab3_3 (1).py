def formated(text):
    for i in range(len(text)):
        if text[i] in ['—', '.', ',', ';', ':', '!', '?', '(', ')', '«', '»']:
            text = text.replace(text[i], ' ')
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    return words


def replace(word, words):
    for i in range(len(words)):
        if words[i] == word[0]:
            words[i] = word[1]


def unicDictWords(words, dictionary):
    k = 0
    unicWords = []
    already = []
    for i in range(len(words)):
        if words[i] not in already:
            unicWords.append(words[i])
            already.append(words[i])
    for i in range(len(unicWords)):
        try:
            if type(dictionary[unicWords[i]]) == int:
                k += 1
        except KeyError:
            pass
    return k


def dist(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]

def print_text(text, mistakes, keys):
    text = text.split()
    for i in range(len(text)):
        for j in range(len(mistakes)):
            if text[i].lower() == mistakes[j]:
                text[i] = keys[j]
            elif text[i][:-1].lower() == mistakes[j]:
                text[i] = keys[j] + text[i][-1]
    print(*text[:3])
    count = 0
    for i in range(3,len(text)):
        count += 1
        print(text[i], end=' ')
        if count % 30 == 0:
            print('\n', end=' ')


vocabulary = open('dict1.txt')
vocab = {}
for line in vocabulary:
    a = line.split()
    vocab[a[0]] = int(a[1])

txt = " ".join(list(open("brain040full.txt", encoding="utf=8")))

words = formated(txt)

print("--- Первичные расчёты ---")
print("кол-во словоформ в тексте: ", len(words))
print("кол-во различных словоформ в тексте: ", len(set(words)))
print('Количество уникальных словоформ присутствующих в словаре:', unicDictWords(words, vocab))

mist = []
print("--- Исправление ошибок ---")

for i in range(len(words)):
    if vocab.get(words[i]) is None:
        mist.append(words[i])

print("кол-во потенциальных ошибок в тексте: ", len(mist))

l = []
keys = []

for j in range(len(mist)):
    length = len(mist[j])
    wordsn = ""
    p = 0
    for key in vocab:
        d = dist(key, mist[j])
        if (d < length) or ((d == length) and (int(vocab[key]) > p)):
            length = d
            wordsn = key
            p = int(vocab[key])
    i = 0
    f = 0
    while i < len(mist[j]):
        i += 1
        str1 = mist[j][0:i]
        str2 = mist[j][i:len(mist[j])]
        if (str1 in vocab) and (str2 in vocab):
            keys.append(str1 + " " + str2)
            l.append(1)
            f = 1
    if (length < 3) and (f == 0):
        l.append(length)
        keys.append(wordsn)
    if (length >= 3) and (f == 0):
        l.append(length)
        keys.append("не найдено")

print("--- Исправленные слова")
for i in range(len(keys)):
    replace((mist[i], keys[i]), words)
    print(mist[i], '-', keys[i], '-', l[i])

print("--- Вторичные расчёты ---")
print("кол-во словоформ в тексте: ", len(words))
print("кол-во различных словоформ в тексте: ", len(set(words)))

mist.clear()
for i in range(len(words)):
    if vocab.get(words[i]) is None:
        mist.append(words[i])

print('Количество уникальных словоформ присутствующих в словаре:', unicDictWords(words, vocab))
print("кол-во потенциальных ошибок в тексте: ", len(mist))
print_text(txt, mist, keys)
vocabulary.close()
