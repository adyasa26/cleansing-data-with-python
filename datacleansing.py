import pandas as pd 
import numpy as np 
from itertools import groupby
import editdistance

kota = ['jaka barat','slo',None,'jakratatimr','mlang','bndng','bgr',None,'smrang','srubaya']
refrensi = ['jakarta barat','bogor','malang','jakarta timur','bandung','semarang','solo','surabaya']
provinsi = ['dki jakarta','jawa tengah','jawa barat','dki jakarta','jawa timur','jawa barat','jawa barat','dki jakarta','jawa tengah','jawa timur']

# mengisi data yang kosong base on provinsi

kota_provinsi = {'Kota' : kota,'Provinsi' : provinsi}
data_frame = pd.DataFrame(kota_provinsi)
data = data_frame['Kota'].groupby(data_frame['Provinsi']).fillna(method='ffill')
data2 = data.groupby(data_frame['Provinsi']).fillna(method='bfill')

#print data bersih 1 (no missing data)

dlist = data2.tolist()
print '============ data kotor : typo dan missing data ============'
print kota
print '============ data bersih 1 : no missing data ============'
print dlist

#print data bersih 1 (no typo data)

print '============== data bersih 2 : no typo data ============='

# membenarkan data yang typo

dataa = 0
loops = len(dlist)
while dataa < loops:
	nb = 0
	loopb = len(refrensi)
	totallist=[]
	while nb < loopb:
		slheksekusi = dlist[dataa]
		bnreksekusi = refrensi[nb]
		dist = editdistance.eval(slheksekusi,bnreksekusi)
		dist = int(dist)
		totallist.append([slheksekusi,bnreksekusi,dist])
		minimum = min(totallist, key=lambda x: x[2])
		nb = nb + 1
	print minimum[1]
	dataa = dataa + 1
	