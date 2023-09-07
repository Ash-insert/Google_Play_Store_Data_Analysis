import seaborn as sns

Light_Categorical_Colors = ['#8a3ffc', '#33b1ff', '#007d79', '#ff7eb6', '#fa4d56', '#ffd7d9', '#6fdc8c', '#4589ff', '#d12771', '#d2a106', '#08bdba', '#bae6ff', '#ba4e00', '#d4bbff']
Dark_Categorical_Colors = ['#6929c4', '#1192e8', '#005d5d', '#9f1853' , '#fa4d56', '#570408', '#198038', '#002d9c', '#ee538b', '#b28600', '#009d9a', '#012749', '#8a3800', '#a56eff']
Tab_10 = sns.color_palette('tab10')
Tab_20 =sns.color_palette('tab20')
Tab_5 =  [sns.color_palette('tab20c')[4*i] for i in range(5)]
Blue_Shade = sns.blend_palette(['#edf5ff', '#d0e2ff', '#a6c8ff', '#78a9ff', '#4589ff','#0f62fe', '#0043ce', '#002d9c', '#001d6c', '#001141'], as_cmap=True)
Purple_Shade = sns.blend_palette([ '#e8daff', '#be95ff', '#8a3ffc', '#491d8b', '#1c0f30'], as_cmap=True)
Cyan_Shade = sns.blend_palette(['#bae6ff', '#33b1ff', '#0072c3', '#003a6d', '#1c0f30'], as_cmap=True)
Teal_Shade = sns.blend_palette(['#d9fbfb', '#08bdba', '#007d79', '#004144', '#081a1c'] , as_cmap=True)
Red_Blue_Diverge = sns.blend_palette(['#750e13', '#fa4d56', '#ffd7d9', '#bae6ff', '#1192e8', '#003a6d'], as_cmap=True)
Purple_Teal_Diverge = sns.blend_palette(['#491d8b', '#a56eff', '#e8daff', '#9ef0f0', '#009d9a', '#004144'], as_cmap=True)

List_of_color_discrete = [Light_Categorical_Colors, Dark_Categorical_Colors, Tab_10, Tab_20, Tab_5, 'viridis', 'coolwarm' ]
List_of_color_maps = [Blue_Shade, Purple_Shade, Cyan_Shade, Teal_Shade, Red_Blue_Diverge, Purple_Teal_Diverge, 'viridis', 'coolwarm']