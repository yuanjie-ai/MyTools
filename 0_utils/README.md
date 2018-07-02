# :rocket: 常用 :facepunch:
---
- 常用import
```python
import warnings
import tqdm
warnings.filterwarnings('ignore')


import numpy as np
import pandas as pd


from keras.layers import Dropout, Dense, Embedding, Flatten, GRU, Input, LSTM, Lambda
from keras.models import K, Input, Model, Sequential, load_model
from keras.optimizers import Adam
from keras.regularizers import l1, l2, l1_l2
```

---
https://mp.weixin.qq.com/s/yja52WLIekZSRLR24s6qGg

```python
import numpy as np
from scipy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
def jaccard_similarity(s1, s2):
    """
    计算两个句子的雅可比相似度
    """
    vectorizer = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = vectorizer.fit_transform(corpus).toarray()
    numerator = np.sum(np.min(vectors, axis=0))
    denominator = np.sum(np.max(vectors, axis=0))
    return numerator/denominator
```
---

