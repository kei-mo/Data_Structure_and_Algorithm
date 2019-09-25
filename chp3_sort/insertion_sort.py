

# %%
import numpy as np 

#%% 
# Inserton sort
# 計算量: O(N^2) 降順で並んでいた場合、計算量が最大となりO(N^2)となる
# 
def insertion_sort(a,n):
    # a: list of number
    # n: length of list a
    for i in range(n):
        v = a[i] # 未ソート部分の先頭
        j = i - 1
        while j>=0 and a[j]>v: # 挿入部分が見つかるまで繰り返す
            a[j+1] = a[j]      # a[j]がvより大きい場合、a[j]をa[j+1]に移動
            j -= 1
        a[j+1] = v             # 挿入
    return a


#%%
n = 20
a = np.random.randint(0,100,n)

a_sorted = insertion_sort(a,n)
print(a_sorted)
