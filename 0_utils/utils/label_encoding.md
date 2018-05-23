```python
def label_encoding(seq):
    # from collections import defaultdict
    # label2idx = defaultdict(int)
    label2idx = {}
    for i in seq:
        if i not in label2idx:
            label2idx[i] = len(label2idx)
    idx2label = {v: k for k, v in label2idx.items()}
    return label2idx, idx2label
```
