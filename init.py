import MergeSorts as ms 
import QuickSorts as qs 
import TimSorts as ts 
import Threeway as tw
import numpy as np
import time

if __name__ == "__main__":
    smaller_list = list(np.random.randint(1, 100, 20))
    small_list = list(np.random.randint(1, 1000, 1000))
    median_list = list(np.random.randint(1, 1000, 10000))
    big_list = list(np.random.randint(1, 10000, 100000))
    start = time.time()
    # sort here
    # ts.timSortBinary(big_list)

    ts.timSortPatience(big_list)
    
    end = time.time()
    print('elapsed tiem: '+ str(end - start))

#
