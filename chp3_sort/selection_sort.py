

# %%
import numpy as np 
import time

#%% 
# Selection sort
# 計算量: O(N^2)
def selection_sort(a,n):
    # a: list of number
    # n: length of list a
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx], a[i]
    return a

#%%
n = 40
a  = np.random.randint(0,100,n)

start = time.time()
a_sorted = selection_sort(a,n)
process_time = time.time() - start

print(a_sorted)
print(process_time)



#%%


#%%
