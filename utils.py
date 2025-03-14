import random

# TODO: Аннотации ко всем идентификаторам в коде

lang_dict: dict[str, dict[str, str]] = {
    "ru": {
        "enter_your_message": "Введите ваше сообщение"
    },
    "en": {
        "enter_your_message": "Enter your message"
    }

}


def choice_lang() -> str:
    """
    Запрашивает у пользователя желаемый язык программы
    :return: str: ru or en
    """
    valid_languages: tuple[str, ...] = ("ru", "en")
    while True:
        lang = input("Выберите язык, русский - ru, английский - en: ")

        if lang in valid_languages:
            break

    return lang


def english_to_leetspeak(message) -> str:
    """Преобразует английскую строку в сообщение и возвращает leetspeak."""
    char_mapping: dict[str, list[str]] = {
        "A" : ["/-|", "4"],
        "B": ["8"],
        "C": ["(", "["],
        "D": ["|)"],
        "E": ["3"],
        "F": ["|=", "ph"],
        "G": ["6", "9"],
        "H": ["|-|"],
        "I": ["|", "!", "1"],
        "J": [")"],
        "K": ["|<", "|("],
        "L": ["|_", "1"],
        "M": ["|\\/|", "/\\/\\"],
        "N": ["|\\|", "^/", "/\\/"],
        "O": ["0", "()", "@"],
        "P": ["|>"],
        "Q": ["0", "0"],
        "R": ["|?", "|2"],
        "S": ["5", "$"],
        "T": ["7", "+"],
        "U": ["|_|", "/_/"],
        "V": ["\\/"],
        "W": ["\\/\\/", "\\X/"],
        "X": ["><", "*"],
        "Y": ["'/"],
        "Z": ["2"],
    }

    REPLACEMENT_CHANCE: float = 0.70
    leetspeak = ""
    for char in message:
        # TODO: Антипаттер: Магическое число.
        #  Можно вынести в константу или значение
        #  вероятности получить от пользователя.
        if char.upper() in char_mapping and random.random() <= REPLACEMENT_CHANCE:
            leetspeak = leetspeak + random.choice(
                char_mapping[char.upper()]
            )
        else:
            leetspeak = leetspeak + char
    return leetspeak


# TODO: 1. Переименовать фукнцию, добавить дополнительные параметры, например название для файла, кодировка
def write_to_file(leetspeak, file_name, encoding):
    """Записывает результат преобразования текста в файл result.txt"""

    # TODO: Использовать контекстный менеджер with.
    with open(file_name + ".txt", "a", encoding=encoding) as file:
        file.write(str(leetspeak) + "\n")
