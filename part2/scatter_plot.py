# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scatter_plot.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aputman <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 08:53:51 by aputman           #+#    #+#              #
#    Updated: 2021/03/08 08:53:52 by aputman          ###   ########.fr        #
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

    sns.scatterplot(data=df, x="Astronomy", y="Defense Against the Dark Arts",
                    hue="Hogwarts House", palette=['blue', 'green', 'red', 'yellow'], alpha=0.5)
    plt.xlabel(df.columns[7])
    plt.ylabel(df.columns[9])

    plt.show()
