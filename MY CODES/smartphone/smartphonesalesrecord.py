import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('smartphonesales.csv')

mno=df['month']
qr=df['quarter']
apple=df['apple']
samsung=df['samsung']
xiomi=df['xiomi']
oneplus=df['oneplus']
realme=df['realme']
oppo=df['oppo']
tu=df['total_units']
tp=df['total_profit']
sal=df['sales']

def submenu2():
    ch2=0
    while ch2!=4:
        print('\n---------------------------------------')
        print('        DATA VISUALIZATION MENU          ')
        print('-----------------------------------------')
        print('1.LINE GRAPH:MONTH WISE-UNITS SOLD OF EACH BRAND')
        print('2.MULTI BAR PLOT FOR BRAND WISE UNITS SOLD')
        print('3.HISTOGRAM-STORE PROFIT MONTHS')
        print('4.RETURN TO MAIN MENU')
        ch2=int(input('\nchoose an option for data visualization'))
        if ch2==1:
            plt.plot(mno,apple,label='apple',color='r',linestyle='-')
            plt.plot(mno,samsung,label='samsung',color='b',linestyle='-')
            plt.plot(mno,xiomi,label='xiomi',color='g',linestyle='-')
            plt.plot(mno,oneplus,label='oneplus',color='k',linestyle='-')
            plt.plot(mno,realme,label='realme',color='y',linestyle='-')
            plt.plot(mno,oppo,label='oppo',color='m',linestyle='-')
            plt.xticks(np.arange(0,13,1),fontsize=12,rotation=30)
            plt.yticks(np.arange(15,55,10),fontsize=8,rotation=30)
            plt.xlabel('month',fontsize=16)
            plt.ylabel('sales unit',fontsize=16)
            plt.legend(loc='upper left')
            plt.title('sales data-brand wise unit sold',fontsize=16)
            plt.grid(True)
            plt.show()
        elif ch2==2:
            x1=np.arange(1,13,1)
            x2=x1+0.15
            x3=x2+0.15
            x4=x3+0.15
            x5=x4+0.15
            x6=x5+0.15
            plt.bar(x1,apple,tick_label=mno,width=0.15,label='apple')
            plt.bar(x2,samsung,tick_label=mno,width=0.15,label='samsung')
            plt.bar(x3,xiomi,tick_label=mno,width=0.15,label='xiomi')
            plt.bar(x4,oneplus,tick_label=mno,width=0.15,label='oneplus')
            plt.bar(x5,realme,tick_label=mno,width=0.15,label='realme')
            plt.bar(x6,oppo,tick_label=mno,width=0.15,label='oppo')
            plt.xticks(x4,labels=mno,fontsize=10,rotation=0)
            plt.yticks(np.arange(10,60,5),fontsize=8,rotation=0)
            plt.xlabel('month',fontsize=16)
            plt.ylabel('sales',fontsize=16)
            plt.legend()
            plt.grid(True)
            plt.title('multiple bar plot-term wise comparison',fontsize=16)
            plt.show()
        elif ch2==3:
            plt.hist(tp,bins=4,range=(150000,250000),edgecolor='k')
            plt.xticks(np.arange(150000,300000,50000),fontsize=12,rotation=30)
            plt.yticks(np.arange(0,9,1),fontsize=12,rotation=30)
            plt.xlabel('total profit',fontsize=16)
            plt.ylabel('months',fontsize=16)
            plt.legend()
            plt.grid(True)
            plt.title('histogram-store profit months',fontsize=16)
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
        print('     SMARTPHONE SALES DATA-MAIN MENU             ')
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
 

            
   

        
