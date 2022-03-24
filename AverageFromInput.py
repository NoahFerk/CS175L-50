#Noah Ferker
#CS 175L
#Average From Input

def main():
    try:
        number_file = open('numbers.txt','r')
        total = 0
        counter = 0
        for line in number_file:
            number = float(line)
            total += number
            counter = counter + 1
            print('I read in ', counter, 'number(s) Current number is: ', f'{number:>8.2f}','Total is: ', f'{total:>8.2f}')
        avg = total/counter
        print('Average: ', avg)
        number_file.close()
    except ValueError:
        print('One of your numbers is not an int or float')
if __name__ == '__main__':
    main()
