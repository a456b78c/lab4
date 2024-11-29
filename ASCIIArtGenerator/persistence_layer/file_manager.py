def save_art_to_file(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл: {filename}")
