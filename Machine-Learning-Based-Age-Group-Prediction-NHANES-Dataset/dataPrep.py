def dataPreperation(df):
  df = df.fillna(df.mean())
  for col in df.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df2 = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    if(len(df2['TenYearCHD'].unique()) == 1):
      df2 = df
    else:
      df = df2		
  if (df2.duplicated().sum() >0):
    df2 = df2.drop_duplicates()
  return df2