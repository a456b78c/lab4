from business_layer.user_input import get_user_input
from business_layer.art_generator import generate_ascii_art
from presentation_layer.art_view import display_art
from persistence_layer.file_manager import save_art_to_file

def main():
    # Отримання даних від користувача
    user_input = get_user_input()
    
    # Генерація ASCII-арту
    ascii_art = generate_ascii_art(user_input)
    
    # Відображення ASCII-арту
    display_art(ascii_art)
    
    # Запит на збереження
    save_option = input("Зберегти ASCII-арт у файл? (yes/no): ").strip().lower()
    if save_option == 'так':
        filename = input("Введіть ім'я файлу для збереження: ")
        save_art_to_file(ascii_art, filename)

if __name__ == "__main__":
    main()
