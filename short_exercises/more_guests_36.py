guest_list = ["SRK", "Salman", "Aamir", "Akshay", "Hrithik",
               "kiara", "Ananya", "Deepika", "Alia", "Katrina"]
removed_from_list = "Aamir"
guest_list.remove(removed_from_list)
print(f"Unfortunately, {removed_from_list} can't make it to the dinner.")
removed_from_list = guest_list.pop(5)
print(f"Unfortunately, {removed_from_list} can't make it to the dinner.")

print("Good news! We found a bigger dinner table.")
guest_list.insert(0, "Ranbir") 
guest_list.insert(5, "Tripti Dimri")
guest_list.append("Disha Patani")

for guest in guest_list:
    print(f"Dear {guest}, you are invited to my birthday dinner.")