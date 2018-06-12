```python
def result_scaling(x=0.37, rate_train_true=0.37, rate_test_true=0.165):
    """适用于线上线下样本分布不一致"""
    a = rate_test_true/rate_train_true
    b = (1 - rate_test_true)/(1 - rate_train_true)
    scale_pos_weight = a/b
    print("Xgb/Lgb scale_pos_weight: %s" %scale_pos_weight)
    return a * x / (a * x + b * (1-x))
```

---
Refer:

https://www.kaggle.com/c/quora-question-pairs/discussion/31179

https://www.kaggle.com/badat0202/estimate-distribution-of-data-in-lb
