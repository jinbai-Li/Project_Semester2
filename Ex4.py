age = int(input("Enter your age："))
if age <= 19:
    print("qualify for student discounts！")
elif 20 <= age <= 54:
    print("qualify for no age discounts！")
else:
    print(" receive senior discounts！")
