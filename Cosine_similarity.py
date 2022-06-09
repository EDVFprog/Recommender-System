# Cosine similarity of a data base
import math
import numpy as np
import pandas as pd # Import some useful libraries
df = pd.DataFrame(np.random.randint(-1,9,size=(8, 8)), columns=list('12345678'),index=['1', '2','3','4','5','6','7','8'])# making a data set in a range of -1 to 8
#That means the user id and the item id and the scores for each one
df[df==-1]=np.nan # here I did a substitution... for each -1 we interprete this data as Nan
print(df)
#Print so we can visualize the data
# Now I wanted to do a cossine correlation function
def CosineCorr(df,u,v):
    """ These function use the formula for similarity based on the cosine to determinate
    the similarity of a user u to another user v."""
    lenght=len(df.index)
    print(lenght)
    U=[]
    V=[]
    U_sq=[]
    V_sq=[]
    Numerator_list=[]
    for i in range(0,lenght):
        rate_u=df.iloc[u-1][i]
        rate_v=df.iloc[v-1][i]
        if np.isnan(rate_u) or np.isnan(rate_v):
            print('Missing data')
        else:
            U.append(rate_u)
            V.append(rate_v)
            numerator=rate_u*rate_v
            Numerator_list.append(numerator)
    for i in range(0,len(U)):
        U_square_rate=U[i]**2
        V_square_rate=V[i]**2
        U_sq.append(U_square_rate)
        V_sq.append(V_square_rate)
    print(Numerator_list)
    print(U)
    print(U_sq)
    Sum_sq_u=sum(U_sq)
    Sum_sq_v=sum(V_sq)
    Sum_num=sum(Numerator_list)
    print(Sum_sq_u)
    print(Sum_sq_v)
    print(Sum_num)
    Cosine=Sum_num/(math.sqrt(Sum_sq_u)*math.sqrt(Sum_sq_v))
    return Cosine

