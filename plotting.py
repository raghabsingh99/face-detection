from capture import df
from bokeh.plotting import figure, show, output_file

p=figure(x_axis_type='detection', height=100, width=200, responsolve=True, title="motion graph")
q=p.quad(left=df["start"],right=df["end"],BOTTOM=0,top=1,color='green')
output_file("graph.html")
show(p)