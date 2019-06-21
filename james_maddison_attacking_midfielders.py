import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt


football_df = pd.read_csv("21st_club_data.csv", encoding = 'unicode_escape')

#Midfielders only
football_df = football_df[football_df['position'] == 'Midfielder']

#Exploritory Data Analysis 
#print(football_df.columns)
#print(football_df.describe)
#print(football_df.head())
#print(football_df.tail())


football_df = football_df[['name','team','season', 'minutes_played',
                           'goals', 'assists',
                           'ground_passes_attacking_third', 'ground_passes_attacking_third_successful',
                           'ground_passes_box', 'ground_passes_box_successful',
                           'high_passes_attacking_third', 'high_passes_attacking_third_successful',
                           'high_passes_box', 'high_passes_box_successful',
                           'dribbles', 'dribbles_successful',
                           'offensive_ground_duels', 'offensive_ground_duels_successful',
                           'passes_received_attacking_third', 'passes_received_box',
                           'carries', 'carries_attacking_third', 'carries_box',
                           ]]

#attacking ones
football_df['ground_passes_attacking_third_successful_%'] = football_df['ground_passes_attacking_third_successful'] / football_df['ground_passes_attacking_third']
football_df['passes_received_box_%'] = football_df['passes_received_box'] / football_df['passes_received_attacking_third']
football_df['ground_passes_box_successful_%'] = football_df['ground_passes_box_successful'] / football_df['ground_passes_box']
football_df['offensive_ground_duels_successful_%'] = football_df['offensive_ground_duels_successful'] / football_df['offensive_ground_duels']

#It Would be difficult to explain the importance of these two statistics in a short report
#football_df['carries_attacking_third_%'] = football_df['carries_attacking_third'] / football_df['carries']
#football_df['carries_attacking_third_in_box_%'] = football_df['carries_box'] / football_df['carries_attacking_third']




football_df = football_df[['name', 'season', 'goals', 'assists', 'ground_passes_attacking_third_successful_%',
                           'passes_received_box_%', 'ground_passes_box_successful_%', 'offensive_ground_duels_successful_%',
                           'team'
                           ]]



jam_mad = football_df[football_df['name'] == 'J. Maddison']
#jam_mad.to_csv('james_maddison.csv')


leicester_boys = football_df[(football_df['name'] == 'Adrien Silva') | (football_df['name'] == 'A. King') |
                             (football_df['name'] == 'H. Barnes') | (football_df['name'] == 'Y. Tielemans') |
                             (football_df['name'] == 'B. Kapustka')
                             ]
#leicester_boys.to_csv('Leicester_AM.csv')


#players i think could replace Maddison before considering the data
am_choices = football_df[(football_df['name'] == 'J. Grealish') | (football_df['name'] == 'M. Mount') |
                             (football_df['name'] == 'D. Brooks')
                             ]
#am_choices.to_csv('am_choices.csv')


#players with very good statistics (it was difficult to find anyone note worthy with better statistics)
bet_mad = football_df[(football_df['goals'] >= 3) & (football_df['assists'] >= 3) &
                              (football_df['ground_passes_attacking_third_successful_%'] >= 0.81) & (football_df['passes_received_box_%'] >= 0.07) &
                              (football_df['ground_passes_box_successful_%'] >= 0.72)
                              ]
#bet_mad.to_csv('bet_mad.csv')





#building a bar chart of the players that have potential to replace Maddison
final_bar_chart = football_df[((football_df['name'] == 'J. Maddison') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'J. Grealish') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'M. Mount') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'D. Brooks') & (football_df['season'] == 2018)) |
                              ((football_df['name'] == 'R. Barkley') & (football_df['season'] == 2018)) 
                              ]
print(final_bar_chart)
final_bar_chart[['name','team', 'goals', 'assists']].to_csv('easy_am_data.csv')


names = ['J. Maddison', 'J. Grealish', 'M. Mount', 'D. Brooks', 'R. Barkley']




N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)


gpats = []
for stat in final_bar_chart['ground_passes_attacking_third_successful_%']:
    gpats.append(stat)
gpats = np.array(gpats)
gpats = gpats * 100
rects1 = ax.bar(ind-width, gpats, width, color='r')

prb = []
for stat in final_bar_chart['passes_received_box_%']:
    prb.append(stat)
prb = np.array(prb)
prb = prb * 100
rects2 = ax.bar(ind, prb, width, color='g')


gpbs = []
for stat in final_bar_chart['ground_passes_box_successful_%']:
    gpbs.append(stat)
gpbs = np.array(gpbs) * 100
rects3 = ax.bar(ind+width, gpbs, width, color='b')

ogds = []
for stat in final_bar_chart['offensive_ground_duels_successful_%']:
    ogds.append(stat)
ogds = np.array(ogds)
ogds = ogds * 100
rects4 = ax.bar(ind+width*2, ogds, width, color='y')



ax.set_ylabel('Percentages %')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Barkley', 'Brooks', 'Mount',  'Maddison', 'Grealish' ) )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]  ), ('GPATS', 'PRB', 'GPBS', 'OGDS' ) )



def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.show()
