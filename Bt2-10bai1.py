import pandas as pd
dataframe_ex= { "a" : [ 1 , 2 , 3 , 4 , 5 ], "b" : [ 6  , 7 , 8 , 9 , 10 ], "c" : [ 11 , 12 , 13 , 14 , 15 ] }
df=  pd . DataFrame (dataframe_ex)
print(df)

print('In ra cot dau cua 1 data ')
print(df['a'])

print('In ra hàng đầu tiên của 1 data')
print(df.loc[0])

print('In ra phan tu dau cua mot series')
series_data = pd.Series([1,2,3,4,5])
