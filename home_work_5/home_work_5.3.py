# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string
hashtag = input("Enter your hashtag: ")
text = hashtag.title() #присвоїла тут змінну щоб вивівся результат

if len(text) > 140: #якщо довжирна рядка більша 140 то встановила межі символів через зріз рядка
    text = text[0:140]

for char in text: #я не знала як ще тут перевірити набір символів та пробіли, тому просто видалила їх через цикл
    if char in string.punctuation + " ":
        text = text.replace(char, "")

if text:
    hashtag = '#' + text
    print("Your hashtag: ", hashtag)
else:
    print("Invalid hashtag.")

