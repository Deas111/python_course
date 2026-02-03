



password = input("введите Пароль:")
special_chars = str('!#$%&*+,-./:;<=>?@\^_`|~')
lenght = len(password)
lenght_status = False
marks = 0

number = any(chap.isdigit() for chap in password)    #проверка на цифры
up_registr = any(char.isupper() for char in password)     #проверка на заглавные
down_registr = any(chal.islower() for chal in password)   # нижний регистр
has_special = any(chag in special_chars for chag in password) #спец. знаки

if lenght > 7:
    lenght_status = True

status_number = "есть" if number else "Нет"
status_up = "есть" if up_registr else "Нет"
status_down = "есть" if down_registr else "Нет"
status_has = "есть" if has_special else "Нет"
status_lenght = "есть" if lenght_status else "Нет"




if number:
    marks += 1
if up_registr:
    marks += 1
if down_registr:
    marks += 1
if has_special:
    marks += 1
if lenght_status:
    marks += 1

print(f"цифры: {status_number}")
print(f"длина больше 8 символов: {status_lenght}")
print(f"заглавные буквы: {status_up}")
print(f"прописные буквы: {status_down}")
print(f"спец. символы: {status_has}")


if marks == 5:
    print(f"пароль {marks}/5. пароль полностью надежен")
elif marks == 4:
    print(f"пароль {marks}/5.пароль хороший")
elif marks == 3:
    print(f"пароль {marks}/5.рекомендуем усложнить пароль")
elif marks == 2:
    print(f"пароль {marks}/5. пароль простой, не рекомендуется к использованию")
elif marks == 1:
    print(f"пароль {marks}/5. категорически не рекомендуется к использованию")