import utils


# Закомментируйте чтобы протестировать работу программы
# import pyperclip



def main():

    lang: str = utils.choice_lan()


    if lang == "ru":
        print(f"{utils.lang_dict["enter_your_message_ru"]} 'leet': ")
    if lang == "en":
        print(f"{utils.lang_dict["enter_your_message_en"]} 'leet': ")
    leet = input("> ")
    print()
    leetspeak = utils.english_to_leetspeak(leet)
    print(leetspeak)


    utils.write_result(leetspeak)


    # Закомментируйте следующую строку кода, чтобы
    # протестировать работу программы
    # pyperclip.copy(leetspeak)
    # print("[INFO] Результат скопирован в буфер обмена.")


if __name__ == "__main__":
    main()
