'''
Author : Théo Bocquet
'''


# Ici on va définir chaque niveau avec une grille de 20*15 représentant les rectancgles sur le terrain 
#niveau de test
niveaut = [[1,   1,   1,  1,   1,   1,   1,  1,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,] ,  
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ], 
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ]

]

niveau1 = [[0,   1,   1,   1,   0,   1,   1,   1,   0,   0,   0,   1,   1,   1,   0,   0,   1,   1,   1,   1,] ,  
[0,   1,   1,   1,   0,   1,   1,   1,   0,   0,   0,   1,   0,   1,   1,   0,   1,   1,   1,   1, ],
[0,   1,   1,   1,   0,   1,   1,   1,   0,   0,   0,   1,   0,   0,   1,   1,   1,   1,   1,   1, ],
[0,   1,   1,   1,   1,   1,   1,   1,   1,   0,   1,   1,   0,   0,   0,   1,   1,   1,   0,   0, ],
[0,   1,   1,   0,   0,   0,   1,   0,   1,   1,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0, ],
[0,   1,   1,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0, ],
[0,   1,   1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   1,   1,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   1,   1,   1,   1,   1,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   1,   1,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0, ], 
[0,   1,   1,   1,   1,   1,   0,   0,   0,   0,   0,   1,   1,   1,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ]

]
niveau2 = [[0,   0,   0,   0,   0,   1,   1,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   4,],   
[0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4, ],
[0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,   4,   4,   4,   4,   0,   0,   0,   0,   4, ],
[0,   0,   0,   0,   0,   4,   0,   0,   1,   1,   1,   1,   1,   1,   1,   4,   4,   0,   0,   4, ],
[0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   2,   0,   0,   4, ],
[0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4, ] ,
[0,   0,   0,   0,   0,   4,   2,   2,   0,   0,   0,   2,   2,   0,   0,   0,   0,   0,   0,   4, ],
[0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,   4,   4,   4,   4,   0,   0,   4,   4,   4, ],
[0,   4,   2,   2,   2,   1,   0,   0,   0,   0,   0,   0,   0,   4,   4,   0,   0,   4,   4,   0, ],
[0,   4,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   4,   4,   0,   0,   0,   4,   0, ],
[0,   4,   0,   0,   0,   0,   0,   0,   2,   2,   2,   0,   0,   4,   4,   4,   0,   0,   4,   0, ] , 
[0,   4,   0,   0,   4,   4,   4,   4,   2,   0,   0,   0,   0,   4,   0,   4,   0,   0,   4,   0, ],
[0,   1,   0,   0,   1,   0,   0,   0,   2,   0,   0,   0,   0,   1,   0,   1,   0,   0,   1,   0, ],
[0,   2,   0,   0,   2,   2,   2,   2,   2,   0,   0,   2,   2,   2,   2,   2,   0,   0,   2,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ]

]
niveau3 = [[0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,],   
[0,   2,   2,   0,   0,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   0,   0,   2,   2,   0, ],
[0,   0,   2,   0,   2,   2,   0,   2,   0,   2,   2,   0,   2,   0,   2,   2,   0,   2,   0,   0, ],
[0,   0,   2,   2,   2,   0,   0,   5,   0,   0,   0,   0,   5,   0,   0,   2,   2,   2,   0,   0, ],
[0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   5,   0,   0,   3,   3,   3,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0, ],
[0,   0,   0,   0,   0,   3,   3,   3,   3,   3,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0,   0,   2,   2,   0,   0,   5,   0,   0,   0, ],  
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   2,   2,   2,   2,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ]

]
niveau4 = [[0,   0,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   0,   0,] ,  
[0,   0,   0,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   2,   2,   2,   2,   2,   2,   2,   2,   0,   0,   0,   0,   0,   0, ],
[3,   3,   0,   0,   0,   0,   0,   0,   2,   2,   2,   2,   0,   0,   0,   0,   0,   0,   3,   3, ],
[3,   3,   3,   3,   3,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   3,   3,   3,   3,   3, ],
[0,   3,   3,   3,   3,   3,   3,   3,   3,   0,   0,   3,   3,   6,   3,   3,   3,   3,   0,   0, ],
[0,   0,   0,   0,   3,   3,   6,   3,   3,   3,   3,   3,   3,   3,   3,   3,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   3,   3,   3,   3,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   6,   0,   0,   0,   0,   0,   0,   0,   6,   0,   0,   0,   0,   0,   0,   6,   0, ],
[0,   0,   0,   0,   0,   6,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ], 
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   6,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   6,   0,   0,   0,   0,   0,   0,   6,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   6,   0,   0, ]

]

niveau5 = [[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,] ,  
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   6,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   5,   0,   0, ],
[0,   1,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   7,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   7,   0,   0,   0,   0,   0,   0,   0,   6,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   1,   1,   1,   5,   0,   0,   0,   0,   7,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   6,   0,   0, ],
[0,   0,   0,   0,   0,   6,   7,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   6,   0, ],
[0,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   5,   0,   0,   1,   0,   7,   0,   0, ],
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0, ], 
[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   5,   0,   0,   0,   0, ],
[0,   0,   7,   0,   6,   0,   0,   0,   0,   0,   7,   0,   0,   6,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ],
[0,   0,   0,   0,   0,   0,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, ]

]
#a chaque ajoue de niveau merci de mettre a jour la liste 
LLEVEL = [niveau1,niveau2,niveau3,niveau4,niveau5]