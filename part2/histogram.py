# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    histogram.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aputman <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 08:54:11 by aputman           #+#    #+#              #
#    Updated: 2021/03/08 08:54:12 by aputman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Not enough arguments")
    if len(sys.argv) > 2:
        sys.exit("Too much arguments")
    df = pd.read_csv(sys.argv[1])

    sns.histplot(data=df, x="Care of Magical Creatures",
                 hue="Hogwarts House", palette=['blue', 'green', 'red', 'yellow'])
    plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin',
               'Ravenclaw'], loc='upper left', frameon=False)
    plt.xlabel('Student Marks')
    plt.ylabel('Number of students')

    plt.show()
