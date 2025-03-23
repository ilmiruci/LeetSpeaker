import leetspeak_tools


flag: bool = leetspeak_tools.exists_pyperclip("pyperclip")


def main():
    lang: str = leetspeak_tools.choice_lang()

    print(
        leetspeak_tools.lang_dict.get(lang).get("enter_your_message")
        + " 'leet'"
    )
    leet: str = input("> ")

    replacement_chance = leetspeak_tools.get_replacement_chance(lang)
    leetspeak: str = leetspeak_tools.english_to_leetspeak(
        leet, replacement_chance
    )
    print(leetspeak)

    leetspeak_tools.write_to_file(leetspeak)

    if flag:
        leetspeak_tools.pyperclip.copy(leetspeak)
        print(f"{leetspeak_tools.lang_dict.get(lang).get("result is copied")}")


if __name__ == "__main__":
    main()
