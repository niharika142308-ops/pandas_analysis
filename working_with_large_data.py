#working with larger amount of data 
import pandas as pd
for df in pd.read_csv('modified.csv',chunksize=5):
    print("chunk df")
    print(df)

output pattern 
chunk df
     #        Name  Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
90  83  Farfetch'd  Normal  Flying    352  52      65       55       58       62     60           1      False
91  84       Doduo  Normal  Flying    310  35      85       45       35       35     75           1      False
92  85      Dodrio  Normal  Flying    460  60     110       70       60       60    100           1      False
93  86        Seel   Water     NaN    325  65      45       55       45       70     45           1      False
94  87     Dewgong   Water     Ice    475  90      70       80       70       95     70           1      False
chunk df
     #      Name  Type 1  Type 2  Total   HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
95  88    Grimer  Poison     NaN    325   80      80       50       40       50     25           1      False
96  89       Muk  Poison     NaN    500  105     105       75       65      100     50           1      False
97  90  Shellder   Water     NaN    305   30      65      100       45       25     40           1      False
98  91  Cloyster   Water     Ice    525   50      95      180       85       45     70           1      False
99  92    Gastly   Ghost  Poison    310   30      35       30      100       35     80           1      False
chunk df
      #               Name   Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
100  93            Haunter    Ghost  Poison    405  45      50       45      115       55     95           1      False        
101  94             Gengar    Ghost  Poison    500  60      65       60      130       75    110           1      False        
102  94  GengarMega Gengar    Ghost  Poison    600  60      65       80      170       95    130           1      False        
103  95               Onix     Rock  Ground    385  35      45      160       30       45     70           1      False        
104  96            Drowzee  Psychic     NaN    328  60      48       45       43       90     42           1      False        
chunk df
       #       Name    Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
105   97      Hypno   Psychic     NaN    483  85      73       70       73      115     67           1      False
106   98     Krabby     Water     NaN    325  30     105       90       25       25     50           1      False
107   99    Kingler     Water     NaN    475  55     130      115       50       50     75           1      False
108  100    Voltorb  Electric     NaN    330  40      30       50       55       55    100           1      False
109  101  Electrode  Electric     NaN    480  60      50       70       80       80    140           1      False
chunk df
       #       Name    Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
110  102  Exeggcute     Grass  Psychic    325  60      40       80       60       45     40           1      False
111  103  Exeggutor     Grass  Psychic    520  95      95       85      125       65     55           1      False
112  104     Cubone    Ground      NaN    320  50      50       95       40       50     35           1      False
113  105    Marowak    Ground      NaN    425  60      80      110       50       80     45           1      False
114  106  Hitmonlee  Fighting      NaN    455  50     120       53       35      110     87           1      False
chunk df
       #        Name    Type 1 Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
115  107  Hitmonchan  Fighting    NaN    455  50     105       79       35      110     76           1      False
116  108   Lickitung    Normal    NaN    385  90      55       75       60       75     30           1      False
117  109     Koffing    Poison    NaN    340  40      65       95       60       45     35           1      False
118  110     Weezing    Poison    NaN    490  65      90      120       85       70     60           1      False
119  111     Rhyhorn    Ground   Rock    345  80      85       95       30       30     25           1      False
chunk df
       #                       Name  Type 1 Type 2  Total   HP  ...  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
120  112                     Rhydon  Ground   Rock    485  105  ...      120       45       45     40           1      False   
121  113                    Chansey  Normal    NaN    450  250  ...        5       35      105     50           1      False   
122  114                    Tangela   Grass    NaN    435   65  ...      115      100       40     60           1      False   
123  115                 Kangaskhan  Normal    NaN    490  105  ...       80       40       80     90           1      False   
124  115  KangaskhanMega Kangaskhan  Normal    NaN    590  105  ...      100       60      100    100           1      False   

[5 rows x 13 columns]
chunk df
       #     Name Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
125  116   Horsea  Water     NaN    295  30      40       70       70       25     60           1      False
126  117   Seadra  Water     NaN    440  55      65       95       95       45     85           1      False
127  118  Goldeen  Water     NaN    320  45      67       60       35       50     63           1      False
128  119  Seaking  Water     NaN    450  80      92       65       65       80     68           1      False
129  120   Staryu  Water     NaN    340  30      45       55       70       55     85           1      False
chunk df
       #        Name    Type 1   Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
130  121     Starmie     Water  Psychic    520  60      75       85      100       85    115           1      False
131  122    Mr. Mime   Psychic    Fairy    460  40      45       65      100      120     90           1      False
132  123     Scyther       Bug   Flying    500  70     110       80       55       80    105           1      False
133  124        Jynx       Ice  Psychic    455  65      50       35      115       95     95           1      False
134  125  Electabuzz  Electric      NaN    490  65      83       57       95       85    105           1      False
chunk df    