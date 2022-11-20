command = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
counter_of_tickets = 0
total_counter_of_ticket = 0
seat_is_available = False
while command != "Finish":
    name_of_film = command
    free_seat = int(input())
    second_command = input()
    while second_command != "End":
        kind_of_ticket = second_command
        if kind_of_ticket == "standard":
            standard_tickets += 1
        elif kind_of_ticket == "kid":
            kid_tickets += 1
        elif kind_of_ticket == "student":
            student_tickets += 1
        counter_of_tickets += 1
        total_counter_of_ticket += 1
        if free_seat == counter_of_tickets:
            seat_is_available = True
            hall_occupancy_rate = (counter_of_tickets / free_seat) * 100
            break
        second_command = input()
    hall_occupancy_rate = (counter_of_tickets / free_seat) * 100
    print(f"{name_of_film} - {hall_occupancy_rate:.2f}% full.")
    counter_of_tickets = 0
    command = input()
percentage_students_ticket = (student_tickets / total_counter_of_ticket) * 100
percentage_standard_ticket = (standard_tickets / total_counter_of_ticket) * 100
percentage_kids_ticket = (kid_tickets / total_counter_of_ticket) * 100
print(f"Total tickets: {total_counter_of_ticket}")
print(f"{percentage_students_ticket:.2f}% student tickets.")
print(f"{percentage_standard_ticket:.2f}% standard tickets.")
print(f"{percentage_kids_ticket:.2f}% kids tickets.")
