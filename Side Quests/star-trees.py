
def triangle_one():
    count = 5
    for i in range(5):
        print("*" * count)
        count = count- 1

    # *****
    # ****
    # ***
    # **
    # *

def triangle_two():
    count = 1
    for i in range(5):
        print("*" * count)
        count = count + 1

    # *
    # **
    # ***
    # ****
    # *****


def triangle_three():
    count = 1
    space = 4
    for i in range(5):
        print(" "* space)
        print("*" * count)
        count = count + 1
        space = space -1

    #     *
    #    **
    #   ***
    #  ****
    # *****

def main():
    triangle_two()
main()