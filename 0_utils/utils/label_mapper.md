```python
def label_encoding(labels):
    # from collections import defaultdict
    # label2idx = defaultdict(int)
    label2idx = {}
    for i in labels:
        if i not in label2idx:
            label2idx[i] = len(label2idx)
    idx2label = {v: k for k, v in label2idx.items()}
    return label2idx, idx2label
```
