def process_text(text):
    print("\nText Processing Menu:")
    print("1. Convert to UPPERCASE")
    print("2. Convert to lowercase")
    print("3. Count number of words")
    print("4. Reverse the text")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print("Uppercase Text:", text.upper())
    elif choice == '2':
        print("Lowercase Text:", text.lower())
    elif choice == '3':
        words = text.split()
        print("Number of Words:", len(words))
    elif choice == '4':
        print("Reversed Text:", text[::-1])
    else:
        print("Invalid choice!")

def process_list(data_list):
    print("\nList Processing Menu:")
    print("1. Find Maximum")
    print("2. Find Minimum")
    print("3. Calculate Sum")
    print("4. Sort List")

    choice = input("Choose an option (1-4): ")

    try:
        numbers = [float(item) for item in data_list]
    except ValueError:
        print("List contains non-numeric data.")
        return

    if choice == '1':
        print("Maximum Value:", max(numbers))
    elif choice == '2':
        print("Minimum Value:", min(numbers))
    elif choice == '3':
        print("Sum of Elements:", sum(numbers))
    elif choice == '4':
        print("Sorted List:", sorted(numbers))
    else:
        print("Invalid choice!")

# Main loop
while True:
    print("\n=== Text and List Data Processor ===")
    print("1. Process Text")
    print("2. Process List")
    user_choice = input("Enter your choice (1 or 2): ")

    if user_choice == '1':
        user_text = input("Enter the text: ")
        process_text(user_text)

    elif user_choice == '2':
        user_input = input("Enter list elements separated by spaces: ")
        user_list = user_input.split()
        process_list(user_list)

    else:
        print("Invalid main choice!")

    cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("Exiting the program. Goodbye!")
        break
