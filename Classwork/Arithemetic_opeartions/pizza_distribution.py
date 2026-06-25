# Pizza Distribution Program

total_slices = int(input("Enter total number of pizza slices: "))
total_children = int(input("Enter total number of children: "))

slices_per_child = total_slices // total_children
remaining_slices = total_slices % total_children

print("Slices each child gets :", slices_per_child)
print("Remaining slices :", remaining_slices)
