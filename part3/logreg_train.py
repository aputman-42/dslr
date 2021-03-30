# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aputman <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/18 08:41:37 by aputman           #+#    #+#              #
#    Updated: 2021/03/18 08:41:39 by aputman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

import numpy as np
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Not enough arguments")
    if len(sys.argv) > 2:
        sys.exit("Too much arguments")
    df = pd.read_csv(sys.argv[1], index_col="Index")

    norm_data = np.insert(np.apply_along_axis(lambda X: (X - np.nanmean(X)) / np.nanstd(X), 0, df.iloc[:, 5:].to_numpy()), 0, 1.0, axis=1)
    norm_data[np.isnan(norm_data)] = 0.0

    true_answers = df.iloc[:, 0]
    houses = np.unique(true_answers)
    final_weights = []

    total_timer = time.perf_counter()
    for i, house in enumerate(houses):
        house_timer = time.perf_counter()
        answer_table = np.where(true_answers == house, 1, 0)
        weights = np.zeros(norm_data.shape[1])
        error = np.array([float("inf")] * answer_table.size)

        while np.sum(error) > 1e-1:
            error = (1 / (1 + np.exp(-norm_data @ weights))) - answer_table
            weights -= 5e-1 * ((norm_data.transpose() @ error) / answer_table.size)
        print(f'House {house} computed in {time.perf_counter() - house_timer:.3f} seconds')
        final_weights.append([house, weights])
    print(f'\nAll houses computed in {time.perf_counter() - total_timer:.3f} seconds')
    np.save("weights", np.array(final_weights, dtype=object))
