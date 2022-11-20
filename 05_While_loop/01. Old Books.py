searching_book = input()
current_book = input()
counter = 0
is_book_found = False
while current_book != "No More Books":
    if current_book == searching_book:
        break
    counter += 1
    current_book = input()
if not current_book == searching_book:
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter} books and found it.")

