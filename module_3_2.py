def send_email(message, recipient, *, sender='university.help@gmail.com'):
    sender_default = 'university.help@gmail.com'

    if recipient == sender:
        message = 'Нельзя отправить письмо самому себе! '
        return message
    if "@" not in sender:
        #print('Нет собаки')
        message = 'Невозможно отправить письмо с адреса '
        return message + sender + 'на адрес' + recipient
    if "@" not in recipient:
        #print('Нет собаки')
        message = 'Невозможно отправить письмо на адрес '
        return message + sender + 'на адрес' + recipient


    for i in ('.com', '.net', '.ru'):

        if i in sender[-len(i):]:
            if i == '.com' and sender == sender_default:
                break
            else:
                message = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса '
                return message + sender + ' на адрес ' + recipient
        else:
            message = 'Невозможно отправить письмо с адреса '
            return message + sender + ' на адрес ' + recipient

    flag = 0  # 1 - нет совпадений
    for j in ('.com', '.ru', '.net'):

        if j not in recipient[-len(j):]:
            flag = 1
        else:
            flag = 0
            break

    if flag == 0:
        if j in recipient[-len(j):]:
            if j == '.com':
                message ='Письмо успешно отправлено с адреса '
                return message + sender  + ' на адрес ' + recipient
            else:
                message = 'НЕСТАНДАРТНЫЙ ПОЛУЧАТЕЛЬ! Письмо отправлено с адреса '
                return message + sender + ' на адрес '+ recipient
                    #return message

    if flag == 1:
        message = 'Невозможно 111 11 отправить письмо c адреса '
        return message + sender + ' на адрес ' + recipient

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com' ))

print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))

print(send_email('Пожалуйста, исправьте задание','urban.student@mail.ru', sender='urban.teacher@mail.uk'))

print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))

print(send_email('Пожалуйста, исправьте задание','urban.student@mail.ru'))






