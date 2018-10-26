- Case When xx Then xx Else xx End
```
def casewhen(series, cond, _then=0, _else=1):
    """cond = series == -1"""
    return series.mask(cond, _then).where(cond, _else)
```
