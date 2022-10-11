# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Assignment2.py File, Octagon calculator in python.

import math


def main():

    # input
    side = float(input("Type in the side length of your octagon in centimeters: "))

    # process
    area = 2 * (1 + math.sqrt(2)) * math.pow(side, 2)
    perimeter = side * 8

    # output
    print(
        "\nThe area of the octagon is {0:,.2f} cm², and the perimeter is {1:,.1f} cm.".format(
            area, perimeter
        )
    )

    print("\n\nDone.")


if __name__ == "__main__":
    main()
