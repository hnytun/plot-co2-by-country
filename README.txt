this is assignment 6, this readme will include all instructions to run my program


installing pandas

http://pandas.pydata.org/pandas-docs/stable/install.html

for ubuntu you might need to do this(as i had to)

sudo apt-get install python3-dev

sudo apt-get install python3-setuptools

then run the setup file in the .tar

For the other platforms i recommend just using the link

installing matplotlib

http://matplotlib.org/users/installing.html

the link says that matplotlib is packaged in almost every major linux distro,
but includes installing instructions for other platforms.

--------------------Instructions to run the program----------------------------

For testing the plots(that are saved in the static folder):

enter "python3 temperature_CO2_plotter.py" (the parameters are changed in the main code)


For testing the website with the plots

run web_visualization.py and enter localhost:5000 or 127.0.0.1:5000
in your browser(I have used chrome)
Here you can mess around with the text-boxes to make different plots.
Note that some arguments result in the plots being weird or invalid,
for example as mentioned on the site, making a plot of temperatures of
max 0 degrees on y-axis in june will generate nothing, so here i just
write "no data" or something like that on the axis of the plot.
It might be confusing that the plot actually has some plottings in these
cases, but this is just a glitch(i think), and the plotting is very wrong
(not valid)

I do not check for errors in the text boxes, so please try to only write valid inputs
Years should be numbers in format YYYY
Month should be on the format of July, February etc
min and max should be numbers
For carbon emissions by country (the most bottom plot)
you should keep the threshold small to avoid many values
which results in cluttering, so a nice test could be:
year: 2010
minY: 0.6
maxY: 1.0
