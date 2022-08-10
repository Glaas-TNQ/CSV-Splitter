import pandas as pd
import xlsxwriter as xlsxwriter

#remember to change the path here to the path of your directory
df = pd.read_csv(r"csvpath\csvname.csv")


#In my case study the column containing all the different values to split the csv is called "KeyWord", replace it with your needs if you use this script

def newSplit():
    print(df.KeyWord.unique())
    uniques = df.KeyWord.unique()
    print(len(uniques))
    g = df.groupby(by=["KeyWord"], dropna=True)

    for KeyWord, KeyWord_df in g:
        print(KeyWord)
        print(KeyWord_df)
        length = len(KeyWord_df)
        writer = pd.ExcelWriter(f'{KeyWord}.xlsx')
        KeyWord_df.to_excel(writer)
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        #for row in range(1, length):
        #     url = df.iat[row, 1]
        #     worksheet.write_url(f'C{row}', url, string='Apply')
        writer.save()

newSplit()

