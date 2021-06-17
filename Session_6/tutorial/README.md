# 1. Numpy
Numpy is a Python library for computationally efficient multidimensional array operations aimed primarily at scientific computing. It is accepted to import as follows:


```python
import numpy as np
```


```python
a = np.array([0, 1, 2, 3]) 
a
```




    array([0, 1, 2, 3])



Let's compare effectivity with Numpy and without:


```python
L = range(1000)
L # from 0 to 999, can use list(L) to get result as a list
```




    range(0, 1000)




```python
%timeit [i**2 for i in L]
```

    308 µs ± 14.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    


```python
a = np.arange(1000)
a
```




    array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
            13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
            26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
            39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
            52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
            65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
            78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
            91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
           104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
           117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
           130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
           143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
           156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
           169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
           182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
           195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
           208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
           221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
           234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
           247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259,
           260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272,
           273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285,
           286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298,
           299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
           312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324,
           325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337,
           338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350,
           351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363,
           364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376,
           377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389,
           390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402,
           403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415,
           416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428,
           429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441,
           442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454,
           455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467,
           468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480,
           481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493,
           494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506,
           507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519,
           520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532,
           533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545,
           546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558,
           559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571,
           572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584,
           585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597,
           598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610,
           611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623,
           624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636,
           637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649,
           650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662,
           663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675,
           676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688,
           689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701,
           702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714,
           715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727,
           728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740,
           741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753,
           754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766,
           767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779,
           780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792,
           793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805,
           806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818,
           819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831,
           832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844,
           845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857,
           858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870,
           871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883,
           884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896,
           897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909,
           910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922,
           923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935,
           936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948,
           949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961,
           962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974,
           975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987,
           988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999])




```python
%timeit a**2
```

    2.13 µs ± 199 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    


## Arrays creation

* **1-D**:



```python
a = np.array([0, 1, 2, 3])
a
```




    array([0, 1, 2, 3])




```python
a.ndim
```
    1



```python
a.shape
```




    (4,)




```python
len(a)
```




    4



* **2-D**:



```python
b = np.array([[0, 1, 2], [3, 4, 5]])  # 2 x 3 array
b
```




    array([[0, 1, 2],
           [3, 4, 5]])




```python
b.ndim
```




    2




```python
b.shape # (rows, columns)
```




    (2, 3)




```python
len(b)  # number of rows
```




    2



- evenly spaced elements:


```python
a = np.arange(10)  # 0 .. n-1 
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
b = np.arange(1, 9, 2)  # start, end (not encluding), step
b
```




    array([1, 3, 5, 7])



- by number of elements:



```python
c = np.linspace(0, 1, 6)  # start, end, amount
c
```




    array([0. , 0.2, 0.4, 0.6, 0.8, 1. ])




```python
d = np.linspace(0, 1, 5, endpoint=False)
d
```




    array([0. , 0.2, 0.4, 0.6, 0.8])



- Widely used arrays:



```python
a = np.ones((3, 3))  # (3, 3) - tuple ('кортеж' - immutable data type (as opposed to a list))
a
```




    array([[1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.]])




```python
b = np.zeros((2, 2))
b
```




    array([[0., 0.],
           [0., 0.]])




```python
c = np.eye(3)
c
```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])




```python
d = np.diag(np.array([1, 2, 3, 4]))
d
```




    array([[1, 0, 0, 0],
           [0, 2, 0, 0],
           [0, 0, 3, 0],
           [0, 0, 0, 4]])



* `np.random` random numbers generation:


```python
a = np.random.rand(4)  # creates an array of specified shape and fills it with random values
a
```




    array([0.50755507, 0.0211933 , 0.43352176, 0.44631306])




```python
b = np.random.randn(4)  # “normal” (Gaussian) distribution of mean 0 and variance 1
b
```




    array([ 0.65034618, -0.51433646,  0.53942869,  1.52676162])




```python
np.random.seed(1234)  # seed - defines the internal state of the generator
```

## Array Indexing and Slicing


```python
a = np.arange(10)
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a[0], a[2], a[-1]
```




    (0, 2, 9)



Multidimensional arrays:



```python
a = np.diag(np.arange(3))
a
```




    array([[0, 0, 0],
           [0, 1, 0],
           [0, 0, 2]])




```python
a[1, 1]
```




    1




```python
a[2, 1] = 10  # 3 row, 2 column
a
```




    array([[ 0,  0,  0],
           [ 0,  1,  0],
           [ 0, 10,  2]])




```python
a[1]
```




    array([0, 1, 0])



**Slices**


```python
a = np.arange(10)
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a[2:9:3]  # [start:end:step]
```




    array([2, 5, 8])




```python
a[:4]
```




    array([0, 1, 2, 3])



By default \`start\` -  0,
\`end\` - last index, \`step\` - 1:



```python
a[1:3]
```




    array([1, 2])




```python
a[::2]
```




    array([0, 2, 4, 6, 8])




```python
a[3:]
```




    array([3, 4, 5, 6, 7, 8, 9])



# 2. Pandas
Pandas is a Python library that provides extensive means for data analysis. Data scientists often work with data stored in table formats like .csv, .tsv, or .xlsx. Pandas makes it very convenient to load, process, and analyze such tabular data using SQL-like queries. In conjunction with Matplotlib and Seaborn, Pandas provides a wide range of opportunities for visual analysis of tabular data.

The main data structures in Pandas are implemented with Series and DataFrame classes. The former is a one-dimensional indexed array of some fixed data type. The latter is a two-dimensional data structure - a table - where each column contains data of the same type. You can see it as a dictionary of Series instances. DataFrames are great for representing real data: rows correspond to instances (examples, observations, etc.), and columns correspond to features of these instances.


```python
import pandas as pd
```

## General info

### Series

** Series object creation**


```python
salaries = pd.Series([400, 300, 200, 250], index=["Andrey", "Kate", "Anton", "Alex"])
print(salaries)
```

    Andrey    400
    Kate      300
    Anton     200
    Alex      250
    dtype: int64
    


```python
salaries[salaries > 250]
```




    Andrey    400
    Kate      300
    dtype: int64



**Indexation can be as s.Name or s['Name'].**


```python
print(salaries.Andrey == salaries["Andrey"])
```

    True
    


```python
salaries["Oli"] = np.nan
```


```python
salaries
```




    Andrey    400.0
    Kate      300.0
    Anton     200.0
    Alex      250.0
    Oli         NaN
    dtype: float64




```python
salaries.fillna(salaries.min(), inplace=True) # fill the gaps with min value
```


```python
salaries
```




    Andrey    400.0
    Kate      300.0
    Anton     200.0
    Alex      250.0
    Oli       200.0
    dtype: float64



**Series objects are similar to ndarray and can be passed as arguments to most Numpy functions**


```python
print("The second element is", salaries[1], "\n") #start from 0
print(salaries[:3], "\n") # from index 0 to 2 
print("There are", len(salaries[salaries > 0]), "positive elements\n")
print(np.exp(salaries)) # exponent
```

    The second element is 300.0 
    
    Andrey    400.0
    Kate      300.0
    Anton     200.0
    dtype: float64 
    
    There are 5 positive elements
    
    Andrey    5.221470e+173
    Kate      1.942426e+130
    Anton      7.225974e+86
    Alex      3.746455e+108
    Oli        7.225974e+86
    dtype: float64
    

### DataFrame

**Such object can be created from a numpy array by specifying the row and column names.**


```python
df1 = pd.DataFrame(
    np.random.randn(5, 3),
    index=["o1", "o2", "o3", "o4", "o5"],
    columns=["f1", "f2", "f3"],
)
df1
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f1</th>
      <th>f2</th>
      <th>f3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>o1</th>
      <td>0.471435</td>
      <td>-1.190976</td>
      <td>1.432707</td>
    </tr>
    <tr>
      <th>o2</th>
      <td>-0.312652</td>
      <td>-0.720589</td>
      <td>0.887163</td>
    </tr>
    <tr>
      <th>o3</th>
      <td>0.859588</td>
      <td>-0.636524</td>
      <td>0.015696</td>
    </tr>
    <tr>
      <th>o4</th>
      <td>-2.242685</td>
      <td>1.150036</td>
      <td>0.991946</td>
    </tr>
    <tr>
      <th>o5</th>
      <td>0.953324</td>
      <td>-2.021255</td>
      <td>-0.334077</td>
    </tr>
  </tbody>
</table>
</div>



**Alternative way**


```python
df2 = pd.DataFrame(
    {"A": np.random.random(5), "B": ["a", "b", "c", "d", "e"], "C": np.arange(5) > 2}
)
df2
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.772827</td>
      <td>a</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.882641</td>
      <td>b</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.364886</td>
      <td>c</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.615396</td>
      <td>d</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.075381</td>
      <td>e</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



**Referring to elements:**


```python
print("Position (3,B) =", df2.at[3, "B"], "\n")
print(df2.loc[[1, 4], ["A", "B"]])
```

    Position (3,B) = d 
    
              A  B
    1  0.882641  b
    4  0.075381  e
    

**Change of the elements:**


```python
df2.at[2, "B"] = "f"
df2
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.772827</td>
      <td>a</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.882641</td>
      <td>b</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.364886</td>
      <td>f</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.615396</td>
      <td>d</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.075381</td>
      <td>e</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc[5] = [3.1415, "c", False]
df2
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.772827</td>
      <td>a</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.882641</td>
      <td>b</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.364886</td>
      <td>f</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.615396</td>
      <td>d</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.075381</td>
      <td>e</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.141500</td>
      <td>c</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



#### Handling missing values


```python
df1.at["o2", "A"] = np.nan
df1.at["o4", "C"] = np.nan
df1
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f1</th>
      <th>f2</th>
      <th>f3</th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>o1</th>
      <td>0.471435</td>
      <td>-1.190976</td>
      <td>1.432707</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>o2</th>
      <td>-0.312652</td>
      <td>-0.720589</td>
      <td>0.887163</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>o3</th>
      <td>0.859588</td>
      <td>-0.636524</td>
      <td>0.015696</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>o4</th>
      <td>-2.242685</td>
      <td>1.150036</td>
      <td>0.991946</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>o5</th>
      <td>0.953324</td>
      <td>-2.021255</td>
      <td>-0.334077</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



**Gaps can be replaced with some value.**


```python
df1.fillna(0)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>f1</th>
      <th>f2</th>
      <th>f3</th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>o1</th>
      <td>0.471435</td>
      <td>-1.190976</td>
      <td>1.432707</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>o2</th>
      <td>-0.312652</td>
      <td>-0.720589</td>
      <td>0.887163</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>o3</th>
      <td>0.859588</td>
      <td>-0.636524</td>
      <td>0.015696</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>o4</th>
      <td>-2.242685</td>
      <td>1.150036</td>
      <td>0.991946</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>o5</th>
      <td>0.953324</td>
      <td>-2.021255</td>
      <td>-0.334077</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Demonstration of main Pandas methods with dataset

We'll work with the next dataset:
https://bigml.com/user/francisco/gallery/dataset/5163ad540c0b5e5b22000383.
We’ll demonstrate the main methods in action by analyzing a dataset on the churn rate of telecom operator clients. Let’s read the data (using the read_csv method), and take a look at the first 5 lines using the head method:


```python
df = pd.read_csv('/Users/Aliaksandra_Varabyo1/OneDrive - EPAM/Desktop/telecom_churn.csv') # change for your path here
df.head() # 5 rows - default
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>Total eve calls</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KS</td>
      <td>128</td>
      <td>415</td>
      <td>No</td>
      <td>Yes</td>
      <td>25</td>
      <td>265.1</td>
      <td>110</td>
      <td>45.07</td>
      <td>197.4</td>
      <td>99</td>
      <td>16.78</td>
      <td>244.7</td>
      <td>91</td>
      <td>11.01</td>
      <td>10.0</td>
      <td>3</td>
      <td>2.70</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OH</td>
      <td>107</td>
      <td>415</td>
      <td>No</td>
      <td>Yes</td>
      <td>26</td>
      <td>161.6</td>
      <td>123</td>
      <td>27.47</td>
      <td>195.5</td>
      <td>103</td>
      <td>16.62</td>
      <td>254.4</td>
      <td>103</td>
      <td>11.45</td>
      <td>13.7</td>
      <td>3</td>
      <td>3.70</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NJ</td>
      <td>137</td>
      <td>415</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>243.4</td>
      <td>114</td>
      <td>41.38</td>
      <td>121.2</td>
      <td>110</td>
      <td>10.30</td>
      <td>162.6</td>
      <td>104</td>
      <td>7.32</td>
      <td>12.2</td>
      <td>5</td>
      <td>3.29</td>
      <td>0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>OH</td>
      <td>84</td>
      <td>408</td>
      <td>Yes</td>
      <td>No</td>
      <td>0</td>
      <td>299.4</td>
      <td>71</td>
      <td>50.90</td>
      <td>61.9</td>
      <td>88</td>
      <td>5.26</td>
      <td>196.9</td>
      <td>89</td>
      <td>8.86</td>
      <td>6.6</td>
      <td>7</td>
      <td>1.78</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OK</td>
      <td>75</td>
      <td>415</td>
      <td>Yes</td>
      <td>No</td>
      <td>0</td>
      <td>166.7</td>
      <td>113</td>
      <td>28.34</td>
      <td>148.3</td>
      <td>122</td>
      <td>12.61</td>
      <td>186.9</td>
      <td>121</td>
      <td>8.41</td>
      <td>10.1</td>
      <td>3</td>
      <td>2.73</td>
      <td>3</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



Let’s have a look at data dimensionality, feature names, and feature types.


```python
print(df.shape)
```

    (3333, 20)
    

From the output, we can see that the table contains 3333 rows and 20 columns.

Now let’s try printing out column names using columns:


```python
print(df.columns)
```

    Index(['State', 'Account length', 'Area code', 'International plan',
           'Voice mail plan', 'Number vmail messages', 'Total day minutes',
           'Total day calls', 'Total day charge', 'Total eve minutes',
           'Total eve calls', 'Total eve charge', 'Total night minutes',
           'Total night calls', 'Total night charge', 'Total intl minutes',
           'Total intl calls', 'Total intl charge', 'Customer service calls',
           'Churn'],
          dtype='object')
    

We can use the info() method to output some general information about the dataframe:


```python
print(df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3333 entries, 0 to 3332
    Data columns (total 20 columns):
     #   Column                  Non-Null Count  Dtype  
    ---  ------                  --------------  -----  
     0   State                   3333 non-null   object 
     1   Account length          3333 non-null   int64  
     2   Area code               3333 non-null   int64  
     3   International plan      3333 non-null   object 
     4   Voice mail plan         3333 non-null   object 
     5   Number vmail messages   3333 non-null   int64  
     6   Total day minutes       3333 non-null   float64
     7   Total day calls         3333 non-null   int64  
     8   Total day charge        3333 non-null   float64
     9   Total eve minutes       3333 non-null   float64
     10  Total eve calls         3333 non-null   int64  
     11  Total eve charge        3333 non-null   float64
     12  Total night minutes     3333 non-null   float64
     13  Total night calls       3333 non-null   int64  
     14  Total night charge      3333 non-null   float64
     15  Total intl minutes      3333 non-null   float64
     16  Total intl calls        3333 non-null   int64  
     17  Total intl charge       3333 non-null   float64
     18  Customer service calls  3333 non-null   int64  
     19  Churn                   3333 non-null   bool   
    dtypes: bool(1), float64(8), int64(8), object(3)
    memory usage: 498.1+ KB
    None
    

Bool, int64, float64 and object are the data types of our features. We see that one feature is logical (bool), 3 features are of type object, and 16 features are numeric. With this same method, we can easily see if there are any missing values. Here, there are none because each column contains 3333 observations, the same number of rows we saw before with shape.

We can change the column type with the astype method. Let’s apply this method to the Churn feature to convert it into int64:


```python
df["Churn"] = df["Churn"].astype("int64")
```

The describe method shows basic statistical characteristics of each numerical feature (int64 and float64 types): number of non-missing values, mean, standard deviation, range, median, 0.25 and 0.75 quartiles.


```python
df.describe()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Account length</th>
      <th>Area code</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>Total eve calls</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
      <td>3333.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>101.064806</td>
      <td>437.182418</td>
      <td>8.099010</td>
      <td>179.775098</td>
      <td>100.435644</td>
      <td>30.562307</td>
      <td>200.980348</td>
      <td>100.114311</td>
      <td>17.083540</td>
      <td>200.872037</td>
      <td>100.107711</td>
      <td>9.039325</td>
      <td>10.237294</td>
      <td>4.479448</td>
      <td>2.764581</td>
      <td>1.562856</td>
      <td>0.144914</td>
    </tr>
    <tr>
      <th>std</th>
      <td>39.822106</td>
      <td>42.371290</td>
      <td>13.688365</td>
      <td>54.467389</td>
      <td>20.069084</td>
      <td>9.259435</td>
      <td>50.713844</td>
      <td>19.922625</td>
      <td>4.310668</td>
      <td>50.573847</td>
      <td>19.568609</td>
      <td>2.275873</td>
      <td>2.791840</td>
      <td>2.461214</td>
      <td>0.753773</td>
      <td>1.315491</td>
      <td>0.352067</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>408.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>23.200000</td>
      <td>33.000000</td>
      <td>1.040000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>74.000000</td>
      <td>408.000000</td>
      <td>0.000000</td>
      <td>143.700000</td>
      <td>87.000000</td>
      <td>24.430000</td>
      <td>166.600000</td>
      <td>87.000000</td>
      <td>14.160000</td>
      <td>167.000000</td>
      <td>87.000000</td>
      <td>7.520000</td>
      <td>8.500000</td>
      <td>3.000000</td>
      <td>2.300000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>101.000000</td>
      <td>415.000000</td>
      <td>0.000000</td>
      <td>179.400000</td>
      <td>101.000000</td>
      <td>30.500000</td>
      <td>201.400000</td>
      <td>100.000000</td>
      <td>17.120000</td>
      <td>201.200000</td>
      <td>100.000000</td>
      <td>9.050000</td>
      <td>10.300000</td>
      <td>4.000000</td>
      <td>2.780000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>127.000000</td>
      <td>510.000000</td>
      <td>20.000000</td>
      <td>216.400000</td>
      <td>114.000000</td>
      <td>36.790000</td>
      <td>235.300000</td>
      <td>114.000000</td>
      <td>20.000000</td>
      <td>235.300000</td>
      <td>113.000000</td>
      <td>10.590000</td>
      <td>12.100000</td>
      <td>6.000000</td>
      <td>3.270000</td>
      <td>2.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>243.000000</td>
      <td>510.000000</td>
      <td>51.000000</td>
      <td>350.800000</td>
      <td>165.000000</td>
      <td>59.640000</td>
      <td>363.700000</td>
      <td>170.000000</td>
      <td>30.910000</td>
      <td>395.000000</td>
      <td>175.000000</td>
      <td>17.770000</td>
      <td>20.000000</td>
      <td>20.000000</td>
      <td>5.400000</td>
      <td>9.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



For categorical (type object) and boolean (type bool) features we can use the value_counts method. Let's take a look at the distribution of Churn:


```python
df["Churn"].value_counts()
```




    0    2850
    1     483
    Name: Churn, dtype: int64



2850 users out of 3333 are loyal

### Sorting

A DataFrame can be sorted by the value of one of the variables (i.e columns). For example, we can sort by Total day charge (use ascending=False to sort in descending order):


```python
df.sort_values(by="Total day charge", ascending=False).head()
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>Total eve calls</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>365</th>
      <td>CO</td>
      <td>154</td>
      <td>415</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>350.8</td>
      <td>75</td>
      <td>59.64</td>
      <td>216.5</td>
      <td>94</td>
      <td>18.40</td>
      <td>253.9</td>
      <td>100</td>
      <td>11.43</td>
      <td>10.1</td>
      <td>9</td>
      <td>2.73</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>985</th>
      <td>NY</td>
      <td>64</td>
      <td>415</td>
      <td>Yes</td>
      <td>No</td>
      <td>0</td>
      <td>346.8</td>
      <td>55</td>
      <td>58.96</td>
      <td>249.5</td>
      <td>79</td>
      <td>21.21</td>
      <td>275.4</td>
      <td>102</td>
      <td>12.39</td>
      <td>13.3</td>
      <td>9</td>
      <td>3.59</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2594</th>
      <td>OH</td>
      <td>115</td>
      <td>510</td>
      <td>Yes</td>
      <td>No</td>
      <td>0</td>
      <td>345.3</td>
      <td>81</td>
      <td>58.70</td>
      <td>203.4</td>
      <td>106</td>
      <td>17.29</td>
      <td>217.5</td>
      <td>107</td>
      <td>9.79</td>
      <td>11.8</td>
      <td>8</td>
      <td>3.19</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>156</th>
      <td>OH</td>
      <td>83</td>
      <td>415</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>337.4</td>
      <td>120</td>
      <td>57.36</td>
      <td>227.4</td>
      <td>116</td>
      <td>19.33</td>
      <td>153.9</td>
      <td>114</td>
      <td>6.93</td>
      <td>15.8</td>
      <td>7</td>
      <td>4.27</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>605</th>
      <td>MO</td>
      <td>112</td>
      <td>415</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>335.5</td>
      <td>77</td>
      <td>57.04</td>
      <td>212.5</td>
      <td>109</td>
      <td>18.06</td>
      <td>265.0</td>
      <td>132</td>
      <td>11.93</td>
      <td>12.7</td>
      <td>8</td>
      <td>3.43</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



We can also sort by multiple columns:


```python
df.sort_values(by=["Churn", "Total day charge"], ascending=[True, False]).head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>Total eve calls</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>688</th>
      <td>MN</td>
      <td>13</td>
      <td>510</td>
      <td>No</td>
      <td>Yes</td>
      <td>21</td>
      <td>315.6</td>
      <td>105</td>
      <td>53.65</td>
      <td>208.9</td>
      <td>71</td>
      <td>17.76</td>
      <td>260.1</td>
      <td>123</td>
      <td>11.70</td>
      <td>12.1</td>
      <td>3</td>
      <td>3.27</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2259</th>
      <td>NC</td>
      <td>210</td>
      <td>415</td>
      <td>No</td>
      <td>Yes</td>
      <td>31</td>
      <td>313.8</td>
      <td>87</td>
      <td>53.35</td>
      <td>147.7</td>
      <td>103</td>
      <td>12.55</td>
      <td>192.7</td>
      <td>97</td>
      <td>8.67</td>
      <td>10.1</td>
      <td>7</td>
      <td>2.73</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>534</th>
      <td>LA</td>
      <td>67</td>
      <td>510</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>310.4</td>
      <td>97</td>
      <td>52.77</td>
      <td>66.5</td>
      <td>123</td>
      <td>5.65</td>
      <td>246.5</td>
      <td>99</td>
      <td>11.09</td>
      <td>9.2</td>
      <td>10</td>
      <td>2.48</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>575</th>
      <td>SD</td>
      <td>114</td>
      <td>415</td>
      <td>No</td>
      <td>Yes</td>
      <td>36</td>
      <td>309.9</td>
      <td>90</td>
      <td>52.68</td>
      <td>200.3</td>
      <td>89</td>
      <td>17.03</td>
      <td>183.5</td>
      <td>105</td>
      <td>8.26</td>
      <td>14.2</td>
      <td>2</td>
      <td>3.83</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2858</th>
      <td>AL</td>
      <td>141</td>
      <td>510</td>
      <td>No</td>
      <td>Yes</td>
      <td>28</td>
      <td>308.0</td>
      <td>123</td>
      <td>52.36</td>
      <td>247.8</td>
      <td>128</td>
      <td>21.06</td>
      <td>152.9</td>
      <td>103</td>
      <td>6.88</td>
      <td>7.4</td>
      <td>3</td>
      <td>2.00</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Indexing and retrieving data

A DataFrame can be indexed in a few different ways.

To get a single column, you can use a DataFrame['Name'] construction. Let's use this to answer a question about that column alone: what is the proportion of churned users in our dataframe?


```python
df["Churn"].mean()
```




    0.14491449144914492



14.5% is actually quite bad for a company; such a churn rate can make the company go bankrupt.

Boolean indexing with one column is also very convenient. The syntax is df[P(df['Name'])], where P is some logical condition that is checked for each element of the Name column. The result of such indexing is the DataFrame consisting only of rows that satisfy the P condition on the Name column.

Let's use it to answer the question:

What are average values of numerical features for churned users?


```python
df[df["Churn"] == 1].mean()
```




    Account length            102.664596
    Area code                 437.817805
    Number vmail messages       5.115942
    Total day minutes         206.914079
    Total day calls           101.335404
    Total day charge           35.175921
    Total eve minutes         212.410145
    Total eve calls           100.561077
    Total eve charge           18.054969
    Total night minutes       205.231677
    Total night calls         100.399586
    Total night charge          9.235528
    Total intl minutes         10.700000
    Total intl calls            4.163561
    Total intl charge           2.889545
    Customer service calls      2.229814
    Churn                       1.000000
    dtype: float64



How much time (on average) do churned users spend on the phone during daytime?


```python
df[df["Churn"] == 1]["Total day minutes"].mean()
```




    206.91407867494814



What is the maximum length of international calls among loyal users (Churn == 0) who do not have an international plan?


```python
df[(df["Churn"] == 0) & (df["International plan"] == "No")]["Total intl minutes"].max()
```




    18.9



DataFrames can be indexed by column name (label) or row name (index) or by the serial number of a row. The loc method is used for indexing by name, while iloc() is used for indexing by number.

In the first case below, we say "give us the values of the rows with index from 0 to 5 (inclusive) and columns labeled from State to Area code (inclusive)". In the second case, we say "give us the values of the first five rows in the first three columns" (as in a typical Python slice: the maximal value is not included).


```python
df.loc[0:5, "State":"Area code"]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KS</td>
      <td>128</td>
      <td>415</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OH</td>
      <td>107</td>
      <td>415</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NJ</td>
      <td>137</td>
      <td>415</td>
    </tr>
    <tr>
      <th>3</th>
      <td>OH</td>
      <td>84</td>
      <td>408</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OK</td>
      <td>75</td>
      <td>415</td>
    </tr>
    <tr>
      <th>5</th>
      <td>AL</td>
      <td>118</td>
      <td>510</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[0:5, 0:3]
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KS</td>
      <td>128</td>
      <td>415</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OH</td>
      <td>107</td>
      <td>415</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NJ</td>
      <td>137</td>
      <td>415</td>
    </tr>
    <tr>
      <th>3</th>
      <td>OH</td>
      <td>84</td>
      <td>408</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OK</td>
      <td>75</td>
      <td>415</td>
    </tr>
  </tbody>
</table>
</div>



### Applying Functions to Cells, Columns and Rows

To apply functions to each column, use apply():


```python
df.apply(np.max)
```




    State                        WY
    Account length              243
    Area code                   510
    International plan          Yes
    Voice mail plan             Yes
    Number vmail messages        51
    Total day minutes         350.8
    Total day calls             165
    Total day charge          59.64
    Total eve minutes         363.7
    Total eve calls             170
    Total eve charge          30.91
    Total night minutes       395.0
    Total night calls           175
    Total night charge        17.77
    Total intl minutes         20.0
    Total intl calls             20
    Total intl charge           5.4
    Customer service calls        9
    Churn                         1
    dtype: object



The apply method can also be used to apply a function to each row. To do this, specify axis=1. Lambda functions are very convenient in such scenarios. For example, if we need to select all states starting with 'W', we can do it like this:


```python
df[df["State"].apply(lambda state: state[0] == "W")].head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>Total eve calls</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>WV</td>
      <td>141</td>
      <td>415</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>37</td>
      <td>258.6</td>
      <td>84</td>
      <td>43.96</td>
      <td>222.0</td>
      <td>111</td>
      <td>18.87</td>
      <td>326.4</td>
      <td>97</td>
      <td>14.69</td>
      <td>11.2</td>
      <td>5</td>
      <td>3.02</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>WY</td>
      <td>57</td>
      <td>408</td>
      <td>No</td>
      <td>Yes</td>
      <td>39</td>
      <td>213.0</td>
      <td>115</td>
      <td>36.21</td>
      <td>191.1</td>
      <td>112</td>
      <td>16.24</td>
      <td>182.7</td>
      <td>115</td>
      <td>8.22</td>
      <td>9.5</td>
      <td>3</td>
      <td>2.57</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>WI</td>
      <td>64</td>
      <td>510</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>154.0</td>
      <td>67</td>
      <td>26.18</td>
      <td>225.8</td>
      <td>118</td>
      <td>19.19</td>
      <td>265.3</td>
      <td>86</td>
      <td>11.94</td>
      <td>3.5</td>
      <td>3</td>
      <td>0.95</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>WY</td>
      <td>97</td>
      <td>415</td>
      <td>No</td>
      <td>Yes</td>
      <td>24</td>
      <td>133.2</td>
      <td>135</td>
      <td>22.64</td>
      <td>217.2</td>
      <td>58</td>
      <td>18.46</td>
      <td>70.6</td>
      <td>79</td>
      <td>3.18</td>
      <td>11.0</td>
      <td>3</td>
      <td>2.97</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>WY</td>
      <td>87</td>
      <td>415</td>
      <td>No</td>
      <td>No</td>
      <td>0</td>
      <td>151.0</td>
      <td>83</td>
      <td>25.67</td>
      <td>219.7</td>
      <td>116</td>
      <td>18.67</td>
      <td>203.9</td>
      <td>127</td>
      <td>9.18</td>
      <td>9.7</td>
      <td>3</td>
      <td>2.62</td>
      <td>5</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



The map method can be used to replace values in a column by passing a dictionary of the form {old_value: new_value} as its argument:


```python
d = {"No": False, "Yes": True}
df["International plan"] = df["International plan"].map(d)
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>Total eve calls</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KS</td>
      <td>128</td>
      <td>415</td>
      <td>False</td>
      <td>Yes</td>
      <td>25</td>
      <td>265.1</td>
      <td>110</td>
      <td>45.07</td>
      <td>197.4</td>
      <td>99</td>
      <td>16.78</td>
      <td>244.7</td>
      <td>91</td>
      <td>11.01</td>
      <td>10.0</td>
      <td>3</td>
      <td>2.70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OH</td>
      <td>107</td>
      <td>415</td>
      <td>False</td>
      <td>Yes</td>
      <td>26</td>
      <td>161.6</td>
      <td>123</td>
      <td>27.47</td>
      <td>195.5</td>
      <td>103</td>
      <td>16.62</td>
      <td>254.4</td>
      <td>103</td>
      <td>11.45</td>
      <td>13.7</td>
      <td>3</td>
      <td>3.70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NJ</td>
      <td>137</td>
      <td>415</td>
      <td>False</td>
      <td>No</td>
      <td>0</td>
      <td>243.4</td>
      <td>114</td>
      <td>41.38</td>
      <td>121.2</td>
      <td>110</td>
      <td>10.30</td>
      <td>162.6</td>
      <td>104</td>
      <td>7.32</td>
      <td>12.2</td>
      <td>5</td>
      <td>3.29</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>OH</td>
      <td>84</td>
      <td>408</td>
      <td>True</td>
      <td>No</td>
      <td>0</td>
      <td>299.4</td>
      <td>71</td>
      <td>50.90</td>
      <td>61.9</td>
      <td>88</td>
      <td>5.26</td>
      <td>196.9</td>
      <td>89</td>
      <td>8.86</td>
      <td>6.6</td>
      <td>7</td>
      <td>1.78</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OK</td>
      <td>75</td>
      <td>415</td>
      <td>True</td>
      <td>No</td>
      <td>0</td>
      <td>166.7</td>
      <td>113</td>
      <td>28.34</td>
      <td>148.3</td>
      <td>122</td>
      <td>12.61</td>
      <td>186.9</td>
      <td>121</td>
      <td>8.41</td>
      <td>10.1</td>
      <td>3</td>
      <td>2.73</td>
      <td>3</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Grouping

In general, grouping data in Pandas works as follows:

df.groupby(by=grouping_columns)[columns_to_show].function()
1. First, the groupby method divides the grouping_columns by their values. They become a new index in the resulting dataframe.
2. Then, columns of interest are selected (columns_to_show). If columns_to_show is not included, all non groupby clauses will be included.
3. Finally, one or several functions are applied to the obtained groups per selected columns.

Here is an example where we group the data according to the values of the Churn variable and display statistics of three columns in each group:


```python
columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]

df.groupby(["Churn"])[columns_to_show].describe(percentiles=[])
```

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="6" halign="left">Total day minutes</th>
      <th colspan="6" halign="left">Total eve minutes</th>
      <th colspan="6" halign="left">Total night minutes</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>50%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>50%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>50%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Churn</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2850.0</td>
      <td>175.175754</td>
      <td>50.181655</td>
      <td>0.0</td>
      <td>177.2</td>
      <td>315.6</td>
      <td>2850.0</td>
      <td>199.043298</td>
      <td>50.292175</td>
      <td>0.0</td>
      <td>199.6</td>
      <td>361.8</td>
      <td>2850.0</td>
      <td>200.133193</td>
      <td>51.105032</td>
      <td>23.2</td>
      <td>200.25</td>
      <td>395.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>483.0</td>
      <td>206.914079</td>
      <td>68.997792</td>
      <td>0.0</td>
      <td>217.6</td>
      <td>350.8</td>
      <td>483.0</td>
      <td>212.410145</td>
      <td>51.728910</td>
      <td>70.9</td>
      <td>211.3</td>
      <td>363.7</td>
      <td>483.0</td>
      <td>205.231677</td>
      <td>47.132825</td>
      <td>47.4</td>
      <td>204.80</td>
      <td>354.9</td>
    </tr>
  </tbody>
</table>
</div>



Let’s do the same thing, but slightly differently by passing a list of functions to agg():


```python
columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]

df.groupby(["Churn"])[columns_to_show].agg([np.mean, np.std, np.min, np.max])
```

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">Total day minutes</th>
      <th colspan="4" halign="left">Total eve minutes</th>
      <th colspan="4" halign="left">Total night minutes</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>std</th>
      <th>amin</th>
      <th>amax</th>
      <th>mean</th>
      <th>std</th>
      <th>amin</th>
      <th>amax</th>
      <th>mean</th>
      <th>std</th>
      <th>amin</th>
      <th>amax</th>
    </tr>
    <tr>
      <th>Churn</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>175.175754</td>
      <td>50.181655</td>
      <td>0.0</td>
      <td>315.6</td>
      <td>199.043298</td>
      <td>50.292175</td>
      <td>0.0</td>
      <td>361.8</td>
      <td>200.133193</td>
      <td>51.105032</td>
      <td>23.2</td>
      <td>395.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>206.914079</td>
      <td>68.997792</td>
      <td>0.0</td>
      <td>350.8</td>
      <td>212.410145</td>
      <td>51.728910</td>
      <td>70.9</td>
      <td>363.7</td>
      <td>205.231677</td>
      <td>47.132825</td>
      <td>47.4</td>
      <td>354.9</td>
    </tr>
  </tbody>
</table>
</div>



### Joins


```python
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'column_1df': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'column_2df': ['B0', 'B1', 'B2']})
```


```python
df1.set_index('key').join(df2.set_index('key'))
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>column_1df</th>
      <th>column_2df</th>
    </tr>
    <tr>
      <th>key</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>A3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K4</th>
      <td>A4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K5</th>
      <td>A5</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.set_index('key').join(df2.set_index('key'), how = 'inner')
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>column_1df</th>
      <th>column_2df</th>
    </tr>
    <tr>
      <th>key</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
    </tr>
  </tbody>
</table>
</div>



How can be: ‘left’, ‘right’, ‘outer’, ‘inner’; default ‘left’

### Summary tables

Suppose we want to see how the observations in our dataset are distributed in the context of two variables - Churn and International plan. To do so, we can build a contingency table using the crosstab method:


```python
pd.crosstab(df["Churn"], df["International plan"])
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>International plan</th>
      <th>False</th>
      <th>True</th>
    </tr>
    <tr>
      <th>Churn</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2664</td>
      <td>186</td>
    </tr>
    <tr>
      <th>1</th>
      <td>346</td>
      <td>137</td>
    </tr>
  </tbody>
</table>
</div>



We can see that most of the users are loyal and do not use additional services (International Plan/Voice mail).

This will resemble pivot tables to those familiar with Excel. And, of course, pivot tables are implemented in Pandas: the pivot_table method takes the following parameters:

values – a list of variables to calculate statistics for,
index – a list of variables to group data by,
aggfunc – what statistics we need to calculate for groups, ex. sum, mean, maximum, minimum or something else.

Let’s take a look at the average number of day, evening, and night calls by area code:


```python
df.pivot_table(
    ["Total day calls", "Total eve calls", "Total night calls"],
    ["Area code"],
    aggfunc="mean",
).head(10)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total day calls</th>
      <th>Total eve calls</th>
      <th>Total night calls</th>
    </tr>
    <tr>
      <th>Area code</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>408</th>
      <td>100.496420</td>
      <td>99.788783</td>
      <td>99.039379</td>
    </tr>
    <tr>
      <th>415</th>
      <td>100.576435</td>
      <td>100.503927</td>
      <td>100.398187</td>
    </tr>
    <tr>
      <th>510</th>
      <td>100.097619</td>
      <td>99.671429</td>
      <td>100.601190</td>
    </tr>
  </tbody>
</table>
</div>



### DataFrame transformations

Like many other things in Pandas, adding columns to a DataFrame is doable in many ways.

For example, if we want to calculate the total number of calls for all users, let’s create the total_calls Series and paste it into the DataFrame:


```python
total_calls = (
    df["Total day calls"]
    + df["Total eve calls"]
    + df["Total night calls"]
    + df["Total intl calls"]
)
df.insert(loc=len(df.columns), column="Total calls", value=total_calls)
# loc parameter is the number of columns after which to insert the Series object
# we set it to len(df.columns) to paste it at the very end of the dataframe
df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>...</th>
      <th>Total eve charge</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
      <th>Total calls</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KS</td>
      <td>128</td>
      <td>415</td>
      <td>False</td>
      <td>Yes</td>
      <td>25</td>
      <td>265.1</td>
      <td>110</td>
      <td>45.07</td>
      <td>197.4</td>
      <td>...</td>
      <td>16.78</td>
      <td>244.7</td>
      <td>91</td>
      <td>11.01</td>
      <td>10.0</td>
      <td>3</td>
      <td>2.70</td>
      <td>1</td>
      <td>0</td>
      <td>303</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OH</td>
      <td>107</td>
      <td>415</td>
      <td>False</td>
      <td>Yes</td>
      <td>26</td>
      <td>161.6</td>
      <td>123</td>
      <td>27.47</td>
      <td>195.5</td>
      <td>...</td>
      <td>16.62</td>
      <td>254.4</td>
      <td>103</td>
      <td>11.45</td>
      <td>13.7</td>
      <td>3</td>
      <td>3.70</td>
      <td>1</td>
      <td>0</td>
      <td>332</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NJ</td>
      <td>137</td>
      <td>415</td>
      <td>False</td>
      <td>No</td>
      <td>0</td>
      <td>243.4</td>
      <td>114</td>
      <td>41.38</td>
      <td>121.2</td>
      <td>...</td>
      <td>10.30</td>
      <td>162.6</td>
      <td>104</td>
      <td>7.32</td>
      <td>12.2</td>
      <td>5</td>
      <td>3.29</td>
      <td>0</td>
      <td>0</td>
      <td>333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>OH</td>
      <td>84</td>
      <td>408</td>
      <td>True</td>
      <td>No</td>
      <td>0</td>
      <td>299.4</td>
      <td>71</td>
      <td>50.90</td>
      <td>61.9</td>
      <td>...</td>
      <td>5.26</td>
      <td>196.9</td>
      <td>89</td>
      <td>8.86</td>
      <td>6.6</td>
      <td>7</td>
      <td>1.78</td>
      <td>2</td>
      <td>0</td>
      <td>255</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OK</td>
      <td>75</td>
      <td>415</td>
      <td>True</td>
      <td>No</td>
      <td>0</td>
      <td>166.7</td>
      <td>113</td>
      <td>28.34</td>
      <td>148.3</td>
      <td>...</td>
      <td>12.61</td>
      <td>186.9</td>
      <td>121</td>
      <td>8.41</td>
      <td>10.1</td>
      <td>3</td>
      <td>2.73</td>
      <td>3</td>
      <td>0</td>
      <td>359</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



It is possible to add a column more easily without creating an intermediate Series instance:


```python
df["Total charge"] = (
    df["Total day charge"]
    + df["Total eve charge"]
    + df["Total night charge"]
    + df["Total intl charge"]
)

df.head()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Account length</th>
      <th>Area code</th>
      <th>International plan</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
      <th>Total day minutes</th>
      <th>Total day calls</th>
      <th>Total day charge</th>
      <th>Total eve minutes</th>
      <th>...</th>
      <th>Total night minutes</th>
      <th>Total night calls</th>
      <th>Total night charge</th>
      <th>Total intl minutes</th>
      <th>Total intl calls</th>
      <th>Total intl charge</th>
      <th>Customer service calls</th>
      <th>Churn</th>
      <th>Total calls</th>
      <th>Total charge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KS</td>
      <td>128</td>
      <td>415</td>
      <td>False</td>
      <td>Yes</td>
      <td>25</td>
      <td>265.1</td>
      <td>110</td>
      <td>45.07</td>
      <td>197.4</td>
      <td>...</td>
      <td>244.7</td>
      <td>91</td>
      <td>11.01</td>
      <td>10.0</td>
      <td>3</td>
      <td>2.70</td>
      <td>1</td>
      <td>0</td>
      <td>303</td>
      <td>75.56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OH</td>
      <td>107</td>
      <td>415</td>
      <td>False</td>
      <td>Yes</td>
      <td>26</td>
      <td>161.6</td>
      <td>123</td>
      <td>27.47</td>
      <td>195.5</td>
      <td>...</td>
      <td>254.4</td>
      <td>103</td>
      <td>11.45</td>
      <td>13.7</td>
      <td>3</td>
      <td>3.70</td>
      <td>1</td>
      <td>0</td>
      <td>332</td>
      <td>59.24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NJ</td>
      <td>137</td>
      <td>415</td>
      <td>False</td>
      <td>No</td>
      <td>0</td>
      <td>243.4</td>
      <td>114</td>
      <td>41.38</td>
      <td>121.2</td>
      <td>...</td>
      <td>162.6</td>
      <td>104</td>
      <td>7.32</td>
      <td>12.2</td>
      <td>5</td>
      <td>3.29</td>
      <td>0</td>
      <td>0</td>
      <td>333</td>
      <td>62.29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>OH</td>
      <td>84</td>
      <td>408</td>
      <td>True</td>
      <td>No</td>
      <td>0</td>
      <td>299.4</td>
      <td>71</td>
      <td>50.90</td>
      <td>61.9</td>
      <td>...</td>
      <td>196.9</td>
      <td>89</td>
      <td>8.86</td>
      <td>6.6</td>
      <td>7</td>
      <td>1.78</td>
      <td>2</td>
      <td>0</td>
      <td>255</td>
      <td>66.80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>OK</td>
      <td>75</td>
      <td>415</td>
      <td>True</td>
      <td>No</td>
      <td>0</td>
      <td>166.7</td>
      <td>113</td>
      <td>28.34</td>
      <td>148.3</td>
      <td>...</td>
      <td>186.9</td>
      <td>121</td>
      <td>8.41</td>
      <td>10.1</td>
      <td>3</td>
      <td>2.73</td>
      <td>3</td>
      <td>0</td>
      <td>359</td>
      <td>52.09</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



To delete columns or rows, use the drop method, passing the required indexes and the axis parameter (1 if you delete columns, and nothing or 0 if you delete rows). The inplace argument tells whether to change the original DataFrame. With inplace=False, the drop method doesn't change the existing DataFrame and returns a new one with dropped rows or columns. With inplace=True, it alters the DataFrame.


```python
df = df.drop(["Total charge"], axis=1)
```

### Tasks (with answers):

1. Display the number of those who used / did not use the "international roaming" service.


```python
print("Number of those who used the service {}, who didn't use the service - {} .".format(sum(df['International plan'] == True), 
                                            sum(df['International plan'] == False)))
```

    Number of those who used the service 323, who didn't use the service - 3010 .
    


```python
df['International plan'].value_counts() # easier
```




    False    3010
    True      323
    Name: International plan, dtype: int64



2. Print rows from 5 to 13 with the following columns: 'State', 'Voice mail plan', 'Number vmail messages'


```python
df[['State','Voice mail plan','Number vmail messages']].loc[5:13,:]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Voice mail plan</th>
      <th>Number vmail messages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>AL</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>MA</td>
      <td>Yes</td>
      <td>24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MO</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>LA</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>WV</td>
      <td>Yes</td>
      <td>37</td>
    </tr>
    <tr>
      <th>10</th>
      <td>IN</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>RI</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>IA</td>
      <td>No</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>MT</td>
      <td>No</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



3. Leave only states where the total number of daily calls is less than 10 and write this cut dataflame to a csv file.


```python
result = df[df["Total day calls"].apply(lambda call: call < 10)]
result.to_csv('task_3.csv', index = False)
```

4. Export of the dataframe to JSON file


```python
df.to_json('task_4.json')
```

5. Export of the dataframe to AVRO file


```python
import pandavro as pdx # before it: pip install pandavro from command line
pdx.to_avro('task_5.avro', df)
```

6. Export of the dataframe to Parquet file


```python
import pyarrow as pa # before it: pip install pyarrow from command line
import pyarrow.parquet as pq

table = pa.Table.from_pandas(df, preserve_index=True)
pq.write_table(table, 'task_6.parquet')
```

7. Using 3 threads raise values in columns 'Total day minutes', 'Total day calls', 'Total day charge' to the third power (power - **) and export result dataframe to csv file.


```python
import threading

df = pd.read_csv('/Users/Aliaksandra_Varabyo1/OneDrive - EPAM/Desktop/telecom_churn.csv')
arr = ['Total night minutes','Total night calls','Total night charge']

def sum_col_values(column_name):
    df[column_name] =  df[column_name].apply(lambda x: x**3)

worker_threads = 3

threads = []

for i in range(worker_threads):
    thread = threading.Thread(target=sum_col_values, args=(arr[i],))
    thread.setDaemon(True)
    thread.start()
    threads.append(thread)
for j in threads:
    j.join()

df.to_csv('task_7.csv')
```

8. Get dataframe (df). Fill the nulls with the average value for the column, add column names as "col_1", "col_2", ... and export the file to html format.


```python
###### don't change it - just run it
df = pd.DataFrame(
    np.random.randn(5, 3)
)
df.iloc[0, 2] = None
df.iloc[4, 1] = None
###### don't change it
```


```python
df = df.fillna(df.mean())
df.columns = ['col_'+ str(i+1) for i in range(df.shape[1])]
df.to_html('task_8.html')
```

9. Get dataframe (df). Then change color to red for cells where value is less than 0 and to yellow where values in cells are nulls. Then export final dataframe to excel.


```python
###### don't change it - just run it
df = pd.DataFrame(
    np.random.randn(5, 3)
)
df.iloc[0, 2] = None
df.iloc[4, 1] = None
###### don't change it
```


```python
styled = (df.style.
          applymap(lambda v: 'background-color: %s' % 'red' if v<0 else '').
          applymap(lambda v: 'background-color: %s' % 'yellow' if np.isnan(v) else ''))
styled.to_excel('task_9.xlsx', engine='openpyxl')
```


10. Is that true that for states that have 'voice mail plan' service churn appears more frequently than for states that don't have such service?


```python
df = pd.read_csv('/Users/Aliaksandra_Varabyo1/OneDrive - EPAM/Desktop/telecom_churn.csv') # change for your path here
voice_loyal = df[df["Voice mail plan"] == "Yes"]["Churn"]
non_voice_loyal = df[df["Voice mail plan"] == "No"]["Churn"]


print(
    "Churns appeared: \n\t among states that had voice mail plan - {}%, \n\t among states that didn't have voice mail plan - {}%".format(
        round(100 * voice_loyal.mean(), 1), round(100 * non_voice_loyal.mean(), 1)
    )
)
```

    Churns appeared: 
    	 among states that had voice mail plan - 8.7%, 
    	 among states that didn't have voice mail plan - 16.7%
    

-> No, churns appeared more frequently for them who didn't have voice mail plan service

11*. Count the total number of calls for loyal states (churn = 0) who did not have service calls, display the data in Excel, highlight the states with the largest number of loyal customers in green, and the states with the smallest in red.


```python
df["Total calls"] = (
    df["Total day calls"]
    + df["Total eve calls"]
    + df["Total night calls"]
    + df["Total intl calls"]
)
result = df[(df['Churn']==False) & (df['Customer service calls']==0)][['State', 'Total calls']]
```

As alternative way to get colored cells in Excel (using openpyxl directly)

As one of the possible solutions:


```python
result['id'] = np.arange(len(result)) # add new column as a sequence 
max_calls = result[result["Total calls"] == max(result["Total calls"])] # row with max number of calls
min_calls = result[result["Total calls"] == min(result["Total calls"])] # row with min number of calls
result.to_excel('task_11.xlsx', sheet_name='task_11', index = False)
```


```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.styles import PatternFill
wb = load_workbook('./task_11.xlsx')
sheet = wb['task_11']

redFill = PatternFill(start_color='FFEE1111', end_color='FFEE1111', fill_type='solid')
greenFill = PatternFill(start_color='0000FF00', end_color='0000FF00', fill_type='solid')

sheet['A'+str(max_calls['id'].values[0]+2)].fill = greenFill # +2 as in python numeration starts from 0; one row is header
sheet['A'+str(min_calls['id'].values[0]+2)].fill = redFill
wb.save('task_11.xlsx')
```
