import pandas as pd

df_male = pd.read_csv('male.csv')


def male_top_clothing():

    df_male.rename(columns = {"chestcircumference": "chest(cm)", "waistcircumference": "waist(cm)", "Heightin": "height(cm)",
                   "Weightlbs": "weight(kg)", "Gender": "gender"}, inplace = True)

    df_male.loc[:, 'height(cm)'] *= 2.54
    df_male.loc[:, 'weight(kg)'] *= 0.45359237
    df_male.loc[:, 'chest(cm)'] *= 0.1
    df_male.loc[:, 'waist(cm)'] *= 0.1

    df_male.loc[(df_male['chest(cm)'] < 79), 'size'] = 'XXS'
    df_male.loc[(df_male['waist(cm)'] < 74), 'size'] = 'XXS'
    df_male.loc[(df_male['chest(cm)'] >= 79) & (df_male['chest(cm)'] < 81), 'size'] = 'XS'
    df_male.loc[(df_male['waist(cm)'] >= 74) & (df_male['waist(cm)'] < 76), 'size'] = 'XS'
    df_male.loc[(df_male['chest(cm)'] >= 81) & (df_male['chest(cm)'] < 91), 'size'] = 'S'
    df_male.loc[(df_male['waist(cm)'] >= 76) & (df_male['waist(cm)'] < 81), 'size'] = 'S'
    df_male.loc[(df_male['chest(cm)'] >= 91) & (df_male['chest(cm)'] < 102), 'size'] = 'M'
    df_male.loc[(df_male['waist(cm)'] >= 81) & (df_male['waist(cm)'] < 84), 'size'] = 'M'
    df_male.loc[(df_male['chest(cm)'] >= 102) & (df_male['chest(cm)'] < 112), 'size'] = 'L'
    df_male.loc[(df_male['waist(cm)'] >= 84) & (df_male['waist(cm)'] < 87), 'size'] = 'L'
    df_male.loc[(df_male['chest(cm)'] >= 112) & (df_male['chest(cm)'] < 122), 'size'] = 'XL'
    df_male.loc[(df_male['waist(cm)'] >= 87) & (df_male['waist(cm)'] < 97), 'size'] = 'XL'
    df_male.loc[(df_male['chest(cm)'] >= 122) & (df_male['chest(cm)'] < 127), 'size'] = 'XXL'
    df_male.loc[(df_male['waist(cm)'] >= 97) & (df_male['waist(cm)'] < 107), 'size'] = 'XXL'
    df_male.loc[(df_male['chest(cm)'] > 127), 'size'] = '3XL'
    df_male.loc[(df_male['waist(cm)'] > 122), 'size'] = '3XL'

    f_tshirt = ['height(cm)', 'weight(kg)', 'gender', 'size']
    modified_male_tshirt = df_male.to_csv('modified_male_shirts.csv', columns = f_tshirt, encoding = 'utf-8',
                                          index = False)
    return modified_male_tshirt


if __name__ == '__main__':
    male_top_clothing()