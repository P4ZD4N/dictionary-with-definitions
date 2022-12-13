
dictionary = {}

while True:

    print("= Choose one option =".upper())
    print("1: Add definition")
    print("2: Find definition")
    print("3: Delete definition")
    print("4: Quit")

    user_option = int(input("Enter option: "))

    if user_option == 1:
        word = input("What word do you want to define?: ")
        if word in dictionary:
            print(f"Dictionary actually contain a definition of {word}!")
            continue
        else:
            definition = input("Now enter definition of this word: ")
            dictionary.update({word: definition})
            print(f"{word} definition was successfully added to dictionary!")
            continue

    elif user_option == 2:
        def_to_find = input("Enter word for which you want to find definition: ")
        if def_to_find in dictionary:
            print(f"{def_to_find} - {dictionary[def_to_find]}")
            continue
        else:
            print(f"Dictionary doesn't contain a definition of {def_to_find}!")
            continue

    elif user_option == 3:
        def_to_del = input("Enter word which definition you want to delete: ")
        if def_to_del in dictionary:
            dictionary.pop(def_to_del)
            print(f"{def_to_del} definition was successfully deleted from dictionary!")
            continue
        else:
            print(f"Dictionary doesn't contain a definition of {def_to_del}!")
            continue

    elif user_option == 4: break

    else:
        print("You have chosen the wrong option! Try again.")
        continue