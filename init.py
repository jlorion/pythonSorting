import MergeSorts as ms 
import QuickSorts as qs 
import TimSorts as ts 
import Threeway as tw
import numpy as np
import time
from ucimlrepo import fetch_ucirepo
import json
import pandas as pd

if __name__ == "__main__":

    data_file = open("yelp\\yelp_academic_dataset_business.json", encoding="utf8")
    data = []
    for line in data_file:
        data.append(json.loads(line))
    checkin_df = pd.DataFrame(data)
    data_file.close()
    yelpStars = list(checkin_df['stars'])
    print(yelpStars)


    # wineQual = fetch_ucirepo(id=186)
    # wineSortData = list(wineQual.data.features['citric_acid'].values)
    # smaller_list = list(np.random.randint(1, 100, 20))
    # small_list = list(np.random.randint(1, 1000, 1000))
    # median_list = list(np.random.randint(1, 1000, 10000))
    # big_list = list(np.random.randint(1, 10000, 100000))
    start = time.time()
    # sort here
    # qs.quickSortStable(wineSortData)
    
    end = time.time()
    print('elapsed tiem: '+ str(end - start))

#
