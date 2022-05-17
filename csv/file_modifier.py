import pandas as pd

df_female = pd.read_csv('female.csv')
df_male = pd.read_csv('male.csv')


def female_top_clothing():
    f_tshirts = ["waistcircumference", "waistdepth", "waistfrontlengthsitting", "acromialheight",
                 "chestbreadth", "chestcircumference", "chestdepth", "chestheight", "cervicaleheight", "neckcircumference",
                 "neckcircumferencebase", "suprasternaleheight", "Heightin", "weightkg", "Gender"]

    f_tshirts_modified = df_female.to_csv('csv/modified_female_tshirts.csv', columns=f_tshirts, encoding='utf-8', index=False)
    return f_tshirts_modified


def female_bottom_clothing():
    f_shorts = ["iliocristaleheight", "kneeheightmidpatella", "kneeheightsitting", "lowerthighcircumference",
                "poplitealheight", "thighcircumference", "thighclearance", "tibialheight", "waistheightomphalion", "Heightin", "weightkg", "Gender"]

    f_shorts_modified = df_female.to_csv('csv/modified_female_shorts.csv', columns=f_shorts, encoding='utf-8', index=False)
    return f_shorts_modified


def male_top_clothing():
    m_tshirts = ["waistcircumference", "waistdepth", "waistfrontlengthsitting", "acromialheight",
                 "chestbreadth", "chestcircumference", "chestdepth", "chestheight", "cervicaleheight", "neckcircumference",
                 "neckcircumferencebase", "suprasternaleheight", "Heightin", "weightkg", "Gender"]

    m_tshirts_modified = df_male.to_csv('csv/modified_male_tshirts.csv', columns=m_tshirts, encoding='utf-8', index=False)
    return m_tshirts_modified


def male_bottom_clothing():
    m_shorts = ["iliocristaleheight", "kneeheightmidpatella", "kneeheightsitting", "lowerthighcircumference",
                "poplitealheight", "thighcircumference", "thighclearance", "tibialheight", "waistheightomphalion", "Heightin", "weightkg", "Gender"]

    m_shorts_modified = df_male.to_csv('csv/modified_male_shorts.csv', columns=m_shorts, encoding='utf-8', index=False)
    return m_shorts_modified


if __name__ == '__main__':
    female_top_clothing()
    female_bottom_clothing()
    male_top_clothing()
    male_bottom_clothing()

''''
df_female = pd.read_csv('csv/female.csv' usecols=f_tshirts, index_col=None, encoding='utf-8')
'''
