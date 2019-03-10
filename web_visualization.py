from flask import Flask, render_template, request
from temperature_CO2_plotter import *
import time

app=Flask(__name__)

#this snippet that prevents caching an old plot is taken from source
#http://stackoverflow.com/questions/13768007/browser-caching-issues-in-flask
#by user "The Internet"
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/")
def showImages():
    """Function that plots pictures and renders template with the pictures,
    which is (re)generated and stored in static folder
    This is basically the "home" page that comes up when you
    first enter the localhost:5000 page"""

    #plot co2 and temperature and then add them to the static folder
    #note, this is only the standard plot that is generated
    #when we enter the root folder of our server(route="/")
    #this is to avoid error by always having a standard plot
    #for both csv files, even before user puts in their own arguments
    #and create a plot
    plot_Temperature("temperature.csv",0,3000,"June",(0,21))
    plot_CO2("co2.csv",0,3000,(0,1000))

    #return the main html page which is located in "templates"-folder
    return render_template("web_visualization.html")


@app.route("/handle_parameters", methods=["POST"])
def handleParameters():
    """Function that handles parameters for temperature plot,
    and then plots it and saves file to static folder, which
    is used by the html file to show the plot to user"""

    #get data from form
    fromYear = int(request.form["fromYear"])
    toYear = int(request.form["toYear"])
    month = request.form["month"]
    minY = int(request.form["minY"])
    maxY = int(request.form["maxY"])

    #plots temperature, which generates a new version of png
    #with same name as old, in order for our standard html to show it
    plot_Temperature("temperature.csv",fromYear,toYear,month,(minY,maxY))
    return render_template("web_visualization.html")

@app.route("/handle_parameters2", methods=["POST"])
def handleParameters2():
    """Function that handles parameters for carbon plot,
    and then plots it and saves file to static folder, which
    is used by the html file to show the plot to user"""

    #get data from form, variables that are set are defined in the name= tag
    fromYear = int(request.form["fromYear"])
    toYear = int(request.form["toYear"])
    minY = int(request.form["minY"])
    maxY = int(request.form["maxY"])


    plot_CO2("co2.csv",fromYear,toYear,(minY,maxY))
    return render_template("web_visualization.html")

@app.route("/handle_parameters3", methods=["POST"])
def handleParameters3():
    """Function that handles parameters for carbon plot by country,
    and then plots it and saves file to static folder, which
    is used by the html file to show the plot to user"""


    #get data from form
    #for this plot we need to get the string, since the
    #year input for our set-generation is a string, while the two previous
    #plotters take year as an int(this is nothing you need to care about,
    #since its only because this csv file is set up differently, which
    #makes us do this different)
    year = request.form["year"]
    minY = float(request.form["minY"])
    maxY = float(request.form["maxY"])

    plotCO2ByCountry("CO2_by_country.csv",year,(minY,maxY))
    return render_template("web_visualization.html")


if __name__ == "__main__":
    app.run()
