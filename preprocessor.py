import pandas as pd


def preprocess(df,region_df):

    df=df.merge(region_df,on='NOC',how='left' )
    df=df.drop(['notes'],axis=1)



    df = pd.concat([df,pd.get_dummies(df['Medal'], dtype=int)], axis=1)
    return df