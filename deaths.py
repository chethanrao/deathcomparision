import numpy as np
import matplotlib.pyplot as plt

objects = ('Heart\nDisease', 'Cancer', 'Accidents', 'Chronic\nlower\nrespiratory\ndiseases', 'Stroke\n(cerebrovascular\ndiseases)', 'Alzheimer’s\ndisease','Diabetes','Influenza\nand\n pneumonia','Nephritis,\nnephrotic syndrome,\n and nephrosis','Suicide','Corona Virus')
y_pos = np.arange(len(objects))
deathnumbers = [647457,599108,169936,160201,146383,121404,83564,55672,50633,47173,21000]

plt.bar(y_pos,deathnumbers, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xticks(fontsize=5)
plt.ylabel('Number of deaths')
plt.title('Comparision of factors of deaths in 2017 with covid19 deaths')

plt.show()
