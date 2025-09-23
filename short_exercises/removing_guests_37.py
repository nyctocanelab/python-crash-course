guest_list = ["SRK", "Salman", "Aamir", "Akshay", "Hrithik",
               "kiara", "Ananya", "Deepika", "Alia", "Katrina"]
removed_from_list = "Aamir"
guest_list.remove(removed_from_list)
# print(f"Unfortunately, {removed_from_list} can't make it to the dinner.")
removed_from_list = guest_list.pop(5)
# print(f"Unfortunately, {removed_from_list} can't make it to the dinner.")

# print("Good news! We found a bigger dinner table.")
guest_list.insert(0, "Ranbir") 
guest_list.insert(5, "Tripti Dimri")
guest_list.append("Disha Patani")

print("I can only invite two people for dinner.")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

for guest in guest_list:
    print(f"Dear {guest}, you are still invited to my dinner.")

while len(guest_list) > 0:
    del guest_list[0]

print(guest_list)
