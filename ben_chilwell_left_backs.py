import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt

football_df = pd.read_csv("21st_club_data.csv", encoding = 'unicode_escape')

#Defenders only
football_df = football_df[football_df['position'] == 'Defender']
#print(football_df.columns)
football_df = football_df[['name', 'age','team','season', 'minutes_played',
                           'defensive_ground_duels', 'defensive_ground_duels_successful',
                           'tackles', 'tackles_successful',
                           'crosses', 'crosses_successful',
                           'passes_received', 'passes_received_attacking_third',
                           'offensive_ground_duels', 'offensive_ground_duels_successful',
                           'ground_passes', 'ground_passes_successful',
                           'ground_passes_attacking_third', 'ground_passes_attacking_third_successful' ,]]
#print(football_df.head())

football_df['def_gro_duel_%'] = football_df['defensive_ground_duels_successful'] / football_df['defensive_ground_duels']
football_df['tackles_%'] = football_df['tackles_successful'] / football_df['tackles']
football_df['crosses_%'] = football_df['crosses_successful'] / football_df['crosses']
football_df['pass_loc_%'] = football_df['passes_received_attacking_third'] / football_df['passes_received']
football_df['off_gro_duel_%'] = football_df['offensive_ground_duels_successful'] / football_df['offensive_ground_duels']
football_df['atk_pass_%'] = football_df['ground_passes_attacking_third_successful'] / football_df['ground_passes_attacking_third']


football_df = football_df[['name', 'season', 'age','team',
                           'def_gro_duel_%', 'tackles_%', 'crosses_%',
                           'pass_loc_%','off_gro_duel_%', 'atk_pass_%',
                           'minutes_played'
                           ]]


ben_chill = football_df[football_df['name'] == 'B. Chilwell']
#ben_chill.to_csv('ben_chillwell.csv')


chr_fuch = football_df[football_df['name'] == 'C. Fuchs']
#chr_fuch.to_csv('christian_fuchs.csv')


#players i think could replace chilwell before considering the data
lb_choices = football_df[(football_df['name'] == 'J. Dasilva') | (football_df['name'] == 'L. Kelly') | (football_df['name'] == 'L. Shaw') ]
#lb_choices.to_csv('lb_choices.csv')


#players with statistics better than Chilwell's
bet_chil = football_df[(football_df['def_gro_duel_%'] >= 0.6) & (football_df['tackles_%'] >= 0.5)
                                & (football_df['crosses_%'] >= 0.3) & (football_df['off_gro_duel_%'] >= 0.5)]
#bet_chil.to_csv('bet_chil.csv')


football_df = football_df[['name','season', 'def_gro_duel_%', 'tackles_%', 'crosses_%',
                           'pass_loc_%','off_gro_duel_%', 'atk_pass_%','minutes_played']]



#building a bar chart of the players that have potential to replace Chilwell
final_bar_chart = football_df[((football_df['name'] == 'B. Chilwell') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'L. Kelly') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'L. Shaw') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'J. Dasilva') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'T. Kongolo') & (football_df['season'] == 2018))
                              ]
print(final_bar_chart)


names = ['B. Chilwell', 'L. Kelly', 'L. Shaw', 'J. Dasilva', 'T. Kongolo']





N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)


def_gro_due = []
for stat in final_bar_chart['def_gro_duel_%']:
    def_gro_due.append(stat)
def_gro_due = np.array(def_gro_due)
def_gro_due = def_gro_due * 100

rects1 = ax.bar(ind-width, def_gro_due, width, color='r')

tackles = []
for stat in final_bar_chart['tackles_%']:
    tackles.append(stat)
tackles = np.array(tackles)
tackles = tackles * 100
rects2 = ax.bar(ind, tackles, width, color='g')

crosses = []
for stat in final_bar_chart['crosses_%']:
    crosses.append(stat)
crosses = np.array(crosses)
crosses = crosses * 100
rects3 = ax.bar(ind+width, crosses, width, color='b')

pass_location = []
for stat in final_bar_chart['pass_loc_%']:
    pass_location.append(stat)
pass_location = np.array(pass_location)
pass_location = pass_location * 100
rects4 = ax.bar(ind+width*2, pass_location, width, color='k')

off_gro_duel = []
for stat in final_bar_chart['off_gro_duel_%']:
    off_gro_duel.append(stat)
off_gro_duel = np.array(off_gro_duel)
off_gro_duel = off_gro_duel * 100
rects5 = ax.bar(ind+width*3, off_gro_duel, width, color='y')

#Leaving out successful ground passes in the final third as it's the least important statistic
#This is so the chart is easier to read and has less of an information overload

'''
atk_pass = []
for stat in final_bar_chart['atk_pass_%']:
    atk_pass.append(stat)
atk_pass = np.array(atk_pass)
atk_pass = atk_pass * 100
rects6 = ax.bar(ind+width*3, atk_pass, width, color='m')
'''


ax.set_ylabel('Percentages %')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Da Silva', 'Kelly', 'Chilwell',  'Shaw', 'Kongolo') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], ), ('DGD %', 'Tackle %', 'Cross %', 'Pass Loc %', 'OGD %') )
#rects6[0] 'Atk Pass %'


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
#autolabel(rects6)

plt.show()
