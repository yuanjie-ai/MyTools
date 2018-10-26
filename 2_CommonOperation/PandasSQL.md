- Case When xx Then xx Else xx End
```
t = s < 3
s.mask(t, 0).where(t, 1)
```
