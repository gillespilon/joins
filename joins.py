#! /usr/bin/env python3

import pandas as pd
left_table = pd.read_csv('left_table.csv') # prefer csv for very large files
left_table.insert(loc=2, column='Desk Location', value='')
right_table = pd.read_csv('right_table.csv') # prefer csv for very large files
left_table['Desk Location'] = left_table[['Employee']]\
        .merge(right_table[['Names', 'Desk Location']],\
        left_on='Employee',\
        right_on='Names',\
        how='left')\
        ['Desk Location'].values
left_table = left_table[['ID', 'Employee', 'Desk Location']]\
        [left_table['Desk Location'].isnull()]
left_table = left_table.dropna(subset=['Employee'])
left_table['ID'] = left_table['ID'].astype(dtype='int')
left_table.to_csv('left_table_exceptions.csv')

