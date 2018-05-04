```python
def skmodel_save(skmodel, path=None):
    from datetime import datetime
    from sklearn.externals import joblib
    dt, model_name = str(datetime.datetime.today())[:22], skmodel.__str__()
    if path:
        joblib.dump(skmodel, '%s/%s___%s.model' % (path, dt, model_name))
    else:
        joblib.dump(skmodel, './%s___%s.model' % (dt, model_name))
```
