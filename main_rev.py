import re

def validate_card(array):
    for idx in range(array[0]):
        card_num = array[idx+1]
        if re.search("^[456]([0-9]{14})|^[456][0-9]{3}(-[0-9]{4}){3}$",card_num) and \
            not re.search(r"(\d)\1{3,}",re.sub("\-","",card_num)):
            print("Valid",card_num)
            continue
        print("Invalid")
          
card_array = []

total = input() 
total = int(total)

card_array.append(total)

for num in range(total):
    card_num = input()
    card_array.append(card_num)

validate_card(card_array)
