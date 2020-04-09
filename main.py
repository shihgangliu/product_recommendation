#!/bin/python3


import re
from classes.jaccard_index import JaccardIndex


if __name__ == '__main__':
    products = set()
    purchase_history = dict()

    with open('data.txt', 'r', encoding='UTF-8') as file:
        data = file.read().splitlines(True)[1:]

        for line in data:
            format_line = re.split(r'\t+', line)
            purchase_history[format_line[0]] = set()
            products.add(format_line[1])

        for line in data:
            format_line = re.split(r'\t+', line)
            purchase_history[format_line[0]].add(format_line[1])

    # Assignment 1
    max_jaccard_index_value = 0

    for first_name in purchase_history:
        for second_name in purchase_history:
            if first_name != second_name:
                jaccard_index_value = JaccardIndex(
                    purchase_history[first_name],
                    purchase_history[second_name]
                ).get_value()

                if jaccard_index_value > max_jaccard_index_value:
                    max_jaccard_index_value = jaccard_index_value
                    max_jaccard_index_pattern = (first_name, second_name)

    print('The {} and {} has the highest Jaccard Index value is {}.'.format(
        max_jaccard_index_pattern[0],
        max_jaccard_index_pattern[1],
        max_jaccard_index_value)
    )

    # Assignment 2
    andrew_recommendation_indexes = dict()
    products_not_in_andrew_history = products - purchase_history['andrew']

    for product in products_not_in_andrew_history:
        product_exclude_history = set()
        andrew_recommendation_indexes[product] = 0

        for shopper in purchase_history:
            if (shopper != 'andrew'
                    and product not in purchase_history[shopper]):
                product_exclude_history.add(shopper)

        for shopper in product_exclude_history:
            andrew_recommendation_indexes[product] += JaccardIndex(
                purchase_history['andrew'],
                purchase_history[shopper]
            ).get_value()

        andrew_recommendation_indexes[product] /= len(product_exclude_history)

    sorted_andrew_recommendation_indexes = sorted(
        andrew_recommendation_indexes.items(),
        key=lambda dic: dic[1],
        reverse=True
    )

    print('The products I want to recommend to andrew are: {}, {}, {}.'.format(
        sorted_andrew_recommendation_indexes[0][0],
        sorted_andrew_recommendation_indexes[1][0],
        sorted_andrew_recommendation_indexes[2][0])
    )
