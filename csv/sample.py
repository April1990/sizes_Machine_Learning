import pandas as pd

df_female = pd.read_csv('female.csv')
df_male = pd.read_csv('male.csv')
size = []


def top_clothing(read_file, write_file):
    read_file['Heightin'] = read_file['Heightin'].multiply(2.54)
    read_file['Weightlbs'] = read_file['Weightlbs'].multiply(0.45359237)
    read_file['chestcircumference'] = read_file['chestcircumference'].multiply(0.1)
    read_file['waistcircumference'] = read_file['waistcircumference'].multiply(0.1)
    read_file.rename(columns={"chestcircumference": "chest", "waistcircumference": "waist", "Heightin": "height", "Weightlbs": "weight", "Gender": "gender"}, inplace=True)

    for chest, waist in zip(read_file['chest'], read_file['waist']):
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
    f_tshirt = ['chest', 'waist', 'height', 'weight', 'size', 'gender']
    modified_female_tshirt = read_file.to_csv(write_file, columns=f_tshirt, encoding='utf-8', index=False)
    return modified_female_tshirt


if __name__ == '__main__':
    top_clothing(read_file=df_female, write_file='modified_female_tshirts.csv')
    top_clothing(read_file=df_male, write_file='modified_male_tshirts.csv')



