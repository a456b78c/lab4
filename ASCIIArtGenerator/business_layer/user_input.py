def get_user_input():
    text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))
    
    # Можливість вибору символів
    symbols = input("Введіть набір символів для малювання: ")
    
    return {
        'text': text,
        'width': width,
        'height': height,
        'symbols': symbols
    }
