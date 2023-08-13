import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('SALES RECORD.csv')

mno=df['month']
qr=df['quarter']
fcream=df['facecream']
fwash=df['facewash']
tpaste=df['toothpaste']
bsoap=df['bathingsoap']
shampoo=df['shampoo']
moisture=df['moisturizer']
tu=df['total_units']
tp=df['total_profit']
sal=df['sales']

def submenu2():
    ch2=0
    while ch2!=4:
        print('\n---------------------------------------')
        print('        DATA VISUALIZATION MENU          ')
        print('-----------------------------------------')
        print('1.LINE GRAPH:MONTH WISE-UNITS SIOLD FOR EACH PRODUCT')
        print('2.MULTI BAR PLOT FOR PRODUCT WISE UNITS SOLD')
        print('3.HISTOGRAM-COMPANY PROFIT MONTHS')
        print('4.RETURN TO MAIN MENU')
        ch2=int(input('\nchoose an option for data visualization'))
        if ch2==1:
            plt.plot(mno,fcream,label='facecream',color='r',linestyle='-')
            plt.plot(mno,fwash,label='facewash',color='b',linestyle='-')
            plt.plot(mno,tpaste,label='toothpaste',color='g',linestyle='-')
            plt.plot(mno,bsoap,label='bathing soap',color='k',linestyle='-')
            plt.plot(mno,shampoo,label='shampoo',color='y',linestyle='-')
            plt.plot(mno,moisture,label='moisturizer',color='m',linestyle='-')
            plt.xticks(np.arange(0,13,1),fontsize=12,rotation=30)
            plt.yticks(np.arange(1000,15000,1000),fontsize=8,rotation=30)
            plt.xlabel('month number',fontsize=16)
            plt.ylabel('sales unit',fontsize=16)
            plt.legend(loc='upper left')
            plt.title('sales data-product wise unit sold',fontsize=16)
            plt.grid(True)
            plt.show()
        elif ch2==2:
            x1=np.arange(1,13,1)
            x2=x1+0.15
            x3=x2+0.15
            x4=x3+0.15
            x5=x4+0.15
            x6=x5+0.15
            plt.bar(x1,fcream,tick_label=mno,width=0.15,label='facecream')
            plt.bar(x2,fwash,tick_label=mno,width=0.15,label='facewash')
            plt.bar(x3,tpaste,tick_label=mno,width=0.15,label='toothpaste')
            plt.bar(x4,bsoap,tick_label=mno,width=0.15,label='bathing soap')
            plt.bar(x5,shampoo,tick_label=mno,width=0.15,label='shampoo')
            plt.bar(x6,moisture,tick_label=mno,width=0.15,label='moisturizer')
            plt.xticks(x4,labels=mno,fontsize=10,rotation=0)
            plt.yticks(np.arange(1000,12000,1000),fontsize=8,rotation=0)
            plt.xlabel('names',fontsize=16)
            plt.ylabel('marks',fontsize=16)
            plt.legend()
            plt.grid(True)
            plt.title('multiple bar plot-term wise comparison',fontsize=16)
            plt.show()
        elif ch2==3:
            plt.hist(tp,bins=4,range=(150000,350000),edgecolor='k')
            plt.xticks(np.arange(150000,400000,50000),fontsize=12,rotation=30)
            plt.yticks(np.arange(0,9,1),fontsize=12,rotation=30)
            plt.xlabel('total profit',fontsize=16)
            plt.ylabel('months',fontsize=16)
            plt.legend()
            plt.grid(True)
            plt.title('histogram-company profit months',fontsize=16)
            plt.show()
        elif ch2==4:
            mainmenu()
        else:
            print('wrong input')

def submenu3():
    ch1=0
    while ch1!=6:
        print('\n-------------------------------------------')
        print('           DATA ANALYSIS MENU                ')
        print('---------------------------------------------')
        print('1.FIND MAX,MIN,MEAN,SUM OF TOTAL UNITS SOLD')
        print('2.DISPLAY THE DETAILS OF SALES OF THOSE 3 MONTHS WHICH HAVE HIGHEST SALES')
        print('3.DISPLAY THE DETAILS OF SALES OF THOSE 3 MONTHS WHICH HAVE LOWEST SALES')
        print('4.RETURN BACK TO MAIN MENU')
        ch1=int(input('\nchoose an option for data analysis'))
        if ch1==1:
            print('max,min,mean,sum of total units sold and total profit:')
            print(df.aggregate({'total_units':['max','min','mean','sum'],'total_profit':['max','min','mean','sum']}))
        elif ch1==2:
            print('details of sales for 3 months with highest sales')
            print(df.sort_values('total_profit',ascending=False).head(3))
        elif ch1==3:
            print('details of sales for 3 months with lowest sales')
            print(df.sort_values('total_profit',ascending=False).tail(3))
        elif ch1==4:
            mainmenu()
        else:
            print('wrong input')
        
            

def mainmenu():
    choice=0
    while choice!=4:
        print('\n--------------------------------------')
        print('      24/7 STORE SALES DATA-MAIN MENU             ')
        print('----------------------------------------')
        print('1.DISPLAY DATA')
        print('2.DATA VISUALIZATION')
        print('3.DATA ANALYSIS')
        print('4.EXIT')
        choice=int(input('\nchoose an option from the menu:'))
        if choice==1:
            print('display data')
            print(df)
            print(df.columns)
        elif choice==2:
            submenu2()
        elif choice==3:
            submenu3()
        elif choice==4:
            print('THANKU FOR VISITING:)')
            break
        else:
            print('wrong input')

mainmenu()
