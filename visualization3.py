# Bokeh Bachelors

#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#prepare data
df=pandas.read_csv("bachelors.csv")
x=df["Year"]
y=df["Engineering"]

#prepare the output
output_file("Bachelors.html")

#create figure object
f=figure()

#create line plot (you can use circle() or triangle() as well)
f.line(x,y)

#write the plot in the figure
show(f)
