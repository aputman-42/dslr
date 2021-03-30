# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pair_plot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aputman <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 08:53:59 by aputman           #+#    #+#              #
#    Updated: 2021/03/08 08:54:00 by aputman          ###   ########.fr        #
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
    df = pd.read_csv(sys.argv[1], index_col="Index")

    sns.pairplot(df, hue='Hogwarts House', palette=[
                 'blue', 'green', 'red', 'yellow'], height=0.9, aspect=1.6)
    plt.tight_layout()

    plt.show()
