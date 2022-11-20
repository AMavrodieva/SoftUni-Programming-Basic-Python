searching_book = input()
current_book = input()
counter_book = 0
book_is_found = False
while current_book != "No More Books":
    if current_book == searching_book:
        book_is_found = True
        break
    counter_book += 1
    current_book = input()
if not book_is_found:
    print(f"The book you search is not here!")
    print(f"You checked {counter_book} books.")
else:
    print(f"You checked {counter_book} books and found it.")
