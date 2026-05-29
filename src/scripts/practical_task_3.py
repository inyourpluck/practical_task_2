import pandas as pd


def extract_name(row):
    if row['Marriage_Status'] == 'Mrs' and '(' in row['Name']:
        return row['Name'].split(',')[1].split('.')[1].split('(')[1].split()[0]
    else:
        return row['Name'].split(',')[1].split('.')[1].split()[0]

df = pd.read_csv('src/data/train.csv')

#Main info
df.info()

print(f'\nКоличество пропусков:\n{df.isna().sum()}')

print(f'\nСредние показатели:\n{df.select_dtypes(include=['number']).mean()}')

print(f'\nПроцент выживаемости у каждого класса пассажиров:\n{df.groupby('Pclass')['Survived'].sum() * 100/df.groupby('Pclass')['Survived'].count()}')


#Most popular names
df['Marriage_Status'] = df['Name'].str.split(',').str[1].str.split('.').str[0].str.strip()
df['First_Name'] = df.apply(extract_name, axis=1)

male_popular = df[df['Sex'] == 'male']['First_Name'].value_counts().head(1)
female_popular = df[df['Sex'] == 'female']['First_Name'].value_counts().head(1)

print(f'Самые популярные мужские имена:\n{male_popular}')
print(f'\nСамые популярные женские имена:\n{female_popular}')

#Most popular names by class
male_popular_by_class = df[df['Sex'] == 'male'].groupby('Pclass')['First_Name'].value_counts().groupby('Pclass').head(1)
female_popular_by_class = df[df['Sex'] == 'female'].groupby('Pclass')['First_Name'].value_counts().groupby('Pclass').head(1)

print(f'Самые популярные мужские имена по классу:\n{male_popular_by_class}')
print(f'\nСамые популярные женские имена по классу:\n{female_popular_by_class}')

#Passengers over 44 years of age
print(f'\nПассажиры, возраст которых больше 44 лет:\n{df[df['Age'] > 44]}')


#Passengers over 44 years of age and male
df_more_44_age = df[(df['Age'] > 44) & (df['Sex'] == 'male')]
print(f'\nПассажиры, возраст которых больше 44 лет и мужчины:\n{df_more_44_age}')

#Number of n-seater cabins
df_cabin_value_counts = df['Cabin'].value_counts()
df_cabin_value_counts = df_cabin_value_counts[df_cabin_value_counts > 1]
print(f'\nКоличества n-местных кабин:\n{df_cabin_value_counts.value_counts()}')