import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('C:/Users/MUDIT JAIN/Desktop/tvshows.csv')

def submenu3():
    ch1=0
    while ch1!=4:
        print('\n---------------------------------------------------')
        print('             DATA ANALYSIS MENU                      ')
        print('---------------------------------------------------')
        print('1.FIND MAX,MIN,MEAN NUMBER OF imdb RATINGS')
        print('2.DISPLAY DETAILS OF TOP 3 TV SERIES')
        print('3.DISPLAY DETAILS OF BOTTOM 3 TV SERIES')
        print('4.GO BACK TO MAIN MENU')
        ch1=int(input('\nchoose a option for data analysis'))
        if ch1==1:
            print('max,min,mean of seasons are')
            print(df.aggregate({'imdbRating':['max','min','mean']}))
        elif ch1==2:
            print('details of 3 TV Series with highest imdb rating')
            print(df.sort_values('imdbRating',ascending=False).head(3))
        elif ch1==3:
            print('details of 3 TV Series with lowest imdb rating')
            print(df.sort_values('imdbRating',ascending=False).tail(3))
        elif ch1==4:
            mainmenu()
        else:
            print('wrong input')

def mainmenu():
    choice=0
    while True:
        print('\n---------------------------------------------------')
        print('     TV SHOWS DATA-MAIN MENU                         ')
        print('---------------------------------------------------')
        print('     1.DISPLAY DATA                                  ')
        print('     2.DATA VISUALIZATION                            ')
        print('     3.DATA ANALYSIS                                 ')
        print('     4.EXIT                                          ')
        choice=int(input('\nChoose a option from the menu:'))
        if choice==1:
            print('DISPLAY DATA')
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

            
def submenu2():
    ch2=0
    while ch2!=3:
        print('\n---------------------------------------------------')
        print('             DATA VISUALIZATION MENU                 ')
        print('---------------------------------------------------')
        print('1.LINE GRAPH:RATING OF TV SHOWS')
        print('2.LINE GRAPH:YEAR OF RELEASE')
        print('3.RETURN BACK TO MAIN MENU')
        ch2=int(input('\nchoose an option from above menu'))
        if ch2==1:
            f=pd.DataFrame(df)
            a=f.loc[:,'Title']
            b=f.loc[:,'imdbRating']
            plt.plot(b,a,c='b',marker='o')
            plt.ylabel('Title', fontsize=16)
            plt.xlabel('No of Votes', fontsize=16)
            plt.title('TOP TV SHOWS ',fontsize=20)
            plt.show()
        elif ch2==2:
            f=pd.DataFrame(df)
            a=f.loc[:,'Title']
            b=f.loc[:,'Year']
            plt.plot(b,a,c='g',marker='o')
            plt.ylabel('Title',fontsize=16)
            plt.xlabel('year',fontsize=16)
            plt.title('YEAR OF RELEASE',fontsize=20)
            plt.show()
        elif ch2==3:
            mainmenu()
        else:
            print('wrong input')
            
            

mainmenu()
