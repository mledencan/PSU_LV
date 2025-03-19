
import pandas as pd

mtcars = pd.read_csv('mtcars.csv')

najveca_potrosnja = mtcars.sort_values(by='mpg', ascending=False).head(5)
print(mtcars)
print("5 automobila s najvećom potrošnjom:")
print(najveca_potrosnja[['car', 'mpg']])

osam_cilindara = mtcars[mtcars['cyl'] == 8]
tri_najmanja_potrosnja = osam_cilindara.sort_values(by='mpg').head(3)
print("\nTri automobila s 8 cilindara koji imaju najmanju potrošnju:")
print(tri_najmanja_potrosnja[['car', 'mpg']])

sest_cilindara = mtcars[mtcars['cyl'] == 6]
srednja_potrosnja = sest_cilindara['mpg'].mean()
print("\nSrednja potrošnja automobila sa 6 cilindara:", srednja_potrosnja)

automobili_cetiri_cilindra = mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] >= 2000/1000) & (mtcars['wt'] <= 2200/1000)]
srednja_potrosnja_cetiri_cilindra = automobili_cetiri_cilindra['mpg'].mean()
print("\nSrednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs:", srednja_potrosnja)

broj_am = mtcars['am'].value_counts()
print("\nBroj automobila s ručnim i automatskim mjenjačem:")
print(broj_am)

automatski_preko_100 = mtcars[(mtcars['am'] == 0) & (mtcars['hp'] > 100)]
brojac_automatski_preko_100 = len(automatski_preko_100)
print("\nBroj automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga:", brojac_automatski_preko_100)

mtcars['mass_kg'] = mtcars['wt'] * 1000
print("\nMasa svakog automobila u kilogramima:")
print(mtcars[['car', 'mass_kg']])