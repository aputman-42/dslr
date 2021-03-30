# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aputman <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/08 08:53:42 by aputman           #+#    #+#              #
#    Updated: 2021/03/08 08:53:43 by aputman          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

import numpy as np
import pandas as pd


def my_mean(dataset):
    _ = 0
    for value in dataset:
        _ += value
    return _ / dataset.size


def my_std(dataset):
    mean_dataset = my_mean(dataset)
    _ = 0
    for value in dataset:
        _ += np.square(value - mean_dataset)
    return np.sqrt(_ / dataset.size)


def my_percentile(dataset, percentile):
    dataset.sort()
    target = (dataset.size - 1) * (percentile / 100)
    low_estimate = np.floor(target)
    high_estimate = np.ceil(target)
    if low_estimate == high_estimate:
        return dataset[int(target)]
    d0 = dataset[int(low_estimate)] * (high_estimate - target)
    d1 = dataset[int(high_estimate)] * (target - low_estimate)
    return d0 + d1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Not enough arguments")
    if len(sys.argv) > 2:
        sys.exit("Too much arguments")
    df = pd.read_csv(sys.argv[1])
    features = df.columns.values.tolist()
    print(f'{"":31}|{"Count":^15}|{"Mean":^15}|{"Std":^15}|{"Min":^15}|{"25%":^15}|{"50%":^15}|{"75%":^15}|{"Max":^15}|')
    for feature in features:
        row = f'{feature:>30} |'
        try:
            data = np.array(df.loc[:, feature], dtype=float)
            data = data[~np.isnan(data)]
            if data.size == 0:
                raise Exception()
            row += f'{data.size:>14f} |{my_mean(data):>14.6f} |{my_std(data):>14.6f} |{my_percentile(data, 0):>14.6f} |{my_percentile(data, 25):>14.6f} |{my_percentile(data, 50):>14.6f} |{my_percentile(data, 75):>14.6f} |{my_percentile(data, 100):>14.6f} |'
        except:
            row += f'{df.loc[:, feature].size:>14.6f} |{"No numerical value to display":^110} |'
        print(row)
