def mult(list):
    product = 1
    for idx in range(len(list)):
        product = product * list[idx]
    return product

def reverse(list):
    reversed = []
    for idx in range(len(list)):
        reversed.append(list[len(list)-1-idx])
    return reversed

def main():
    size = int(input("Enter the size of your list: "))
    list = []
    for idx in range(size):
        list.append(int(input("Enter an integer to add to your list: ")))
<<<<<<< HEAD
        
=======

>>>>>>> 135d07a (Changed comments above the main method function call.)
    sum_of_list = sum(list)
    product_of_list = mult(list)
    reversed_list = reverse(list)
    print(f'The sum of elements is {sum_of_list}')
    print(f'The product of elements is {product_of_list}')
    print(f'The reversed list is {reversed_list}')

<<<<<<< HEAD
## The main function will now run and prompt the user to provide information. Afterwards, all of the functions will be
## and the outputs will be printed to the user.
=======

## The main() method call will prompt users to enter information and will return print statements to the user.
>>>>>>> 135d07a (Changed comments above the main method function call.)
main()