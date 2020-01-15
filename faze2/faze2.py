import pandas as pd
from Reader import Readcsv as rc
df2=rc.ownershipDF.loc[(df['date']>='2018-00-00') & (df['date']<='2020-00-00')]

