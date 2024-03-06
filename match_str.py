import pandas as pd

def match_str():
    ExcelFile = 'match.xlsx'
    df = pd.read_excel(ExcelFile, sheet_name='match')

    list_a = df['Data_A'].tolist()
    list_b = df['Data_B'].tolist()
    match_a =[]
    match_b =[]

    for data_a in list_a:
        if not pd.isna(data_a):
            for data_b in list_b:
                if str(data_a) in str(data_b):
                    match_a.append(str(data_a))
                    match_b.append(str(data_b))
    
    for index, data in enumerate(match_a):
        df.at[index, 'Match_A'] = data
    
    for index, data in enumerate(match_b):
        df.at[index, 'Match_B'] = data

    df.to_excel(ExcelFile, index=False)
    print('Finish!')

def main():
    match_str()

if __name__ == '__main__':
    main()