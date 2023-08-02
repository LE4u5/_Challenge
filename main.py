import re

def validate_card(array):
    
    for idx in range(array[0]):
        card_num = array[idx+1]

        # Checks if card number contains invalid characters
        result = re.search("^[0-9\-]*$",card_num)
        if not result:
            print('Invalid')
            continue

        # checks if card number begins with 4, 5, or 6 and returns invalid if it doesnt 
        result = re.search("^[456]", card_num)
        if(result == None):
            print('Invalid')
            continue
        if "-" in card_num:
        # validates numbers with hyphens then removes them
            result = re.search("^([0-9]{4}\-){3}[0-9]{4}", card_num)
            if result:
                card_num = re.sub("\-","",card_num)
            if not result:
                print('Invalid')
                continue

        # checks if card number has digits that repeat 4 or more times
        result = re.search(r"(\d)\1{3,}",card_num)
        if result:
            print('Invalid')
            continue

        # validates card number length
        if not len(card_num) == 16:
            print('Invalid')
            continue
        if len(card_num) == 16:
            print('Valid')
          
new_card_array = []

total = input() 
total = int(total)

new_card_array.append(total)

for num in range(total):
    card_num = input()
    new_card_array.append(card_num)

validate_card(new_card_array)
