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

    f_tshirt = ['chest(cm)', 'waist(cm)', 'height(cm)', 'weight(kg)', 'gender']
    modified_female_tshirt = read_file.to_csv(write_file, columns=f_tshirt, encoding='utf-8', index=False)
    return modified_female_tshirt


if __name__ == '__main__':
    top_clothing(read_file=df_female, write_file='modified_female_tshirts.csv')
    top_clothing(read_file=df_male, write_file='modified_male_tshirts.csv')


'''
    read_file['Heightin'] = read_file['Heightin'].multiply(2.54)
    read_file['Weightlbs'] = read_file['Weightlbs'].multiply(0.45359237)
    read_file['chestcircumference'] = read_file['chestcircumference'].multiply(0.1)
    read_file['waistcircumference'] = read_file['waistcircumference'].multiply(0.1)
    read_file.rename(columns={"chestcircumference": "chest(cm)", "waistcircumference": "waist(cm)",
                              "Heightin": "height(cm)", "Weightlbs": "weight(kg)", "Gender": "gender"}, inplace=True)
'''
