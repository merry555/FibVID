#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
df=pd.read_csv("final_dataset/origin_change/claim_propagation.csv")


claim=list(set(df['claim_number'].tolist()))
print("# of claims : ",len(claim))


# ### 1. Depth per tweets and per claims & Volume per claims


#dataframe per tweets
df_finals = pd.DataFrame(columns=df.columns)


#dataframe per claims
df_claim = pd.DataFrame(columns=['claim_number', 'num_origin','volume', 'max_depth'])  #anova


for i in range(len(claim)):
    claim_n=claim[i]
    temp_claim=df[df['claim_number'] == claim_n ]
    temp_claim=temp_claim.reset_index(drop=True)
    origin_tweets=[]  
    for i in range(len(temp_claim)):
        if np.isnan(temp_claim['parent_id'][i]) :
            origin_tweets.append(temp_claim['tweet_id'][i])

    origin_n=len(origin_tweets)
    
    depth=1
    temp_claim["depth"]=0

    while list(temp_claim['depth']).count(0)!= origin_n:
        temp=[]
        for origin in origin_tweets:
            indexes=temp_claim.index[temp_claim['parent_id'] == origin].tolist()
            temp_claim.loc[indexes,'depth'] = depth
            temp=temp +temp_claim.tweet_id[temp_claim['parent_id'] == origin].tolist()
        origin_tweets=temp
        depth+=1
    df_finals=pd.concat([df_finals, temp_claim])
    df_claim.loc[len(df_claim)]=[claim_n, origin_n, len(temp_claim), temp_claim.depth.max()]    


# ### 2. Virality per claims

import numpy as np

df_claim["virality"]=0

for i in range(len(claim)):
    claim_n=claim[i]
    temp_claim=df_finals[df_finals['claim_number'] == claim_n ]
    temp_claim=temp_claim.reset_index(drop=True)
    
    
    all_lists=list(set(list(temp_claim["parent_id"].unique())+list(temp_claim["tweet_id"].unique())))
    all_lists.remove(0)
    A = np.zeros((len(all_lists),len(all_lists)))
    df_matrix = pd.DataFrame(A, index=all_lists, columns=all_lists)
    for i in range(len(temp_claim)):
        if temp_claim["parent_id"][i]!=0:
            df_matrix.loc[temp_claim["tweet_id"][i], temp_claim["parent_id"][i]]=1
    matrix=df_matrix.values
    
    virality=0
    length=0
    depth=0

    while depth!=temp_claim.depth.max():
        virality+=(np.count_nonzero(matrix == 1)*(depth+1))
        matrix=np.matmul(matrix,matrix)
        depth+=1
    
    if len(all_lists)>2:
        df_claim.virality[df_claim.index[df_claim['claim_number'] == claim_n]] =  virality/(len(all_lists)*(len(all_lists)-1)/2)