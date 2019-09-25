

# %%
import numpy as np 

#%% 
# Bubble sort
# 計算量: O(N^2)
# 要素が同じだった場合入れ変わることのない安定なソート
def bubble_sort(a,n):
    # a: list of number
    # n: length of list a
    k = 0      # 交換回数
    
    for i in range(n):
        for j in range(1,n)[::-1]:  
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1].copy(),a[j].copy()
                k += 1
    return a, k

#%%
n = 10
a  = np.random.randint(0,100,n)

a_sorted, i = bubble_sort(a,n)
print(a_sorted)



#%%


#%%
