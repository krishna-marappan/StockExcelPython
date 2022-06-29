import pandas as pds
import os
import glob
import data
import csv
import MA_Calculation

count = 0
newData = pds.read_csv(data.bhavfile)
commonstocklist = newData['SYMBOL']
os.chdir(data.lisfofstock)
stockfiles = glob.glob(os.path.join(os.getcwd(), "*.csv"))
for stockpath in stockfiles:
     j = stockpath.split("\\")[-1]
     stockname = j.split(".")[0]
     print(stockname)
     #column = commonstocklist[commonstocklist == stockname].index[0]
     with open(data.bhavfile) as file_obj:
          reader_obj = csv.reader(file_obj)
          for row in reader_obj:
               if row[0] == stockname:
                    break
     print(row)
     lis = MA_Calculation.MA_20_Calculation(stockpath, row)
     with open(stockpath, "a", newline="") as file_obj1:
          writer_obj = csv.writer(file_obj1)
          writer_obj.writerow(row)
     file_obj1.close()
