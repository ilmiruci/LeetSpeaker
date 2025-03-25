import logging
from logging.handlers import RotatingFileHandler

from leetspeak_tools import (
    INFO_MESSAGES,
    choice_lang,
    english_to_leetspeak,
    exists_pyperclip,
    get_replacement_chance,
    write_to_file,
)

flag: bool = exists_pyperclip("pyperclip")


def main():
    lang: str = choice_lang()
    logger.debug(f"Пользователь выбрал язык {lang}")

    print(INFO_MESSAGES.get(lang).get("enter_your_message") + " 'leet'")
    leet: str = input("> ")
    logger.debug(f"Пользователь ввел текст {leet}")

    replacement_chance = get_replacement_chance(lang)
    leetspeak: str = english_to_leetspeak(leet, replacement_chance)
    logger.debug(f"Пользователь получил leetspeak-текст: {leetspeak}")

    print(leetspeak)

    write_to_file(leetspeak)
    logging.info("Перевод в leetspeak был сохранен в файл")

    if flag:
        import pyperclip

        pyperclip.copy(leetspeak)
        logging.debug(f"{INFO_MESSAGES.get(lang).get("result is copied")}")
        print(f"{INFO_MESSAGES.get(lang).get("result is copied")}")
    else:
        logger.debug("pyperclip не установлен")


if __name__ == "__main__":
    LOG_FILE_MAX_SIZE_BYTES: int = 1024 * 1024 * 5
    BACKUP_MAX_COUNT: int = 5

    logger = logging.getLogger(__name__)
    rotating_handler = RotatingFileHandler(
        filename="leetspeak.log",
        maxBytes=LOG_FILE_MAX_SIZE_BYTES,
        backupCount=BACKUP_MAX_COUNT,
    )
    formatter = logging.Formatter(
        "[%(asctime)s] | %(name)s | [%(levelname)s] | %(message)s"
    )

    logger.setLevel(logging.DEBUG)
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)

    main()
