
import re #імпорт модуля регулярних виразів
import codecs # імпорт модуля для роботи з файлами
def delete_html_tags(html_file, result_file='cleaned.txt'):
    # функія для видалення тегі
    # в параметри нашої функції добавляємо сам файл і одразу створюємо змінну де буде зберігатись результат (очищений текст)
      with codecs.open(html_file, 'r', 'utf-8') as file:
    #відкриваємо файл за допомогою імпортованого модуля,
    # в дужках сам файл, що ми з ним робимо (тобто - r (Read))
    # і яким способом читатиметься файл: у кодуванні 'utf-8'
           html = file.read()  #зчитаний файл зберігаємо у нову змінну

      clean_text = re.sub(r'<[^>]*>', '', html)
      #пайтон метод регулярного виразу re.sub - пошук шаблону у рядку і заміна його на вказаний підрядок
      # r' - сирий рядок (щоб символ \ зчитувався як команда, а не частина рядку)
      # <[^>]*> - замінити все що між символами <> на '' (тобто на пустий рядок)
      # html - текст у якому ми робимо пошук і заміну символів

      with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)
        # відкриваємо файл для запису і записуємо в нього очищений текст від тегів


delete_html_tags('draft.html')