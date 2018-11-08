```
def hive_agg_desc(column: str):
    """
    mad skew kurt ...
    """
    expr = f"""
            AVG({column}) AS {column}_mean,
            MAX({column}) AS {column}_max,
            MIN({column}) AS {column}_min,
            MAX({column}) - MIN({column}) AS {column}_r,
            STDDEV_SAMP({column}) AS {column}_std,
            PERCENTILE({column}, 0.25) AS {column}_per25,
            PERCENTILE({column}, 0.5) AS {column}_per50,
            PERCENTILE({column}, 0.75) AS {column}_per75,
            PERCENTILE({column}, 0.75) - PERCENTILE({column}, 0.25) AS {column}_iqr,
            STDDEV_SAMP({column}) / (AVG({column}) + pow(10, -8)) AS {column}_cv,
            COUNT(CASE WHEN {column} = 0 THEN 1 ELSE NULL END) AS {column}_zeros_num
            COUNT(CASE WHEN {column} = 0 THEN 1 ELSE NULL END) / COUNT(1) AS {column}_zeros_perc
            """
    return expr
```
