```python
def skmodel_save(skmodel, path=None):
    from datetime import datetime
    from sklearn.externals import joblib
    if path:
        joblib.dump(skmodel, '%s/%s___%s.model' % (path, str(datetime.datetime.today())[:22], skmodel.__str__()))
    else:
        joblib.dump(skmodel, './%s___%s.model' % (str(datetime.today())[:22], skmodel.__str__()))
```
