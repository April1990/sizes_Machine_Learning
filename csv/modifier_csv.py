import pandas as pd

df = pd.read_csv('merge_male_female.csv')


def female_top_clothing():

    df.rename(columns={"chestcircumference": "chest(cm)", "waistcircumference": "waist(cm)", "Heightin": "height(cm)",
                              "Weightlbs": "weight(kg)", "Gender": "gender"}, inplace=True)

    df.loc[:, 'height(cm)'] *= 2.54
    df.loc[:, 'weight(kg)'] *= 0.45359237
    df.loc[:, 'chest(cm)'] *= 0.1
    df.loc[:, 'waist(cm)'] *= 0.1

    df.loc[(df['chest(cm)'] < 79), 'size'] = 'XX-Small'
    df.loc[(df['waist(cm)'] < 74), 'size'] = 'XX-Small'
    df.loc[(df['chest(cm)'] >= 79) & (df['chest(cm)'] < 81), 'size'] = 'X-Small'
    df.loc[(df['waist(cm)'] >= 74) & (df['waist(cm)'] < 76), 'size'] = 'X-Small'
    df.loc[(df['chest(cm)'] >= 81) & (df['chest(cm)'] < 91), 'size'] = 'Small'
    df.loc[(df['waist(cm)'] >= 76) & (df['waist(cm)'] < 81), 'size'] = 'Small'
    df.loc[(df['chest(cm)'] >= 91) & (df['chest(cm)'] < 102), 'size'] = 'Medium'
    df.loc[(df['waist(cm)'] >= 81) & (df['waist(cm)'] < 84), 'size'] = 'Medium'
    df.loc[(df['chest(cm)'] >= 102) & (df['chest(cm)'] < 112), 'size'] = 'Large'
    df.loc[(df['waist(cm)'] >= 84) & (df['waist(cm)'] < 87), 'size'] = 'Large'
    df.loc[(df['chest(cm)'] >= 112) & (df['chest(cm)'] < 122), 'size'] = 'X-Large'
    df.loc[(df['waist(cm)'] >= 87) & (df['waist(cm)'] < 97), 'size'] = 'XL-Large'
    df.loc[(df['chest(cm)'] >= 122) & (df['chest(cm)'] < 127), 'size'] = 'XX-Large'
    df.loc[(df['waist(cm)'] >= 97) & (df['waist(cm)'] < 107), 'size'] = 'XX-Large'
    df.loc[(df['chest(cm)'] > 127), 'size'] = '3X-Large'
    df.loc[(df['waist(cm)'] > 122), 'size'] = '3X-Large'

    f_tshirt = ['height(cm)', 'weight(kg)', 'gender', 'size']
    modified_female_tshirt = df.to_csv('modified_male_female.csv', columns = f_tshirt, encoding = 'utf-8', index = False)
    return modified_female_tshirt


if __name__ == '__main__':
    female_top_clothing()


'''
def top_clothing(read_file, write_file):

    read_file.loc[:, 'Heightin'] *= 2.54
    read_file.loc[:, 'Weightlbs'] *= 0.45359237
    read_file.loc[:, 'chestcircumference'] *= 0.1
    read_file.loc[:, 'waistcircumference'] *= 0.1

    read_file.rename(columns={"chestcircumference": "chest(cm)", "waistcircumference": "waist(cm)",
                              "Heightin": "height(cm)", "Weightlbs": "weight(kg)", "Gender": "gender"}, inplace=True)

        for chest, waist in zip(read_file['chest(cm)'], read_file['waist(cm)']):
            if chest in range(66, 71):
                if waist in range(61, 66):
                    size.append('XS')
            else:
                size.append('XXS')
            if chest in range(86, 91):
                if waist in range(76, 81):
                    size.append('S')
            else:
                size.append('XS')
            if chest in range(97, 102):
                if waist in range(81, 84):
                    size.append('M')
            else:
                size.append('S')
            if chest in range(107, 112):
                if waist in range(84, 87):
                    size.append('L')
            else:
                size.append('M')
            if chest in range(116, 122):
                if waist in range(91, 97):
                    size.append('XL')
            else:
                size.append('L')
            if chest in range(122, 127):
                if waist in range(102, 107):
                    size.append('XXL')
            else:
                size.append('XL')
            if chest in range(127, 132):
                if waist in range(112, 122):
                    size.append('3XL')
            else:
                size.append('XXL')



    read_file['size'] = pd.Series(size)
    f_tshirt = ['height(cm)', 'weight(kg)', 'size']
    modified_female_tshirt = read_file.to_csv(write_file, columns=f_tshirt, encoding='utf-8', index=False)
    return modified_female_tshirt


if __name__ == '__main__':
    top_clothing(read_file=df_female, write_file='modified_male_female.csv')
    top_clothing(read_file=df_male, write_file='modified_male_shirts.csv')

*************************************************************************************

for chest, waist in zip(read_file['chest(cm)'], read_file['waist(cm)']):
    if chest < 74:
        if waist < 69:
            size.append('XXS')
 
       elif 74 >= chest < 81:
            if 69 >= waist < 76:
                size.append('XS')
        elif 81 >= chest < 91:
            if 76 >= waist < 81:
                size.append('S')
        elif 91 >= chest < 102:
            if 81 >= waist < 84:
                size.append('M')
        elif 102 >= chest < 112:
            if 84 <= waist < 87:
                size.append('L')
        elif 112 >= chest < 122:
            if 87 >= waist < 97:
                size.append('XL')
        elif 122 >= chest < 127:
            if 97 >= waist < 107:
                size.append('XXL')
        elif 127 >= chest >= 132:
            if 107 >= waist >= 122:
                size.append('3XL')     
'''
