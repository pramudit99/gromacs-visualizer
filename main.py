import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def read_xvg(filename):
	xvgfile = open(filename)
	lines = xvgfile.readlines(1200)
	legend = []
	for i in range(len(lines)):
		line = lines[i]
		if line.startswith('#'):
			continue
		if line.startswith('@    title'):
			plotTitle = line.split('"')[-2]
			continue
		if line.startswith('@    xaxis'):
			xLabel = line.split('"')[-2]
			continue
		if line.startswith('@    yaxis'):
			yLabel = line.split('"')[-2]
			continue
		if line.startswith('@ subtitle'):
			continue
		if line.startswith('@ s'):
			legend.append(line.split('"')[-2])
			continue
		if line.startswith('@'):
			continue
		else:
			break
	xvgfile.close()
	
	cols = ['x']
	if len(legend) == 0:
		legend = ['y']
	cols = cols + legend
	preData = pd.read_csv(filename,header=i-1,names=['x'])['x'].str.split()
	data = pd.DataFrame(data=np.array(list(preData)),columns=cols)
	data = data.astype('float')
	if xLabel == 'Time (ps)':
		xLabel = 'Time (ns)'
		data.x = data.x/1000
	return(plotTitle,xLabel,yLabel,legend,data)


def main():
	flag = False	
	if '-nx' in sys.argv:
		sys.argv.remove('-nx')
		flag = True
	
	if flag == True:
		for i in range(len(sys.argv)-1):
			(plotTitle,xLabel,yLabel,legend,data) = read_xvg(sys.argv[i+1])

			for j in range(len(legend)):
				plt.plot(data.x,data[legend[j]])
			plt.title(plotTitle)
			plt.xlabel(xLabel)
			plt.ylabel(yLabel)
			plt.legend(legend)
			plt.get_current_fig_manager().set_window_title(str(sys.argv[i+1]))
			plt.show()
	
	else:
		for i in range(len(sys.argv)-1):
			(plotTitle,xLabel,yLabel,legend,data) = read_xvg(sys.argv[i+1])
			plt.plot(data.x,data[legend[0]])
		plt.title(plotTitle)
		plt.xlabel(xLabel)
		plt.ylabel(yLabel)
		plt.legend(legend)
		plt.get_current_fig_manager().set_window_title(plotTitle)
		plt.legend(sys.argv[1::])
		plt.show()

main()
