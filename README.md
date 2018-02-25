# Innovaccer_Analytics_Assignment

## Getting Started

These instructions will let you know about the project.

### Prerequisites
- csv
- numpy
- Levenshtein
- random

### How to run:

1. Directly run the python file.
```
$ python cluster_the_names.py
Prints the clusters with names.
```
2. Open the python shell and execute the below commands.
```
>> import csv
>> import numpy as np
>> import Levenshtein
>> from random import shuffle
>>
>> from cluster_the_names import read_data, is_name_matched, cluster_names
>> filename = 'Sample_Dataset.csv'
>> read_data(filename)  # Read data
>> cluster_names()      # Clusters all the names that are provided in the dataset.
Prints the clusters with names.
```
#### If you want to find whether two names are matching or not...
```
>> name_1 = 'Vladimir Frometa'
>> name_2 = 'Vladimir Frometa Garo'
>> is_name_matched(name_1, name_2)
True
