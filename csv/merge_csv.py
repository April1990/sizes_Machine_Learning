import pandas as pd


def concat_data():
    f_tshirt = ['height(cm)', 'weight(kg)', 'gender', 'size']
    df = pd.concat(map(pd.read_csv, ['modified_female_shirts.csv', 'modified_male_shirts.csv']), ignore_index = True)
    merge_data = df.to_csv('merge_modified_data.csv', columns = f_tshirt, encoding = 'utf-8', index = False)
    return merge_data


if __name__ == '__main__':
    concat_data()
