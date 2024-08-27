def send_email(message, recipient,  sender = "university.help@gmail.com"):
    if '@' in sender and '@' in recipient and (recipient.endswith('.ru') or recipient.endswith('.com') or recipient.endswith('.net')) and (sender.endswith('.ru') or sender.endswith('.com') or sender.endswith('.net')):
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            return
        if sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса {} на адрес {}.".format(sender, recipient))
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}.".format(sender, recipient))
    else: print('Невозможно отправить письмо с адреса {} на адрес {}'.format(sender, recipient))




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')