"""
Created on Mon Jun 10 21:43:20 2019

@author: venkat
"""
def validate_credit_card_number(card_number):
    temp_list = [int(c) for c in str(card_number)]

    list1 = temp_list[-2::-2]
    list2 = temp_list[::-2]

    total_sum = sum(list2)
    for el in list1:
        el *= 2
        if(el > 9):
            sum_res = 0
            while el:
                rem = el % 10
                sum_res += rem
                el = el // 10
            total_sum += sum_res
        else:
            total_sum += el

    return(total_sum % 10 == 0)

card_number=int(input("Enter the credit card number : "))

result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
