user_text = input("Enter your paragraph of text : ")

while True:
    print("\n" + "=" * 60)
    print("TEXT MANIPULATION MENU")
    print("=" * 60)
    print("01. Text Statistics")
    print("02. Change Text Case")
    print("03. Reverse Text")
    print("04. Extract Parts")
    print("05. Search In Text")
    print("06. Enter New Text")
    print("07. Exit")
    print("=" * 60)

    user_choice = input("\nEnter Your Choice (1-7) : ")

    if user_choice == "1":
        print("\n" + "-" * 40)
        print("TEXT STATISTICS")
        print("-" * 40)
        
        total_characters = len(user_text)
        print(f"Total Characters : {total_characters} Characters")
        
        words_list = user_text.split()
        total_words = len(words_list)
        print(f"Total Words : {total_words} Words")
        
        sentences = user_text.count(".") + user_text.count("!") + user_text.count("?")
        print(f"Total Sentences : {sentences} Sentences")
        
        if total_words > 0:
            total_letters = 0
            for word in words_list:
                total_letters += len(word)

            average_length = total_letters / total_words
            print(f"Average Word Length : {average_length:.1f} Characters")

            longest_word = ""
            for word in words_list:
                if len(word) > len(longest_word):
                    longest_word = word
            print(f"Longest Word : '{longest_word}' - {len(longest_word)} Characters")
        else:
            print("Longest Word : None")
        print("-" * 40)

    elif user_choice == "2":
        print("\n" + "-" * 40)
        print("CHANGE TEXT CASE")
        print("-" * 40)
        print("01. UpperCASE")
        print("02. lowercase")
        print("03. Title Case")
        print("-" * 40)

        case_choice = input("Enter Your Case Choice (1,2,3) : ")
        
        original_text = user_text

        if case_choice == "1":
            user_text = user_text.upper()
            print(f"\nIn Upper Case : {user_text}")
        elif case_choice == "2":
            user_text = user_text.lower()
            print(f"\nIn Lower Case : {user_text}")
        elif case_choice == "3":
            user_text = user_text.title()
            print(f"\nIn Title Case : {user_text}")
        else:
            print("\nInvalid Choice")

        if case_choice in ["1","2","3"]:
            print(f"\nBefore : {original_text}")
            print(f"After : {user_text}")
        print("-" * 40)

    elif user_choice == "3":
        print("\n" + "-" * 40)
        print("REVERSE TEXT")
        print("-" * 40)
        print("01. Entire Text Reversal")
        print("02. Each Word Reversal Seperately")
        print("03. Reverse Word Order")
        print("-" * 40)
        
        reverse_choice = input("Enter Your Reverse Choice (1,2,3) : ")

        original_text = user_text

        if reverse_choice == "1":
            print(f"\nReversed Entire User Text : {user_text[::-1]}")
        elif reverse_choice == "2":
            words = user_text.split()
            
            if len(words) == 0:
                print("\nText Is Empty")
            else:
                reversed_words = []
                for word in words:
                    reversed_words.append(word[::-1])
                
                user_text = " ".join(reversed_words)
                print("\nEach Word Reversed")
        elif reverse_choice == "3":
            words = user_text.split()

            if len(words) == 0:
                print("\nText Is Empty")
            else:
                reversed_order = words[::-1]
                user_text = " ".join(reversed_order)
                print("\nWord Order Reversed")
        else:
            print("\nInvalid Choice")

        if reverse_choice in ["1","2","3"]:
            print(f"\nBefore : {original_text}")
            print(f"After : {user_text}")
        print("-" * 40)

    elif user_choice == "4":
        print("\n" + "-" * 40)
        print("EXTRACT PARTS")
        print("-" * 40)
        print("01. First 50 Characters")
        print("02. Last 50 Characters")
        print("03. Custom Range")
        print("-" * 40)

        extract_choice = input("Enter Choice (1,2,3) : ")

        if extract_choice == "1":
            print(f"\nFirst 50 Characters : {user_text[:50]}")
        elif extract_choice == "2":
            print(f"\nLast 50 Characters : {user_text[-50:]}")
        elif extract_choice == "3":
            start = int(input("\nStart Position : "))
            end = int(input("End Position : "))
            print(f"\nText From {start} To {end} : {user_text[start:end]}")
        else:
            print("\nInvalid Choice")
        print("-" * 40)
    
    elif user_choice == "5":
        print("\n" + "-" * 40)
        print("SEARCH IN TEXT")
        print("-" * 40)
        
        search_word = input("Enter The Word To Search : ")

        if search_word in user_text:
            count = user_text.count(search_word)
            position = user_text.find(search_word)
            print(f"\nFound '{search_word}' {count} Time/s")
            print(f"First Appears At Position: {position}")
        else:
            print(f"\n'{search_word}' Not Found In Text")
        print("-" * 40)

    elif user_choice == "6":
        print("\n" + "-" * 40)
        print("ENTER NEW TEXT")
        print("-" * 40)
        
        user_text = input("Enter New Text: ")
        print("\nText Updated Successfully!")
        print("-" * 40)

    elif user_choice == "7":
        print("\n" + "=" * 60)
        print("Goodbye! Thanks For Using Text Manipulator!")
        print("=" * 60)
        break

    else:
        print("\n" + "-" * 40)
        print("Invalid Choice! Please Enter Between 1-7")
        print("-" * 40)
