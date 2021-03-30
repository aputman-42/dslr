# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aputman <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/12 13:30:45 by aputman           #+#    #+#              #
#    Updated: 2021/03/12 13:30:47 by aputman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

import numpy as np
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Not enough arguments")
    if len(sys.argv) > 3:
        sys.exit("Too much arguments")
    df = pd.read_csv(sys.argv[1], index_col="Index")
    weights = np.load(sys.argv[2], allow_pickle=True)

    norm_data = np.insert(np.apply_along_axis(lambda X: (X - np.nanmean(X)) / np.nanstd(X), 0, df.iloc[:, 5:].to_numpy()), 0, 1.0, axis=1)
    norm_data[np.isnan(norm_data)] = 0.0

    houses = weights[:, 0]
    my_answers = np.empty(df.shape[0], dtype=object)

    output_table = np.empty((df.shape[0], houses.shape[0]))

    t1 = time.perf_counter_ns()
    for i in range(norm_data.shape[0]):
        for j in range(output_table.shape[1]):
            output_table[i, j] = 1 / (1 + np.exp(-norm_data[i, :] @ weights[j][1]))
            my_answers[i] = houses[np.argmax(output_table[i])]
    print(f'All predictions computed in {(time.perf_counter_ns() - t1) / 1e+6:.2f} ms')

    pd.DataFrame(data=my_answers, columns=[df.columns[0]]).to_csv("houses.csv", index_label="Index")
