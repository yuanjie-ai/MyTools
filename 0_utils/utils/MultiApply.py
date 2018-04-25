import dask.dataframe as dd
from dask.multiprocessing import get
from tqdm import tqdm

tqdm.pandas(desc='prep')


class MultiApply(object):

    def __init__(self, pandas_df):
        self.pandas_df = pandas_df

    def multiApply(self, func=lambda df: df['xx'].progress_apply(lambda: 1)):
        return self.ddf.map_partitions(func).compute(get=get)

    @property
    def ddf(self):
        return dd.from_pandas(self.pandas_df, 32)
