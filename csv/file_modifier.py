import pandas as pd

df_female = pd.read_csv('female.csv', usecols=['Heightin', 'Weightlbs', 'chestcircumference', 'waistcircumference', "Gender"])
df_male = pd.read_csv('male.csv')


def female_top_clothing():
    df_female.loc[:, 'Gender'] = 1
    df_female.loc[:, 'Heightin'] = df_male['Heightin'].multiply(2.54)
    df_female.to_csv('modified_female_tshirts.csv')

    '''
    df = f_tshirts.reset_index()
    for index, row in df.iterrows():
        df_dict = 
            {
            'chest_c': row['chestcircumference'] / 10,
            'waist_c': row['waistcircumference'] / 10,
            'gender': row['Gender'],
            'height': round(row['Heightin'] * 2.54, 2),
            'weight': round(row['Weightlbs'] * 0.45359237, 2)
        }
        df_list.append(df_dict)

    df_list.to_csv('modified_female_tshirts.csv', columns=df_dict, encoding='utf-8', index=False)

    #f_tshirts_modified = df_dict.to_csv('modified_female_tshirts.csv', columns=df_dict, encoding='utf-8', index=False)
    #return f_tshirts_modified
    '''


def female_bottom_clothing():
    pass
    f_shorts = ["iliocristaleheight", "kneeheightmidpatella", "kneeheightsitting", "lowerthighcircumference",
                "poplitealheight", "thighcircumference", "thighclearance", "tibialheight", "waistheightomphalion", "Heightin", "weightkg", "Gender"]

    f_shorts_modified = df_female.to_csv('modified_female_shorts.csv', columns=f_shorts, encoding='utf-8', index=False)
    return f_shorts_modified


def male_top_clothing():
    pass
    m_tshirts = ["waistcircumference", "waistdepth", "waistfrontlengthsitting", "acromialheight",
                 "chestbreadth", "chestcircumference", "chestdepth", "chestheight", "cervicaleheight", "neckcircumference",
                 "neckcircumferencebase", "suprasternaleheight", "Heightin", "weightkg", "Gender"]

    m_tshirts_modified = df_male.to_csv('modified_male_tshirts.csv', columns=m_tshirts, encoding='utf-8', index=False)
    return m_tshirts_modified


def male_bottom_clothing():
    pass
    m_shorts = ["iliocristaleheight", "kneeheightmidpatella", "kneeheightsitting", "lowerthighcircumference",
                "poplitealheight", "thighcircumference", "thighclearance", "tibialheight", "waistheightomphalion", "Heightin", "weightkg", "Gender"]

    m_shorts_modified = df_male.to_csv('modified_male_shorts.csv', columns=m_shorts, encoding='utf-8', index=False)
    return m_shorts_modified


if __name__ == '__main__':
    female_top_clothing()
    female_bottom_clothing()
    male_top_clothing()
    male_bottom_clothing()

''''
df_female = pd.read_csv('female.csv' usecols=f_tshirts, index_col=None, encoding='utf-8')
('modified_male_tshirts.csv', columns=m_tshirts, encoding='utf-8', index=False)

    height_cm = f_tshirts((["Heightin"]).multiply(2.54), 
    weight_kg = f_tshirts['Weightlbs'].multiply(0.45359237)
    chest_cm = f_tshirts['chestcircumference'].multiply(0.1)
    waist_cm = f_tshirts['waistcircumference'].multiply(0.1)
    gender = f_tshirts.loc[:, 'Gender'] = 1
'''
