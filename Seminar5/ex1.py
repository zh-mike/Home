# 1. Написать программу, которая удаляет из текста все слова, содержащие "абв"

text = "Я люблю абвЖава иабв Питон"

answer_list = [el for el in text.split() if not "абв" in el]
# answer_list = list(filter(lambda el: not "абв" in el, text.split()))
print(" ".join(answer_list))