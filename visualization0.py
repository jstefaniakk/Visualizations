# Making a basic bokeh graph
from bokeh.plotting import figure
from bokeh.io import output_file,show

#prepare data
x=[1,2,3,4,5]
y=[10,8,9,8,7]

#prepare the output
output_file("Line.html")

#create figure object
f=figure()

#create line plot (you can use circle() or triangle() as well)
f.triangle(x,y)

#write the plot in the figure
show(f)
