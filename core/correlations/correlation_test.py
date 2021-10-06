from scipy import stats

def pearson_cor(column_1, column_2):
    pearson_cor, pearson_pvalue = stats.pearsonr(column_1, column_2)
    print(f"Pearson correlation: {pearson_cor:.03f}, p-value: {pearson_pvalue:.03f}")


def spearman_cor(column_1, column_2):
    spearman_cor, spearman_pvalue = stats.spearmanr(column_1, column_2)
    print(f"Spearman correlation: {spearman_cor:.03f}, p-value: {spearman_pvalue:.03f}")
