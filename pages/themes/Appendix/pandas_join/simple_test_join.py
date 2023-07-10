import pandas as pd
from IPython.display import display
from IPython.display import Image


tableA_raw = {
  'tac': [1,2,3],
  'a': ["a1","a2","a3"],
}
dfA = pd.DataFrame(tableA_raw, columns = ['tac', 'a'])
dfA

tableB_raw = {
  'tac': [3,4,5],
  'b': ["b3","b4","b5"],
}
dfB = pd.DataFrame(tableB_raw, columns = ['tac', 'b'])
dfB

# by index:
dfNew = dfA.join(dfB,on='tac',how="left", lsuffix='_caller', rsuffix='_other')

# left outer by column:
dfNew = dfA.set_index('tac').join(dfB,on='tac',how="left", lsuffix='_caller', rsuffix='_other')
# dfNew = pd.merge(dfA, dfB, on='tac', how='left')
dfNew
