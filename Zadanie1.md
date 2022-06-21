```python
import numpy as np
```


```python
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
```


```python
print(a)
```

    [[ 1  6]
     [ 2  8]
     [ 3 11]
     [ 3 10]
     [ 1  7]]
    


```python
mean_a = a.mean(axis = 0)
```


```python
print(mean_a)
```

    [2.  8.4]
    

## Zadanie2


```python
a_centered = a - mean_a
```


```python
print(a_centered)
```

    [[-1.  -2.4]
     [ 0.  -0.4]
     [ 1.   2.6]
     [ 1.   1.6]
     [-1.  -1.4]]
    

# Zadanie3


```python
a_centered_sp = a_centered.T[0] @ a_centered.T[1]
```


```python
print(a_centered_sp)
```

    8.0
    


```python
a_centered_sp / (a_centered.shape[0] - 1)
```




    2.0




```python

```
