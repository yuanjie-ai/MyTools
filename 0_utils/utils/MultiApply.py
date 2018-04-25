import dask.dataframe as dd
from dask.multiprocessing import get
from tqdm import tqdm

tqdm.pandas(desc='prep')


class MultiApply(object):

    def __init__(self, pandas_df):
        self.ddf = dd.from_pandas(pandas_df, 32)
        
    def run(self, func=lambda df: df['xx'].progress_apply(lambda: 1)):
        return self.ddf.map_partitions(func).compute(get=get)

