
def sum(list):
    sum = 0
    for idx in range(len(list)):
        sum = sum + list[idx]
    return sum

def mult(list):
    product = 1
    for idx in range(len(list)):
        product = product * list[idx]
    return product

def main():
    size = int(input("Enter the size of your list: "))
    list = []
    for idx in range(size):
        list.append(int(input("Enter an integer to add to your list: ")))
    sum_of_list = sum(list)
    product_of_list = mult(list)
    print(f'The sum of elements is {sum_of_list}')
    print(f'The product of elements is {product_of_list}')