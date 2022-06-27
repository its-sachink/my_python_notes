# you can write to stdout for debugging purposes, e.g.  
# print("this is a debug message")  

```python
def insert_five(position, number):
    str_number = str(number)
    insert_five_number = " ".join(str_number)
    insert_five_number.insert(position, "5")
    return insert_five_number



def solution(N):
    num_length = str(int(N)).len()
    max = N
    tmp_max = 0
    for num in range(num_length):
        tmp_max = insert_five(num, N)
        if tmp_max > max:
            max = tmp_max

    return max
```
