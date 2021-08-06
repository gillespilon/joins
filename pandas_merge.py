#! /usr/bin/env python3
'''
Examples of pandas merge

- Left merge
'''

from pathlib import Path
import time

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
    # print('</pre>')
    # print(s1)
    # print('<pre style="white-space: pre-wrap;">')
    df_one = pd.DataFrame(
        {
            'id': [1, 2, 3, 4, 5],
            'age': [134, 28, np.NaN, 29, 17],
            'ctg': ['A', 'A', 'B', 'C', None]
        }
    ).astype({'age': 'Int64'})
    print('df_one')
    print("- has unique values in 'id'")
    print()
    print(
        tabulate(
            df_one,
            headers='keys',
            tablefmt='html',
            numalign="right",
            stralign="right"
        )
    )
    print()
    df_two = pd.DataFrame(
        {
            'id': [3, 4, 5, 6, 7, 4, 4],
            'ticket': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
            'amount': [24.1, np.NaN, 34.5, 19.5, 26.2, 27.3, np.NaN]
        }
    )
    print('df_two')
    print("- has multiple values in 'id'")
    print()
    print(
        tabulate(
            df_two,
            headers='keys',
            tablefmt='html',
            numalign="right",
            stralign="right"
        )
    )
    print()
    # left merge
    # fill_values = {'age': np.NaN, 'ticket': np.NaN}
    df_one_two = df_one.merge(
        right=df_two,
        how='left',
        left_on=['id'],
        right_on=['id'],
        indicator=True,
        validate='one_to_many'
    ).astype(
        dtype={
            'age': 'Int64',
            'ticket': 'Int64'
        }
    # ).fillna(value=fill_values)
    )
    ds.save_file(
        df=df_one_two,
        file_name='justatest.csv'
    )
    print('df_one -> df_two is a one-to-many left merge')
    print()
    # print(df)
    print(
        tabulate(
            df_one_two,
            headers='keys',
            tablefmt='html',
            numalign="right",
            stralign="right"
        )
    )
    print()
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == '__main__':
    main()
