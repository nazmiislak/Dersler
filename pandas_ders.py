import pandas as pd

seri_2=pd.Series( [175,160,180,182,162],index=['Ahmet','Ali','Ayşe','Melis','Ela'])
print(seri_2)

seri_2.index = ['Sıra_1','Sıra_2','Sıra_3','Sıra_4','Sıra_5']
print(seri_2)

#index olarak öğrenci numaralarının son 4 hanesi ve değer olarak da vize notlarını içeren bir seri yazın
#5 öğrenciyi temsil etsin

vize_notlari=pd.Series([25,65,40,76,86],index=['Efe','Nazmi','Ömer','Emin','Ali'])
print(vize_notlari)

vize_notlari.index=['3024','3001','3026','3019','3045']
print(vize_notlari)