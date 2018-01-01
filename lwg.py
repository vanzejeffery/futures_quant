import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = "http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=RB0"

req = requests.get(url)
LWG=eval(req.text)
df_lwg=pd.DataFrame(LWG)
df_lwg.columns=[['date','open','high','low','close','volume']]
df_lwg.index=df_lwg['date'].tolist()
df_lwg=df_lwg.drop('date',1)
df_lwg=df_lwg.astype('float')
df_lwg['Log_Ret']=np.log(df_lwg['close']/df_lwg['close'].shift(1))
df_lwg['Volatility']=pd.rolling_std(df_lwg['Log_Ret'],window=252)*np.sqrt(252)

ddaa=df_lwg.index.tolist()
df_lwg['year']=[x[0:4] for x in df_lwg.index.tolist()]
df_lwg['month']=[x[5:7] for x in df_lwg.index.tolist()]