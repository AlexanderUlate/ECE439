1) #!/usr/bin/python3
2) # -*- coding: utf-8 -*-
3) """
4) Quick demo of graphing data
5) """
6)
7) import numpy as np
8) from matplotlib import pyplot as plt
9)
10) # Enter some data
11) xdata = np.array([-7, -3,-1,0,2,4,8])
12) ydata = np.array([-10,-5,0,13,27,44,76])
13)
14) # Use Matplotlib/Pyplot to plot it. 
15) # Note, many aspects are a lot like MATLAB plotting. 
16) fig = plt.figure()  # create a Figure
17) p = plt.plot(xdata,ydata,'o-r')  # add a plot to it: first xdata, then ydata. "o-r" means "circle markers, with a line, red"
18) plt.xlabel("X Label Here")
19) plt.ylabel("Y Label Here")
20) plt.title("Title Here")
21) #plt.show()  # Sometimes this is necessary to show the plot. But often not. 
22)
23) #If that shows up in the console at right (instead of as a separate window), then go to Tools->Preferences->IPython console-> 
Graphics->Graphics Backend and select "Automatic".
24) print('done')