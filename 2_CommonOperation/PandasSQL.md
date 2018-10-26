- Case When xx Then xx Else xx End
```
def casewhen(cond, _then=0, _else=1):
    """cond = data.label == -1"""
    return data.label.mask(cond, _then).where(cond, _else)
```
