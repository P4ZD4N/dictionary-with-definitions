from enum import IntEnum

Dictionary_Menu = IntEnum("Dictionary", ["Add", "Find", "Delete", "Quit"])
dictionary = {}

while True:

    print(
"""
= Choose one option =
1: Add definition
2: Find definition
3: Delete definition
4: Quit
"""
    )

    user_option = int(input("Enter option: "))

    if user_option == Dictionary_Menu.Add:
        word = input("What word do you want to define?: ").lower()
        if word in dictionary:
            print(f"Dictionary actually contain a definition of {word}!")
            continue
        else:
            definition = input("Now enter definition of this word: ").lower()
            dictionary.update({word: definition})
            print(f"{word} definition was successfully added to dictionary!")
            continue

    elif user_option == Dictionary_Menu.Find:
        def_to_find = input("Enter word for which you want to find definition: ").lower()
        if def_to_find in dictionary:
            print(f"{def_to_find.capitalize()} - {dictionary[def_to_find].capitalize()}")
            continue
        else:
            print(f"Dictionary doesn't contain a definition of {def_to_find}!")
            continue

    elif user_option == Dictionary_Menu.Delete:
        def_to_del = input("Enter word which definition you want to delete: ").lower()
        if def_to_del in dictionary:
            dictionary.pop(def_to_del)
            print(f"{def_to_del} definition was successfully deleted from dictionary!")
            continue
        else:
            print(f"Dictionary doesn't contain a definition of {def_to_del}!")
            continue

    elif user_option == Dictionary_Menu.Quit: break

    else:
        print("You have chosen the wrong option! Try again.")
        continue