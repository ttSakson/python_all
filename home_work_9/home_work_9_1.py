# text = input("Enter your text: ").lower()  #весь текст перевожу у нижній регістр
# words_list = text.split()  #створюю список, в якому розділяю кожне слово
#
#
# def popular_words(words_list, word=None):
#     word_count = {}  #сторення пустого словника, куди поміщу результат роботи функції
#     for word in words_list: #для кожного слова зі списку розділених слів
#         word = word.lower()
#         if word in word_count:  # Перевіряємо чи слово є у словнику
#             word_count[word] += 1  #тоді збільшуємо кількість входжень на 1
#         else:
#             word_count[word] = 1
#     return word_count  #повернення результату фукнції у наш створений пустий словник
#
#
# result = popular_words(words_list)
# print(result)


#####################

# user_text = input("Please, enter your text: ").lower()
# text_letters = {}
#
# for char in user_text:
#     if char in text_letters:
#         text_letters[char] += 1
#     else:
#         text_letters[char] = 1
#
# print(text_letters)


