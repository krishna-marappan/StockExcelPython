import pandas as pd
def MA_20_Calculation(stockpath, row):
    Data = pd.read_csv(stockpath)
    commonstocklist = pd.DataFrame(Data)
    product = commonstocklist['Close Price'].values.tolist()
    product.append(float(row[8]))
    value = sum(product[-20::])
    ma_20 = value/20
    print(ma_20)
    if ma_20 > product[-1]:
        res = "True"
    else:
        res = "False"
    row.append(ma_20)
    row.append(res)
    return row



