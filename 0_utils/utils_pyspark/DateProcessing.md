```python
class DateProcessing(object):
    
    def __init__(self, df, date_col):
        self.df = df
        self.col = col(date_col)
    
    def time_delta(self):
        return df.select('*', dayofweek(self.col), month(self.col), dayofmonth(self.col), hour(self.col), minute(self.col), second(self.col))
```
