def getCorrelation(self, dataset):
    import pandas as pd
    corr = dataset.corr('pearson')['popularity']
    corr_sq = corr.pow(2)
    corr = pd.DataFrame({"variables": list(dataset.columns),
                         "corr_score": corr.to_numpy(),
                         "corr_sq": corr_sq.to_numpy()})
    corr = corr.sort_values(by=['corr_sq'], ascending=False)

    return pd.DataFrame({"variables": corr['variables'].to_numpy(),
                         "corr_score": corr['corr_score'].to_numpy()})