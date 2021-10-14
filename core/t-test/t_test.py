import pandas as pd
import scipy.stats as stats
from scipy.stats import ttest_1samp

class t_test(object):
    def __init__(self, data_file):
        self.data_file = data_file
        
        
    # ------------- Function for insert data for one sample T test ------------- #
    def insert_data(self):
        sample_data = []
        sample_size = int(input('Enter the samples size: '))
        
        for element in range(1, sample_size, 1):
            data = int(input('Enter data: '))
            sample_data.append(data)
            
        print(sample_data)
        return sample_data
    
    
    # ------------- Function for one sample T test ------------- #
    def one_sample_t_test(self, sample_size, sample_data):
        df = pd.DataFrame(sample_data)
        t_statictic = ttest_1samp(sample_data,  df.mean()[0])
        print(f"Test statistic: {t_statictic[0]:.03f}, p-value: {t_statictic[1]:.03f}")
        
          
    # ------------- Function for paired t test with two samples ------------- #
    def paired_t_test(self, column_1, column_2):
        t_statictic = stats.ttest_ind(a = column_1, b = column_2)
        print(f"Test statistic: {t_statictic[0]:.03f}, p-value: {t_statictic[1]:.03f}")
        alpha = 0.05
        
        if t_statictic.pvalue > alpha:
            print("The alternate hypothesis is rejected and the null hypothesis is taken. The two groups are the same")
        else:
            print("The null hypothesis is rejected and the alternate hypothesis is taken. The two groups are different")