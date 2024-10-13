def send_email(message, recipient, *, sender='urban.info@gmail.com'):

    #print(message) # задание для выполняемого кода (тесты):

    if recipient == sender:
        message = 'Нельзя отправить письмо самому себе!'
        return message


    for i in ('.com', '.net', '.ru', '@'):

        if i in sender:
            if i == '.com':
                break
        else:
            message = 'Невозможно отправить письмо с адреса'
            return message, sender, 'на адрес', recipient


    for j in ('.com', '.net', '.ru', '@'):
        if j in recipient:
            if j == '.com':
                message ='Письмо успешно отправлено с адреса '
                return message, sender, 'на адрес ', recipient
            else:
                message = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса'
                return message, sender, 'на адрес', recipient



print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', ))

print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))

print(send_email('Пожалуйста, исправьте задание','urban.student@mail.ru', sender='urban.teacher@mail.uk'))

print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))






