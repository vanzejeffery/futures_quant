import numpy as np
import pandas as pd
from sklearn.decomposition import KernelPCA
import tushare as ts
# 定义获取数据的时间段
start = "2014-01-01"
end = "2017-11-16"
symbols=ts.get_sz50s()['code'].tolist()
symbols.append('sz50')
data=pd.DataFrame()
for sym in symbols:
    www=ts.get_k_data(sym,start,end,autype='qfq')
    www['date'] = pd.to_datetime(www['date'])
    www.set_index("date", inplace=True)
    data[sym]=www['close']
dax=pd.DataFrame(data.pop('sz50'))
data=data.dropna(axis=1,how='any')
scale_function=lambda x:(x-x.mean())/x.std()
pca=KernelPCA().fit(data.apply(scale_function))
pca=KernelPCA(n_components=1).fit(data.apply(scale_function))
dax['PCA_1']=pca.transform(-data)
import matplotlib.pyplot as plt
%matplotlib inline
dax.apply(scale_function).plot(figsize=(20,10))

pca=KernelPCA(n_components=5).fit(data.apply(scale_function))
pca_components=pca.transform(-data)
weights=get_we(pca.lambdas_)
dax['PCA_5']=np.dot(pca_components,weights)
import matplotlib.pyplot as plt
%matplotlib inline
dax.apply(scale_function).plot(figsize=(20,10))
