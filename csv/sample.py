import pandas as pd

df_female = pd.read_csv('female.csv')
df_male = pd.read_csv('male.csv')
size = []


def female_top_clothing():
    df_female['Heightin'] = df_female['Heightin'].multiply(2.54)
    df_female['Weightlbs'] = df_female['Weightlbs'].multiply(0.45359237)
    df_female['chestcircumference'] = df_female['chestcircumference'].multiply(0.1)
    df_female['waistcircumference'] = df_female['waistcircumference'].multiply(0.1)
    df_female.rename(columns={"chestcircumference": "chest", "waistcircumference": "waist", "Heightin": "height", "Weightlbs": "weight", "Gender": "gender"}, inplace=True)

    for chest, waist in zip(df_female['chest'], df_female['waist']):
        if chest < 80:
            if waist < 65:
                size.append('XXS')

        elif chest <= 89:
            if waist >= 68:
                size.append('S')

            else:
                size.append('XS')

        elif chest <= 99:
            if waist >= 78:
                size.append('L')

            else:
                size.append('M')

        elif chest > 105:
            if waist > 89:
                size.append('XXL')

        elif chest <= 104:
            if waist >= 83:
                size.append('XL')

            else:
                size.append('L')



        #if chest in range(60-80):
         #   if waist in range(45-65):
          #      size.append('XS')
        #elif chest in range(81-85):
            #if waist in range(65-68):
                #size.append('S')

    df_female['size'] = pd.Series(size)
    f_tshirt = ['chest', 'waist', 'height', 'weight', 'size', 'gender']
    modified_female_tshirt = df_female.to_csv('modified_female_tshirts.csv', columns=f_tshirt, encoding='utf-8', index=False)
    return modified_female_tshirt


if __name__ == '__main__':
    female_top_clothing()

'''
        if 81 < chest < 85:
            if 65 < waist < 68:
                size.append('S')
            else:
                size.append('XS')
'''
