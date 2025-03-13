import utils

# TODO: Аннотации ко всем идентификаторам в коде

flag: bool = True
try:
    import pyperclip
except ModuleNotFoundError:
    flag: bool = False


def main():
    lang: str = utils.choice_lang()

    print(utils.lang_dict.get(lang).get("enter_your_message") + " 'leet'")
    leet: str = input("> ")

    print()
    leetspeak: str = utils.english_to_leetspeak(leet)
    print(leetspeak)

    utils.write_to_file(leetspeak, file_name="results", encoding="UTF-8")

    if flag:
        pyperclip.copy(leetspeak)
        print("[INFO] Результат скопирован в буфер обмена.")


if __name__ == "__main__":
    main()
