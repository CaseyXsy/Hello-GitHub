#徐舒扬 20312080 2021/9/6 HW2-1

DNAstr='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
sep=list(DNAstr)            #Convert string to list

## list(str)会将str中的每个字符(包括空格等)作为列表元素

# str.split("分隔符")会将str按分隔符split
#"分隔符".join(list)则将list按分隔符输出为str

A_n=sep.count('A')
T_n=sep.count('T')
C_n=sep.count('C')
G_n=sep.count('G')          #返回碱基数
SUM=A_n+T_n+C_n+G_n         #求和

print(f"各个碱基的占比分别为\nA:%.1f%%, T:%.1f%%, C:%.1f%%, G:%.1f%%"  %(A_n*100/SUM, T_n*100/SUM, C_n*100/SUM, G_n*100/SUM))
#用占位符格式化输出可显著减少用连接符"+"产生的代码冗余

#"%"作占位符,"%%"可输出"%"
# %s输出str, %f输出float, %d输出int, 其中%f可写为%.nf, n即为小数保留位数
