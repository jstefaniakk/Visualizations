# Bokeh TEmperatrure and Pressure

#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#prepare data
df=pandas.read_excel("verlegenhuken.xlsx", sheetname=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10

p=figure(plot_width=500,plot_height=400,tools='pan',logo=None)

p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"

p.circle(df["Temperature"],df["Pressure"],size=0.5)

#prepare the output
output_file("temperature_pressure.html")

#write the plot in the figure
show(p)

#for more visualisation options see https://bokeh.pydata.org/en/latest/docs/user_guide/styling.html
