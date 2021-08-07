#! /usr/bin/env python3
'''
Left merge of three dataframes

df_one_two = df_one <- df_two
df_one_two_three = df_one_two <- df_three
'''

from pathlib import Path

from tabulate import tabulate
import datasense as ds
import pandas as pd
import numpy as np


def main():
    header_title = 'pandas merge'
    header_id = 'pandas-merge'
    output_url = 'pandas_merge.html'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    # df_one has unique values in 'id'
    df_one = pd.DataFrame(
        {
            'id': [1, 2, 3, 4, 5],
            'age': [134, 28, np.NaN, 29, 17],
            'ctg': ['A', 'A', 'B', 'C', None]
        }
    ).astype({'age': 'Int64'})
    df_one.index.name = 'rows'
    # df_one has unique values in 'id'
    print(
        tabulate(
            tabular_data=df_one,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    df_two = pd.DataFrame(
        {
            'id': [3, 4, 5, 6, 7, 4, 4],
            'ticket': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
            'amount': [24.1, np.NaN, 34.5, 19.5, 26.2, 27.3, np.NaN]
        }
    ).astype({'ticket': 'Int64'})
    df_two.index.name = 'rows'
    # df_two has multiple values in 'id'
    print(
        tabulate(
            tabular_data=df_two,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    df_three = pd.DataFrame(
        {
            'id': [4, 4, 4],
            'ticket': [1002, 1006, 1007],
            'amount': [13.69, 11.11, 69.13]
        }
    ).astype({'ticket': 'Int64'})
    df_three.index.name = 'rows'
    # df_three has multiple values in 'id'
    print(
        tabulate(
            tabular_data=df_three,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    ds.page_break()
    df_one_two = df_one.merge(
        right=df_two,
        how='left',
        left_on=['id'],
        right_on=['id'],
        indicator=True,
        validate='one_to_many'
    ).astype(
        dtype={
            'age': 'Int64'
        }
    )
    df_one_two.index.name = 'rows'
    ds.save_file(
        df=df_one_two,
        file_name=Path.cwd() / 'df_one_two.csv'
    )
    # df_one_two = df_one <- df_two is a one-to-many left merge
    print(
        tabulate(
            tabular_data=df_one_two,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    ds.page_break()
    # df_one_two_three = df_one_two <- df_three is a one-to-one left merge
    print()
    df_one_two_three = df_one_two\
        .drop(columns=['_merge'])\
        .merge(
            right=df_three,
            how='left',
            left_on=['id', 'ticket'],
            right_on=['id', 'ticket'],
            suffixes=('_left', '_right'),
            indicator=True,
            validate='one_to_one'
        )
    df_one_two_three.index.name = 'rows'
    print(
        tabulate(
            tabular_data=df_one_two_three,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    df_one_two_three = df_one_two_three.drop(columns=['_merge'])
    # create 'amount' from 'amount_left' and replace np.NaN from 'amount_right'
    df_one_two_three['amount'] = df_one_two_three['amount_left']\
        .where(
            df_one_two_three['amount_left'].notnull(),
            df_one_two_three['amount_right']
        )
    print(
        tabulate(
            tabular_data=df_one_two_three,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    df_one_two_three = df_one_two_three\
        .drop(columns=['amount_left', 'amount_right'])
    ds.save_file(
        df=df_one_two_three,
        file_name=Path.cwd() / 'df_one_two_three.csv'
    )
    print(
        tabulate(
            tabular_data=df_one_two_three,
            headers='keys',
            tablefmt='html',
            numalign='right',
            stralign='right',
            floatfmt='.2f'
        )
    )
    print()
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == '__main__':
    main()
