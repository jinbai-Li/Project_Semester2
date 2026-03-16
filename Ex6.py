studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
print("initial list")
for name in studentNames:
    print(f"{name} Evans")

new_name = input("enter new name")
studentNames.append(new_name)

print("\nname after adding")
for name in studentNames:
    print(f"{name} Evans")
