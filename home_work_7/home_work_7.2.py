def correct_sentence(text):
    corrected_text = text.capitalize() #перша буква з великої літери
    if not corrected_text.endswith('.'): #якщо не закінчується крапкою, то добавляємо її
        corrected_text += '.'
    return corrected_text

text = input("Enter two sentences: ")

corrected_text = correct_sentence(text)
print(corrected_text)


