def translate(text):
    """Решение рофловое не воспринимать близко к сердцу"""
    global translated_text
    text = text.replace('-', '').replace('е', '').replace('ы', '').replace('а', '') \
        .replace('о', '').replace('э', '').replace('я', '').replace('и', '').replace('ю', '') \
        .replace(',', '').replace('.', '').replace('/', '').replace(';', '').replace(':', '') \
        .replace("'", '').replace('"', '').replace('', '').replace('', '').replace('', '') \
        .replace('!', '').replace('У', '').replace('Ы', '').replace('О', '').replace('Э', '') \
        .replace('Я', '').replace('И', '').replace('Ю', '').replace('Е', '').replace('А', '') \
        .replace('у', '')
    translated_text = ''
    for word in text.split():
        translated_text += word.replace(' ', '') + ' '
    translated_text = translated_text[:-1]
