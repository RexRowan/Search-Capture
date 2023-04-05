# Search-Capture
Python module for searching common interests in suspects lists

```
from common_words import find_common_words

list1 = ['John', 'Alex', 'Carol', 'Jason']
list2 = ['Alex', 'Jason', 'Joe', 'Linda']
list3 = ['Jason', 'Justin', 'Joe', 'Linda']

common_words = find_common_words(list1, list2, list3)
print(common_words)  # Output: ['Jason']
```
