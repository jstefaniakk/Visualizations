# Bokeh timeseries from link

#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas

#prepare data
df=pandas.read_csv("http://finance.google.com/finance/historical?cid=4112&startdate=Jan+1%2C+2009&enddate=Aug+2%2C+2012&num=30&ei=YhIzWsipFIqMjAH6m5TwDg&output=csv", parse_dates=["Date"])
p=figure(width=500,height=250,x_axis_type="datetime") #,responsive=True
p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)

output_file("Timeseries.html")
show(p)
