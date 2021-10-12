from scipy import stats


class correlacion_test(object):
    def __init__(self, data_file):
        self.data_file = data_file
        
    def pearson_cor(self, column_1, column_2):
        try:
            pearson_cor, pearson_pvalue = stats.pearsonr(self.data_file[column_1], self.data_file[column_2])
            return "Pearson Correlacion = %.3f, PValue = %.3f " % (pearson_cor, pearson_pvalue)
        except:
            return "Error El tipo de dato no es numerico."
    
    def spearman_cor(self, column_1, column_2):
        try:
            spearman_cor, spearman_pvalue = stats.spearmanr(self.data_file[column_1], self.data_file[column_2])
            return "Spearman Correlacion = %.3f, PValue = %.3f " % (spearman_cor, spearman_pvalue)
        except:
            return "Error El tipo de dato no es numerico."
