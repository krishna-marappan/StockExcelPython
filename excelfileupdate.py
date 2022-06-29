import pandas as pd
import os
import glob
import data
import csv
count = 0
os.chdir(data.lisfofstock)
stockfiles = glob.glob(os.path.join(os.getcwd(), "*.csv"))
for stockpath in stockfiles:
  Data = pd.read_csv(stockpath)
  allvalues = pd.DataFrame(Data)
  closeprice = allvalues['Close Price'].values.tolist()
  length = int((len(closeprice))/20) * 20
  print(length)
  malist = []
  macmplist = []
  j = -20
  k = -1
  for i in range(1,length):
      value = sum(closeprice[:j:k])
      print(closeprice[:j:k])
      print(j,k,value,i)
      j -= 1
      k -= 1

