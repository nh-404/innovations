
conversionType = input('''Choice your conversion type serial number: 
                        1. decimal 
                        2. binary 
                        3. octal 
                        4. hexadecimal
                        Q. Exit
->  ''')


while not conversionType == 'Q'.lower():

        if conversionType:
                
                user_input = input('Enter any number : ')


                def decimalToother(decimalNum): # decimal to binary/octal/hexadecimal

                        octal = oct(decimalNum)[2:]
                        binary = bin(decimalNum)[2:]
                        hexadecimal = hex(decimalNum)[2:]

                        return octal,binary,hexadecimal

                def otherTodecimal(baseNum,base):  # binary/octal/hexadecimal to decimal

                        decimalNum = int(baseNum,base)

                        return decimalNum


                if conversionType == '1':

                        decimalNum = int(user_input)
                        octal,binary,hexadecimal = decimalToother(decimalNum)

                        print(f'Binary: {binary}')
                        print(f'Octal: {octal}')
                        print(f'Hexadecimal: {hexadecimal}')

                elif conversionType == '2':
                        decimalNum= otherTodecimal(user_input,2)
                        print(f'Decimal: {decimalNum}')
                        octal,binary,hexadecimal = decimalToother(decimalNum)
                        print(f'Octal: {octal}')
                        print(f'Hexadecimal: {hexadecimal}')

                elif conversionType == '3':
                        
                        decimalNum = otherTodecimal(user_input,8)
                        print(f'Decimal: {decimalNum}')  
                        octal,binary,hexadecimal = decimalToother(decimalNum)
                        print(f'binary: {binary}')
                        print(f'Hexadecimal: {hexadecimal}')

                elif conversionType == '4':

                        decimalNum = otherTodecimal(user_input,16)
                        print(f'Decimal: {decimalNum}')
                        octal,binary,hexadecimal = decimalToother(decimalNum)
                        print(f'Octal: {octal}')
                        print(f'Binary: {binary}')

                else:
                        print('Enter vaild number')

