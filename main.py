import leetspeak_tools

# TODO: Аннотации ко всем идентификаторам в коде

flag: bool = True
try:
    import pyperclip
except ModuleNotFoundError:
    flag: bool = False


def main():
    lang: str = leetspeak_tools.choice_lang()

    print(leetspeak_tools.lang_dict.get(lang).get("enter_your_message") + " 'leet'")
    leet: str = input("> ")

    replacement_chance = leetspeak_tools.get_replacement_chance(lang)
    leetspeak: str = leetspeak_tools.english_to_leetspeak(leet, replacement_chance)
    print(leetspeak)

    leetspeak_tools.write_to_file(leetspeak)

    if flag:
        pyperclip.copy(leetspeak)
        print(f"{leetspeak_tools.lang_dict.get(lang).get("result is copied")}")


if __name__ == "__main__":
    main()
