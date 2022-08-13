import pandas as pd
import matplotlib.pyplot as plt

sets = pd.read_csv('data/sets.csv')
sets.head

sets[sets['year'] == 1949]
sets.sort_values('num_parts', ascending=False).head()
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()
sets_by_year['set_num'].tail()
themes_by_year = sets.groupby('year').agg({'theme_id' : pd.Series.nunique})
themes_by_year.rename(columns = {'themes_id' : 'nr_themes'}, inplace = True)
themes_by_year.head()
themes_by_year.tail()
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.set_num[:-2], color='b')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')
parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]
themes = pd.read_csv('data/themes.csv')
themes[themes.name == 'Star Wars']
set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]
set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})
set_theme_count.head()
merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df[:3]
plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
