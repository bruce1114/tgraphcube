# coding=utf-8

from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

create_dataset = ['s=10', 's=20', 's=50',  's=80']
lenDataset = 4

col = ["green",'blue','black','#386cb0']
lab = ['o',  '>', 'x', 'v']

# from excel
prearray_time=[
    [1638,2419,2636,2705,2726,2733,2720,2515,2473,2506],
    [1314,1517,1534,1530,1424,1396,1398,1400,1399,1398],
    [839,775,739,739,740,743,741,741,743,745],
    [658,571,573,569,569,568,568,569,570,569]
]

prearray_size=[
    [3668231,10412411,18204690,26309127,34492702,42692064,50893578,59095297,67297027,75498757],
    [2791015,6762518,10853890,14954218,19055058,23155923,27256788,31357653,35458518,39559383],
    [1531888,3172066,4812406,6452746,8093086,9733426,11373766,13014106,14654446,16294786],
    [1032726,2057931,3083136,4108341,5133546,6158751,7183956,8209161,9234366,10259571]
]

stable_time=[
    [6473,13242,20399,20351,26620,27660,27649,27674,31920,34643],
    [5716,10570,14176,14194,17197,17686,17668,17679,19769,21167],
    [4430,6896,8480,8507,9803,10030,10021,10029,10944,11585],
    [3724,5459,6552,6559,7502,7688,7666,7681,8331,8779]
]

stable_size=[
    [5698456,18389139,38552151,58711872,85953714,114281354,142629160,170986797,204254947,240800692],
    [4980992,14859759,28818810,42784364,60302334,78367589,96421039,114485789,135010662,157170469],
    [3614739,9603441,17232536,24862218,33913168,43182643,52453245,61720878,71974326,82883082],
    [2854375,7226391,12622547,18018820,24303480,30726470,37147333,43569476,50605999,58053217]
]

stree_time=[
    [3634,4593,5263,5166,5886,5682,5651,5650,6301,6249],
    [3310,4076,4692,4551,5224,4952,5116,5059,5663,5396],
    [2803,3518,3955,3956,4345,4250,4382,4360,4749,4538],
    [2572,3235,3614,3643,3995,3954,4064,4035,4346,4192]
]

stree_size=[
    [2748876,5260430,8523002,11049883,14622063,17308428,20041644,22602603,26308712,29264641],
    [2372326,4512811,7140443,9279362,12115459,14295577,16620781,18769845,21732495,24014456],
    [1784040,3442867,5314364,6967087,8933177,10576584,12336414,13976391,16032484,17645090],
    [1498617,2906697,4446084,5849617,7444488,8832683,10308709,11698326,13356809,14697858]
]

# ber = [
#     [0.37, 2.21, 36.93, 760.86,15781.73],
#     [12.58 ,12.53, 12.53, 12.51 ,12.57, 12.54 ,12.53, 12.55 ,12.56, 12.52, 12.56, 12.58, 12.60], 
#     [72.0958, 67.6276, 57.5917, 46.0523, 37.2395, 30.3636, 25.4278, 20.1151, 15.4145, 12.007, 9.38356, 8.0542, 7.13913],
#     # 29,944960
#     [7.64, 12.42, 7.27, 7.44, 4.86, 2.32, 2.78, 2.28, 2.33, 3.67, 2.51, 3.79, 2.54],
#     [1.44, 1.56, 1.66 ,1.77, 1.88, 1.99 ,2.13 ,2.23 ,2.22, 2.32 ,2.38, 2.43, 2.50],
# ]

# comlj =[ 
#     [7.19, 19.18, 407.22, 16484.43, 1000000], 
#     [981.21, 6056.79, 33501.54], 
#     [80.0534, 154.474, 147.495, 156.24, 142.238, 126.787,],
#     #53.900113
#     [90.26, 53.76 ,69.60 ,39.48, 29.66 ,30.99],
#     [21.17, 20.76, 21.36, 21.61, 22.49, 21.74]
# ]

# friender = [
# [],
# [6000 ,6480.0, 6734.8 ,7080 ,7380 ,7380 ,7552.0 ,7980.0, 8280.0 ,8380 ,8480, 8680 ,8797.0 ],
# [],
# #memory error
# [],
# # [3020.79+92.25, 3239.41+75.27, 3421.21+65.72, 59.91,  56.51,  54.43, 53.09 , 52.70, 52.18 ,52.32 ,52.80, 53.21, 53.84],color
# [3020.79+1208.30, 3239.41+783.84, 3421.21+532.43, 3576.06+377.49, 3634.48+264.86, 3829.09+197.03, 
#     3975.41+148.41, 4036.47+111.64, 4086.19+81.81, 4076.47+62.67 , 4078.99+49.82, 4138.42+40.44, 4185.26+33.58],
# ]

# google = [ 
#     [0.33, 0.58,1.12,2.29,5.05,11.31,27.89,74.45,206.75,566.53,1519.12,3636.11,8129.75],
#     [6.53, 6.53, 6.52, 6.51, 6.52 ,6.49, 6.54, 6.56, 6.49, 6.54, 6.55, 6.52, 6.50],
#     [3.96271, 3.94301, 3.86201, 3.71399, 3.24706, 2.66175, 2.13169, 1.78012, 1.61686, 1.57949, 1.60364, 1.67008, 1.76707],
#     #0.318088
#     [1.21 ,1.76,  1.25, 1.56, 1.05, 1.32, 1.39, 1.00 ,1.64, 0.73,  0.85, 0.6, 0.55],
#     [0.62 ,0.62, 0.60  ,0.60, 0.58, 0.54 ,0.49 , 0.43 ,0.45 ,0.32, 0.40  ,0.26, 0.26],
# ]

# ork = [
#     [49.47,89.62,220.10,684.95,2536.43,9824.68],
#     [1114.03, 1610.36 ,1949.50 , 2313.71, 2502.91  ,2603.71, 2679.12 ,2731.61, 2752.67, 2767.74, 2765.66, 2860.72, 2904.02],
#     [441.014, 2823.79, 4687.24, 10200.3, 14633.4],
#     #>5h
#     [135.26 ,178.72, 483.88, 581.19, 2669.30, 2940.57,  30144.23],
#     [212.06, 199.08, 197.97, 208.30, 200.29, 207.14, 213.22, 234.95, 222.41 , 319.57, 309.64, 393.75, 489.95],
# ]
# skitter =[
#     [ 1.42,2.57,7.08,35.94,232.28,1486.84,8774.39],
#     [30.07 ,43.71, 56.33 ,64.57, 68.36 ,69.88 ,69.94, 70.21 ,70.10 ,70.06 ,69.99 ,70.11, 70.47],
#     [70.9152, 175.956, 163.798, 191.195, 221.064, 235.469, 252.879, 290.342, 355.323, 435.796, 545.738, 680.336, 820.721],
#     # 236.330142
#     [4.77, 4.73, 7.74, 6.59, 6.82, 7.05, 10.53, 20.96, 38.97, 43.81, 40.54, 41.75, 33.32],#color
#     [4.32 , 4.68,  4.86 ,4.87, 5.55, 5.43 ,6.78, 6.45, 8.25, 8.88, 9.03 ,10.04 ,10.56],#ccpath
# ] 
# stanford = [
#     [0.12,0.34,1.76,12.01,86.76,571.05,3388.10,15896.47],
#     [3.28, 3.29, 3.28, 3.29, 3.27, 3.28, 3.28, 3.27, 3.28, 3.28 ,3.28, 3.28, 3.27],
#     [ 2.0806, 23.0449, 58.7399, 94.3231, 94.2891, 76.8394,49.9915, 36.5018, 29.7268, 26.3479, 21.1106, 11.6343,10.2308],
#     # 7.643751
#     [0.78  ,0.93, 0.97 ,1.68 ,0.99, 0.90 ,0.65, 0.67 ,0.75, 0.59 ,0.75 ,0.68, 1.46],
#     [0.32 ,0.36 ,0.39 ,0.44 ,0.47 ,0.50 ,0.55 ,0.73 ,0.65 ,0.69 ,0.95 ,0.97 , 0.94],
# ]

# dblp = [
#     [0.06,0.10,0.51,6.96,104.86, 1353.52, 19721.00],
#     [1.396636, 1.408782,1.399590,1.425978,1.417049,1.429389,1.417019,1.432931,1.416402,1.430560,1.414653,1.434913,1.418079],
#     [0.932886, 1.04262, 1.09461, 1.1071, 1.11892, 1.13289, 1.14972, 1.17025, 1.19203, 1.21717, 1.24451, 1.27531, 1.30655],
#     # 0.134239
#     [0.21 ,0.13, 0.09, 0.07, 0.05, 0.05 ,0.04, 0.05 ,0.03, 0.03 ,0.02 ,0.03 ,0.02],
#     [0.13, 0.10, 0.09, 0.08, 0.07 ,0.06 ,0.06, 0.06 ,0.06, 0.06 ,0.06 ,0.06, 0.06]
# ]

# exactNow = [
#     [0.19,0.21,0.24,0.25,0.25,0.28,0.41,0.52,0.65,0.68,0.7,0.67,0.71],#sta
#     [],#dblp
#     [0.75,0.8,0.88,0.94,0.96,1,1.21,1.32,2.27,2.47,2.79,2.92,3.04], #ber
#     [0.47,0.51,0.59,0.68,0.77,0.84,0.88,0.84,0.75,0.64,0.53,0.43,0.34],#goo
#     [2.83,2.95,3.09,3.16,3.2,3.28,3.37,3.4,3.41,3.41,3.39,3.38,3.4],#ski
#     [101.46,104.93,110.68,115.42,121.74,125.89,134.19,138.83,144.15,151.85,158.83,166.09,174.49],#ork
#     [13.57,14.35,15.04,15.51,15.87,16.06,16.19,16.19,16.15,16.02,15.93,15.81,15.74],#lj
#     [2206.97,  2271.22 ,2374.36 ,2374.52, 2431.87, 2492.33 ,2637.15, 2647.86, 2669.46 ,2645.87 ,2676.92, 2658.04 ,2662.44],
# ]

# exactPre = [
#     [0.16,0.19,0.21,0.22,0.22,0.25,0.32,0.35,0.39,0.41,0.4,0.45,0.47],#sta
#     [],#dblp
# [0.71,0.74,0.81,0.85,0.87,0.92,1.03,1.06,1.17,1.25,1.31,1.34,1.36,], #ber
# [0.35,0.38,0.43,0.45,0.47,0.47,0.46,0.42,0.36,0.31,0.27,0.22,0.18,],#goo
# [2.87,3.28,3.52,3.62,3.93,3.73,4.17,3.97,4.07,4.12,4.2,4.32,4.43,],#ski
# [101.46,104.93,110.68,115.42,121.74,125.89,134.19,138.83,144.15,151.85,158.83,166.09,174.49],#ork
# [13.26,14.68,15.57,16.58,17.34,19.54],#lj
# [3020.79,3239.41,3421.21,3533.8,3576.06,3634.48,3829.09,3975.41,4036.47,4086.19,4076.47,4078.99,4138.42,4185.26],
# ]


data_time = [prearray_time,stable_time,stree_time]
data_size=[prearray_size,stable_size,stree_size]
# dName = ['web-Stanford', 'com-DBLP', 'web-BerkStan', 'web-Google', 'as-Skitter','com-Orkut'
# ,'com-LiveJournal', 'com-Friendster']
time_name=['Prefix Array', 'STable', 'STree']
size_name=time_name
# dName = ['Prefix Array', 'STable', 'STree', 'Prefix Array', 'STable','STree']
enumerate_char = ['a','b','c','d','e','f']
lim=[[0,3000],[0,40000],[1000,7000],[0,8*10**7],[0,25*10**7],[0,35*10**6]]
the_ticks=[
    [0,500,1000,1500,2000,2500,3000],
    [x*5000 for x in range(9)],
    [x*1000 for x in range(1,8)],
    [x*10**7 for x in range(9)],
    [x*50000000 for x in range(6)],
    [x*5000000 for x in range(8)]
]
# ticks_num=[8,7,7,6,10,7]
# z = [1,1,1,1,1,1]
# xx = [5,5,5,5,5,5]
# inf = [35000,38000,35000,35000,35000,30000,30000,10**4+1300]
# lim = [18000,10000,35000,35000,10000,30000,30000,10**4+1300]

# k = 0
# while alg[k] != 'DPColorPath':
#     k = k + 1

# for i in range(len(data)):
#     d = data[i][k]
#     for j in range(3, len(d)):
#         if(j >= len(exactPre[i])):
#             break
#         if(j >= len(exactNow[i])):
#             break
#         d[j] = d[j] + exactNow[i][j] - exactPre[i][j]

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
# plt.rcParams['font.sans-serif'] = ['Arial']  # 如果要显示中文字体,则在此处设为：SimHei
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

lw = 1.5
x=[i for i in range(1,11)]

for i in range(len(time_name)):
    plt.subplot(2,3,i+1)

    plt.xlabel('batch of edges',fontsize=15)
    plt.ylabel('time(ms)',fontsize=15)
    plt.title('('+enumerate_char[i]+') '+time_name[i],fontsize=15, y=-0.4, fontweight='ultralight')

    data_series=data_time[i]
    for j in range(len(data_series)):
        plt.plot(x,data_series[j],marker=lab[j],color=col[j],label=create_dataset[j],
                    linewidth=lw,markerfacecolor='none', markersize=12)
    
    plt.ylim(lim[i])
    plt.xticks(x,fontsize=14)

    # num_ticks=ticks_num[i]
    # locs=[lim[i][0]]
    # y_step=(lim[i][1]-lim[i][0])/(num_ticks-1)
    # for j in range(num_ticks-1):
    #     locs.append(locs[-1]+y_step)
    
    plt.yticks(the_ticks[i],[str(x) for x in the_ticks[i]],fontsize=14)

    if i==1:
        plt.legend(loc=9,ncol=len(create_dataset),bbox_to_anchor=(0.5, 1.27))
        leg = plt.gca().get_legend()
        ltext = leg.get_texts()
        plt.setp(ltext, fontsize=15, fontweight='bold' )  # 设置图例字体的大小和粗细

for i in range(len(size_name)):
    plt.subplot(2,3,i+4)
    plt.xlabel('batch of edges',fontsize=15)
    plt.ylabel('space($10^6$ edges)',fontsize=15)
    plt.title('('+enumerate_char[i+3]+') '+size_name[i],fontsize=15, y=-0.4, fontweight='ultralight')
    data_series=data_size[i]
    for j in range(len(data_series)):
        plt.plot(x,data_series[j],marker=lab[j],color=col[j],label=create_dataset[j],
                    linewidth=lw,markerfacecolor='none', markersize=12)

    plt.ylim(lim[i+3])
    plt.xticks(x,fontsize=14)
    plt.yticks(the_ticks[i+3],[str(x//1000000) for x in the_ticks[i+3]],fontsize=14)



# for i in range(len(dName)):
#     plt.subplot(2, 4, i+1)

#     plt.xlabel('k', fontsize=15)
#     plt.ylabel("Time(s)", fontsize=15)   
#     plt.yscale('log')
#     plt.title("({}) ".format(dId[i])+dName[i], fontsize=15, y=-0.4, fontweight='ultralight')

#     for j in range(len(alg)):
#         if(len(data[i][j]) == 0):
#             if dName[i] == 'Friendster':
#                 plt.plot([x for x in range(5, 16, 2)], [10**4+1100 for x in range(5, 16, 2)], marker=lab[j], color=col[j], 
#                     label=alg[j], linewidth=lw, markerfacecolor='none', markersize=12)
#             continue
#         d = data[i][j]
        
#         x = []
#         if dName[i] == 'LiveJournal':
#             for t in range(4, len(d)+3, 1):
#                 x.append(t)
#         else:
#             for t in range(5, len(d)+3, 2):
#                 x.append(t)

#         y = []
#         for t in x:
#             if d[t-3] < inf[i] and t-3<len(d):
#                 y.append(d[t-3])
#             else:
#                 y.append(inf[i])
        
#         if dName[i] != 'LiveJournal':
#             while len(y) < 6:
#                 x.append(x[-1]+2)
#                 y.append(inf[i])
#         else:
#             while len(y) < 5:
#                 x.append(x[-1]+1)
#                 y.append(inf[i])

#         if dName[i] == 'Friendster':
#             plt.yscale('linear')

#         plt.plot(x, y, marker=lab[j], color=col[j],
#             label=alg[j], linewidth=lw, markerfacecolor='none', markersize=12)
#         if dName[i] == 'webGoogle':
#             print(x, y)
   
#     plt.ylim([0, lim[i]])
#     ticks = [10**t for t in range(z[i], xx[i])]
#     ticks.append(inf[i])
#     labels = ticks

#     labels = ['$10^{'+'{}'.format(str(i))+'}$' for i in range(z[i], xx[i])]

#     labels.append('INF')
   
#     plt.xticks([i for i in x], fontsize=14)
#     ax = plt.gca()
#     ax.yaxis.set_ticks(ticks)
#     ax.yaxis.set_ticklabels(labels, fontsize=14)

#     if i == 1:
#         plt.legend(loc=9, numpoints=1, ncol=len(alg)
#                         , bbox_to_anchor=(0.65,0.3,1,1))
#         leg = plt.gca().get_legend()
#         ltext = leg.get_texts()
#         plt.setp(ltext, fontsize=15, fontweight='bold' )  # 设置图例字体的大小和粗细

plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.3,hspace=0.60)
fig = plt.gcf()
fig.set_size_inches(20, 8)
plt.show()
fig.savefig('./index_update_noratio.pdf',bbox_inches='tight', format='pdf') 
plt.close()

# print(2000*3, 2160*3.0, 2260*2.98, 2360*3, 2460*3, 2460*3, 
#     2560*2.95, 2660*3., 2760*3.0, 3060*3, 3360*3, 3560*3, 3660*2.95)


# ama=[ 381473, 692634, 839713, 862125,  838047, 801738]
# google= [1344429, 1754363, 2070058 ,2294787, 2393186, 2510759, 2570742 ,2556452 ,2536756 ,2489182 ,2402669 ,2308335 ,2200116]
# gowlla  =[498068 ,1689166, 497703, 1692445, 2030488, 2179035 ,2369108 ,2579640 ,2757584 ,2915957, 2992733, 3064002, 3001384 ,2950010, 2836370]
# ork = [ 10586105, 12778045, 47850174,92193449,114602642, 124881988
# , 131458884, 142067233, 148893397, 158087150, 154286218
# , 122558552, 119927358
# ]
# goo2=[
# 3.283822,
# 3.287095,
# 3.284652,
# 3.292665,
# 3.270897,
# 3.277068,
# 3.284509,
# 3.272466,
# 3.277414,
# 3.278208,
# 3.276467,
# 3.282245,
# 3.267974,
# ]
# # data = ["skitter.txt","google.txt","berkstan.txt","stanford.txt"]
# for i in ama:
#     print("{:.2f}".format(i / 1000000), end=' ')
# print()
# for i in google:
#     print("{:.2f}".format(i / 1000000), end=' ')
# print()
# for i in gowlla:
#     print("{:.2f}".format(i / 1000000), end=' ')
# print()
# for i in ork:
#     print("{:.2f}".format(i / 1000000), end=' ')
# print()
# for i in goo2:
#     print("{:.2f}".format(i ), end=' ')

