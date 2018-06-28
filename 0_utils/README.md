# :rocket: 临时笔记 :facepunch:
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

