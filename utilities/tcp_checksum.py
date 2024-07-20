#copyright IOTSecureLab
#Author Anand A. 2023
# TCP checksum generator

a1='c0a8'
a2='0402'
a3='c0a8'
a4='0401'
a5='0006'
a6='003b'
a7='0538'
a8='afdd'
a9='1ac8'
a10='7299'
a11='6ca4'
a12='5018'
a13='ffff'
a14='7365'
a15='745f'
a16='5749'
a17='4649'
a18='313a'
a19='3a73'
a20='7369'
a21='643d'
a22='6379'
a23='6265'
a24='7265'
a25='793b'
a26='7061'
a27='7373'
a28='3d63'
a29='6562'
a30='6831'
a31='3233'
a32='343b'
a33='0a00'


#################Data##################
a1_int = int(a1, 16)
a2_int = int(a2, 16)
a3_int = int(a3, 16)
a4_int = int(a4, 16)
a5_int = int(a5, 16)
a6_int = int(a6, 16)
a7_int = int(a7, 16)
a8_int = int(a8, 16)
a9_int = int(a9, 16)
a10_int = int(a10, 16)
a11_int = int(a11, 16)
a12_int = int(a12, 16)
a13_int = int(a13, 16)
a14_int = int(a14, 16)
a15_int = int(a15, 16)
a16_int = int(a16, 16)
a17_int = int(a17, 16)
a18_int = int(a18, 16)
a19_int = int(a19, 16)
a20_int = int(a20, 16)
a21_int = int(a21, 16)
a22_int = int(a22, 16)
a23_int = int(a23, 16)
a24_int = int(a24, 16)
a25_int = int(a25, 16)
a26_int = int(a26, 16)
a27_int = int(a27, 16)
a28_int = int(a28, 16)
a29_int = int(a29, 16)
a30_int = int(a30, 16)
a31_int = int(a31, 16)
a32_int = int(a32, 16)
a33_int = int(a33, 16)



result = hex(a1_int + a2_int + a3_int + a4_int + a5_int + a6_int +a7_int + a8_int + a9_int
+a10_int + a11_int + a12_int + a13_int + a14_int + a15_int + a16_int + a17_int+ a18_int + a19_int 
+ a20_int + a21_int + a22_int + a23_int + a24_int + a25_int + a26_int + a27_int+ a28_int + a29_int + a30_int + a31_int + a32_int + a33_int)


print(result[2:])
