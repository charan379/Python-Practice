# kwargs with dynamic printing format and dynamic keys and dynamic values

# function to display **kwargs items
def myFunc(**kvps):
    hkl = 0
    ## Get hkl ( highest key length value )
    for key, value in kvps.items():
        ## print key length
        print(f'{key} : length {len(key)}')
        ## present highest key length for now
        print(f'present highest key length for now is :  {hkl}')
        ## now get the key element with highest length by comparing all key elements with each other and store the
        ## length in hkl

        ## If present key length is higher than present Highest key length value than
        ## Replace present highest key length value with present key length
        if len(key) > hkl:
            hkl = len(key)
            print(f'Now replacing hkl with present key length \n'
                  f'key = {key} >> length = {hkl}')
        print(f"Here Final Highest Key Length value is : {hkl}")

    ## Print Key value pairs with good printing format
    for key, value in kvps.items():
        if len(key) == hkl:
            print(f'{key} : {value}')
        else:
            space = ''
            space_diff = hkl - len(key)
            ##print(space_diff)
            ## using While Loop
            # while space_diff != 1:
            #     space += ' '
            #     space_diff -= 1

            ## using For Loop
            for x in range(space_diff):
                space += ' '
                ##print(space.count(' '))
            ##print(key + space, ':', value)
            print(f'{key}+{space}:{value}')



myFunc(Name='Charan',  mobile_number='0987654321', Age = '23')
