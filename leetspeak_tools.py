import random


def exists_pyperclip(module_name):
    try:
        __import__(module_name)
    except ModuleNotFoundError:
        return False
    return True


lang_dict: dict[str, dict[str, str]] = {
    "ru": {
        "enter_your_message": "Введите ваше сообщение",
        "probability of replacement": "Вероятность замены символов",
        "result is copied": "[INFO] Результат скопирован в буфер обмена.",
    },
    "en": {
        "enter_your_message": "Enter your message",
        "probability of replacement": "Probability of symbols replacement",
        "result is copied": "[INFO] The result has been copied to the clipboard.",
    },
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


def get_replacement_chance(lang: str) -> float:
    replacement_chance: float = (
        int(
            input(f"{lang_dict.get(lang).get("probability of replacement")}: ")
        )
        / 100
    )
    return replacement_chance


def english_to_leetspeak(message: str, replacement_chance: float) -> str:
    """Преобразует английскую строку в сообщение и возвращает leetspeak."""
    char_mapping: dict[str, list[str]] = {
        "A": ["/-|", "4"],
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

    leetspeak = ""
    for char in message:
        if (
            char.upper() in char_mapping
            and random.random() <= replacement_chance
        ):
            leetspeak = leetspeak + random.choice(char_mapping[char.upper()])
        else:
            leetspeak = leetspeak + char
    return leetspeak


def write_to_file(
    leetspeak: str, file_name: str = "results.txt", encoding: str = "UTF-8"
):
    """Записывает результат преобразования текста в файл result.txt"""
    with open(file_name, mode="a", encoding=encoding) as file:
        file.write(f"{leetspeak}\n")
