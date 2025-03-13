import utils

# TODO: Аннотации ко всем идентификаторам в коде

flag: bool = True
try:
    import pyperclip
except ModuleNotFoundError:
    flag = False


def main():
    lang: str = utils.choice_lan()

    print(utils.lang_dict.get(lang).get("enter_your_message") + " 'leet'")
    leet = input("> ")

    print()
    leetspeak = utils.english_to_leetspeak(leet)
    print(leetspeak)

    utils.write_result(leetspeak)

    if flag:
        pyperclip.copy(leetspeak)
        print("[INFO] Результат скопирован в буфер обмена.")


if __name__ == "__main__":
    main()
