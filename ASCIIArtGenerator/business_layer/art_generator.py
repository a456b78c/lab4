def generate_ascii_art(user_input):
    text = user_input['text']
    width = user_input['width']
    height = user_input['height']
    symbols = user_input['symbols']
    
    # Створюємо базову матрицю ASCII-арту, заповнену символами фону
    art = []
    for i in range(height):
        line = ''.join(symbols[j % len(symbols)] for j in range(width))
        art.append(line)

    # Розраховуємо координати для тексту
    start_row = height // 2
    start_col = (width - len(text)) // 2

    # Вставляємо текст у середину з іншим символом (наприклад, пробіл)
    for i in range(len(text)):
        art[start_row] = (art[start_row][:start_col + i] + 
                          text[i] + 
                          art[start_row][start_col + i + 1:])

    # Виводимо результат