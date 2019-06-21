import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt


football_df = pd.read_csv("21st_club_data.csv", encoding = 'unicode_escape')

#Midfielders Only
football_df = football_df[football_df.position == 'Midfielder']
#print(football_df.columns)
football_df = football_df[['name','team','season', 'minutes_played',
                           'ground_passes', 'ground_passes_successful',
                           'ground_interceptions', 'headed_interceptions',
                           'blocks','tackles', 'tackles_successful',
                           'defensive_ground_duels', 'defensive_ground_duels_successful',
                           'defensive_aerial_duels', 'defensive_aerial_duels_successful',
                           'headed_passes','headed_passes_successful','high_passes', 'high_passes_successful',
                           ]]
#print(football_df.head())


football_df['matches'] = football_df['minutes_played'] / 90

#defensive 
football_df['tackle_%'] = football_df['tackles_successful'] / football_df['tackles']
football_df['def_ground_duel_%'] = football_df['defensive_ground_duels_successful'] / football_df['defensive_ground_duels']
football_df['def_aerial_duel_%'] = football_df['defensive_aerial_duels_successful'] / football_df['defensive_aerial_duels']
football_df['interceptions'] = football_df['ground_interceptions'] + football_df['headed_interceptions']
football_df['ground_inters_pm'] = football_df['ground_interceptions'] / football_df['matches']
football_df['blocks_pm'] = football_df['blocks'] / football_df['matches']
football_df['interceptions_pm'] = football_df['interceptions'] / football_df['matches']
#attacking 
football_df['ground_pass_%'] = football_df['ground_passes_successful'] / football_df['ground_passes']
football_df['headed_pass_%'] = football_df['headed_passes_successful'] / football_df['headed_passes']
football_df['high_pass_%'] = football_df['high_passes_successful'] / football_df['high_passes']


football_df = football_df[['name', 'season', 'tackle_%', 'interceptions_pm', 'ground_pass_%', 'blocks_pm', 'def_ground_duel_%',  'def_aerial_duel_%', 'minutes_played']]


wil_ndi = football_df[football_df['name'] == 'W. Ndidi']
#wil_ndi.to_csv('wil_ndi.csv')


leicester_boys = football_df[(football_df['name'] == 'H. Choudhury') | (football_df['name'] == 'N. Mendy') |
                             (football_df['name'] == 'M. James') | (football_df['name'] == 'Y. Tielemans') |
                             (football_df['name'] == 'D. Amartey')
                             ]
#leicester_boys.to_csv('leicester_boys.csv')



#players i think could replace Ndidi before considering the data
dm_choices = football_df[(football_df['name'] == 'Rúben Neves') | (football_df['name'] == 'D. Rice') |
                         (football_df['name'] == 'E. Konsa')
                        ]
#dm_choices.to_csv('dm_choices.csv')



#players with statistics better than Ndidi's
bet_ndi = football_df[(football_df['tackle_%'] >= 0.48) & (football_df['interceptions_pm'] >= 2.03) &
                      (football_df['ground_pass_%'] >= 0.89)
                     ]
#bet_ndi.to_csv('bet_ndi.csv')




#building a bar chart of the players that have potential to replace Ndidi
final_bar_chart = football_df[((football_df['name'] == 'W. Ndidi') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'H. Choudhury') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'D. Amartey') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'Rúben Neves') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'D. Rice') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'E. Konsa') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'R. Morrison'))
                              ]


names = ['Rúben Neves', 'W. Ndidi', 'H. Choudhury', 'E. Konsa', 'D. Rice', 'R. Morrison', 'D. Amartey']





N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.3       # the width of the bars


fig = plt.figure()
ax = fig.add_subplot(111)


interceptions_pm = []
for stat in final_bar_chart['interceptions_pm']:
    interceptions_pm.append(stat)
interceptions_pm = np.array(interceptions_pm) * 100
rects1 = ax.bar(ind, interceptions_pm, width, color='r')


blocks_pm = []
for stat in final_bar_chart['blocks_pm']:
    blocks_pm.append(stat)
blocks_pm = np.array(blocks_pm) * 100
rects2 = ax.bar(ind+width, blocks_pm, width, color='g')


ax.set_ylabel('Average Per Match')
ax.set_xticks(ind+(width*0.5))
ax.set_xticklabels( ('Rúben Neves', 'W. Ndidi', 'H. Choudhury', 'E. Konsa', 'D. Rice', 'R. Morrison', 'D. Amartey') )
ax.legend( (rects1[0], rects2[0] ), ('Inters PM', 'Blocks PM') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()


width = 0.15
figure = plt.figure()
bx = figure.add_subplot(111)

tackles = []
for stat in final_bar_chart['tackle_%']:
    tackles.append(stat)
tackles = np.array(tackles) * 100
rects3 = bx.bar(ind-(width *2), tackles, width, color='b')

ground_pass = []
for stat in final_bar_chart['ground_pass_%']:
    ground_pass.append(stat)
ground_pass = np.array(ground_pass) * 100
rects4 = bx.bar(ind - width, ground_pass, width, color='k')

def_ground_duel = []
for stat in final_bar_chart['def_ground_duel_%']:
    def_ground_duel.append(stat)
def_ground_duel = np.array(def_ground_duel) * 100
rects5 = bx.bar(ind, def_ground_duel, width, color='y')

def_aerial_duel = []
for stat in final_bar_chart['def_aerial_duel_%']:
    def_aerial_duel.append(stat)
def_aerial_duel = np.array(def_aerial_duel) * 100
rects6 = bx.bar(ind + width, def_aerial_duel, width, color='g')


bx.set_ylabel('Percentages %')
bx.set_xticks(ind- (width*(2/3)))
bx.set_xticklabels( ('Rúben Neves', 'W. Ndidi', 'H. Choudhury', 'E. Konsa', 'D. Rice', 'R. Morrison', 'D. Amartey') )
bx.legend( (rects3[0], rects4[0], rects5[0], rects6[0],), ('Tackle %', 'Ground Pass %', 'Def Ground Duel %', 'Def Aerial Duel %') )


def autolabelb(rects):
    for rect in rects:
        h = rect.get_height()
        bx.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabelb(rects3)
autolabelb(rects4)
autolabelb(rects5)
autolabelb(rects6)


plt.show()

