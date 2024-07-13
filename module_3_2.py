# Задание №1
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Задание №2 Проверка на корректность e-mail адреса
    valid_domains = [".com", ".ru", ".net"]
    if "@" not in recipient or not any(recipient.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if "@" not in sender or not any(sender.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Задание №3 Проверка на отправку самому себе
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        return

    # Задание №4 Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        # Задание №5 и №6
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Задание №7 Примеры вызова функции
send_email('Это сообщение для проверки связи', 'valentinov9797@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
