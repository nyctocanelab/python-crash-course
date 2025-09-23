guest_list = ["SRK", "Salman", "Aamir", "Akshay", "Hrithik",
               "kiara", "Ananya", "Deepika", "Alia", "Katrina"]
removed_from_list = "Aamir"
guest_list.remove(removed_from_list)
print(f"Unfortunately, {removed_from_list} can't make it to the dinner.")
removed_from_list = guest_list.pop(5)
print(f"Unfortunately, {removed_from_list} can't make it to the dinner.")

print(f"Updated Guest List: + {guest_list}")