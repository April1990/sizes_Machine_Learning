import pandas as pd

df_female = pd.read_csv('female.csv')
df_male = pd.read_csv('male.csv')
size = []


def top_clothing(read_file, write_file):
    read_file.loc[:, 'Heightin'] *= 2.54
    read_file.loc[:, 'Weightlbs'] *= 0.45359237
    read_file.loc[:, 'chestcircumference'] *= 0.1
    read_file.loc[:, 'waistcircumference'] *= 0.1
    read_file.rename(columns={"chestcircumference": "chest(cm)", "waistcircumference": "waist(cm)",
                              "Heightin": "height(cm)", "Weightlbs": "weight(kg)", "Gender": "gender"}, inplace=True)

    for chest, waist in zip(read_file['chest(cm)'], read_file['waist(cm)']):
        if chest <= 81:
            if waist <= 76:
                size.append('XS')

            else:
                size.append('XXS')

        elif chest <= 102:
            if waist <= 84:
                size.append('M')

            else:
                size.append('S')

        elif chest <= 122:
            if waist >= 97:
                size.append('XL')

            else:
                size.append('L')

        elif chest <= 132:
            if waist >= 122:
                size.append('3XL')

            else:
                size.append('XXL')

    read_file['size'] = pd.Series(size)
    f_tshirt = ['height(cm)', 'weight(kg)', 'size']
    modified_female_tshirt = read_file.to_csv(write_file, columns=f_tshirt, encoding='utf-8', index=False)
    return modified_female_tshirt


if __name__ == '__main__':
    top_clothing(read_file=df_female, write_file='modified_female_shirts.csv')
    top_clothing(read_file=df_male, write_file='modified_male_shirts.csv')


'''
def top_clothing(read_file, write_file):
    read_file.rename(columns={"chestcircumference": "chest(cm)", "waistcircumference": "waist(cm)",
                              "Heightin": "height(cm)", "Weightlbs": "weight(kg)", "Gender": "gender"}, inplace=True)

    for chest, waist in zip(read_file['chest(cm)'], read_file['waist(cm)']):
        if chest <= 810:
            if waist <= 760:
                size.append('XS')

            else:
                size.append('XXS')

        elif chest <= 1020:
            if waist <= 840:
                size.append('M')

            else:
                size.append('S')

        elif chest <= 1220:
            if waist >= 970:
                size.append('XL')

            else:
                size.append('L')

        elif chest <= 1320:
            if waist >= 1220:
                size.append('3XL')

            else:
                size.append('XXL')

    read_file['size'] = pd.Series(size)
    f_tshirt = ['height(cm)', 'weight(kg)', 'size']
    modified_female_tshirt = read_file.to_csv(write_file, columns=f_tshirt, encoding='utf-8', index=False)
    return modified_female_tshirt


if __name__ == '__main__':
    top_clothing(read_file=df_female, write_file='modified_female_shirts.csv')
    top_clothing(read_file=df_male, write_file='modified_male_shirts.csv')

'''

#, 'size'
#'chest(cm)', 'waist(cm)'

