guests = ["John von Neumann", "Lev Landau", "Richard Feynman"]

inv_message1 = f"{guests[0]}, I would like to invite You."
print(inv_message1)
inv_message2 = f"{guests[1]}, I would like to invite You."
print(inv_message2)
inv_message3 = f"{guests[2]}, I would like to invite You."
print(inv_message3)
print("\n")

print(guests)
guests[0] = "Robert Oppenheimer"
inv_message1 = f"{guests[0]}, I would like to invite You."
print(inv_message1)
inv_message2 = f"{guests[1]}, I would like to invite You."
print(inv_message2)
inv_message3 = f"{guests[2]}, I would like to invite You."
print(inv_message3)
print("\n")

guests.insert(0, "Enrico Fermi")
guests.insert(2, "Marie Curie")
guests.append("Niels Bohr")
print(guests)
print("\n")

guest_to_del = guests.pop()
print(f"{guest_to_del}, I regret to inform you that your invitation has been canceled.")
guest_to_del = guests.pop()
print(f"{guest_to_del}, I regret to inform you that your invitation has been canceled.")
guest_to_del = guests.pop()
print(f"{guest_to_del}, I regret to inform you that your invitation has been canceled.")
guest_to_del = guests.pop()
print(f"{guest_to_del}, I regret to inform you that your invitation has been canceled.")
print(f"{guests[0]} and {guests[1]}, glad to inform you that your invitation remains valid")
del guests[1], guests[0]
print(guests)