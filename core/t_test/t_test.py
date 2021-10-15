import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import ttest_1samp

class t_test(object):
    def __init__(self, data_file):
        self.data_file = data_file
        
        
    # ------------- Function for insert data for one sample T test ------------- #
    def random_data_sample(self, sample_size, column_1):
        return self.data_file[column_1].sample(n=sample_size)
    
    
    # ------------- Function for one sample T test ------------- #
    def one_sample_t_test(self, sample_size, column_1):
        random_data_sample = self.random_data_sample(sample_size, column_1)
        #print(random_data_sample)
        df = pd.DataFrame(random_data_sample)
        t_statictic = ttest_1samp(random_data_sample,  df.mean()[0])
        #print(f"Test statistic: {t_statictic[0]:.03f}, p-value: {t_statictic[1]:.03f}")
        return t_statictic
        
          
    # ------------- Function for paired t test with two samples ------------- #
    def paired_t_test(self, column_1, column_2):
        t_statictic = stats.ttest_ind(a = self.data_file[column_1], b = self.data_file[column_2])
        print(f"Test statistic: {t_statictic[0]:.03f}, p-value: {t_statictic[1]:.03f}")
        alpha = 0.05
        
        if t_statictic.pvalue > alpha:
            print("The alternate hypothesis is rejected and the null hypothesis is taken. The two groups are the same")
        else:
            print("The null hypothesis is rejected and the alternate hypothesis is taken. The two groups are different")
        
        return t_statictic
            


#r = t_test("")
#r.one_sample_t_test(10)