n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end="\t")
    print('')

"""
output:
1                                                                                                                                             
2       2                                                                                                                                     
3       3       3                                                                                                                             
4       4       4       4                                                                                                                     
5       5       5       5       5  
"""
