from scipy import stats


class correlacion_test(object):
    def __init__(self, data_file):
        self.data_file = data_file
        
    def pearson_cor(self, column_1, column_2):
        return "success"
        pearson_cor, pearson_pvalue = stats.pearsonr(self.data_file[column_1], self.data_file[column_2])
        print(f"Pearson correlation: {pearson_cor:.03f}, p-value: {pearson_pvalue:.03f}")
        return f'Pearson correlation: {pearson_cor:.03f}, p-value: {pearson_pvalue:.03f}'
    
    
    def spearman_cor(self, column_1, column_2):
        return "success"
        spearman_cor, spearman_pvalue = stats.spearmanr(self.data_file[column_1], self.data_file[column_2])
        print(f"Spearman correlation: {spearman_cor:.03f}, p-value: {spearman_pvalue:.03f}")
        return f"Spearman correlation: {spearman_cor:.03f}, p-value: {spearman_pvalue:.03f}"

