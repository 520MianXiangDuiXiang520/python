#function
def change_number(number):
    hiding_number=number.replace(number[3:7],'*'*4)
    print(hiding_number)
change_number('15293621384')