#Подсчет количества каждой буквы в строке:

def get_count_char(str_):
    str_ = str_.lower()
    letters_dict = {}
    for letter in str_:
        if letter.isalpha():
            letters_dict[letter] = letters_dict.get(letter, 0) + 1
    return letters_dict

main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
print(get_count_char(main_str))

#Определение процентного отношения количества каждой буквы к общему числу букв в строке:

def get_percent_char(letters_dict):
    percent_dict = {}
    letters_sum = sum(letters_dict.values())
    for k, n in letters_dict.items():
        percent = round(n * 100 / letters_sum, 3)
        percent_dict[k] = percent_dict.get(k, percent)
    return percent_dict

print(get_percent_char(get_count_char(main_str)))