import dask.dataframe as dd
from dask.multiprocessing import get
from tqdm import tqdm

tqdm.pandas(desc='prep')


class MultiApply(object):
    def __init__(self, pandas_df):
        self.ddf = dd.from_pandas(pandas_df, 32)

    def apply(self, func):
        """
        :param func: lambda df: df['xx'].progress_apply(func_)
        :return: pd.DataFrame
        """
        return self.ddf.map_partitions(func).compute(get=get)
