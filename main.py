NUMBER_OF_DISKS = 3
number_of_moves = 2**NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

# initiate call from source A to target C with auxiliary B
def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods)

    for number in range(0, number_of_moves):
            print(number)

move(NUMBER_OF_DISKS, 'A', 'B', 'C')
