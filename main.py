def palindorme(number):
    original_number = number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_number == reverse_num:
        print("Giver number is a palindrome")
    else:
        print("Givern number is not a palindrome")


number = int(input("Enter a number: "))
print("Working")
print("Working")
palindorme(number)
