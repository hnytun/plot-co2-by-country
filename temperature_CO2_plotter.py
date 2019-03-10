import pandas as pd
import matplotlib.pyplot as mpl

def getTemperatureDataset(filename,fromYear,toYear,monthToPlot,threshold):
    """
    function that makes a dataframe object of temperature-data from file with the pandas lib
    input:
            filename: filename in csv format with the data
            fromYear: gives data from this year
            toYear: gives data up to this year
            monthToPlot: what month we want data from
            threshold: min value and max value of temperature(y-value)
    returns:
            DataFrameobject with temperature values from a range of years within threshold
    """
    #parse dataset
    dataset = pd.read_csv(filename);
    #only make dataset out of the years user specified
    yearsFiltered = dataset[(dataset["Year"]>=fromYear) & (dataset["Year"]<=toYear)]
    #only make dataset where temperature values are between threshold
    thresholdFiltered = yearsFiltered[(yearsFiltered[monthToPlot]>=threshold[0]) & (yearsFiltered[monthToPlot]<=threshold[1])]
    return thresholdFiltered[["Year",monthToPlot]]

def getCO2Dataset(filename,fromYear,toYear,threshold):
    """
    function that makes a dataframe object of carbon-emission-data from file with the pandas lib
    takes in arguments and generates a set based on these
    input:
            filename: filename in csv format with the data
            fromYear: gives data from this year
            toYear: gives data up to this year
            threshold: min value and max value of temperature(y-value)
    returns:
            DataFrameobject with c02 values from a range of years within threshold
    """
    #parse dataset
    dataset = pd.read_csv(filename)
    #only make dataset out of the years user specified
    yearsFiltered = dataset[(dataset["Year"]>=fromYear) & (dataset["Year"]<=toYear)]
    #only make dataset where temperature values are between threshold
    thresholdFiltered = yearsFiltered[(yearsFiltered["Carbon"]>=threshold[0]) & (yearsFiltered["Carbon"]<=threshold[1])]

    return thresholdFiltered[["Year","Carbon"]]

def getCO2ByCountryDataset(filename,year,threshold):
    """function that makes a dataframe object for carbon emission
    by country
    input:
            filename: filename in csv format with data
            year: what year to plot
            threshold: threshold of y values
    returns:
            DataFrameobject with co2 by country"""
    dataset = pd.read_csv(filename)

    #filter out so we only get the countries and the specified year
    #use country code instead of name to fit in all plotted elements
    #since the task didnt specify otherwise

    #but first, we check if we can generate a set on given year,typically
    #without this program would crash if user put in invalid year
    #we do this by checking if year is in the dataframe-set, if not,
    #we just return an "empty"set
    if year in dataset:
        datasetWithYearOnly=dataset[['Country Code',year]]
        #filter out the countries that are within the threshold
        datasetWithinThreshold=datasetWithYearOnly[(datasetWithYearOnly[year]>=threshold[0]) & (datasetWithYearOnly[year]<=threshold[1])]
        #print(datasetWithinThreshold)
    else: # = means that the year isnt a column in the set, return empty set
        datasetWithinThreshold = pd.Series(0, index=['NO DATA'])
    return datasetWithinThreshold

def plotCO2ByCountry(filename,year,threshold):
    """Function plots dataset for CO2 by country
    input:
            filename: filename
            year: what year to plot (reasonable: between 0 and 3000)
            threshold:threshold of y values (reasonable value to avoid cluttering values: f.example 0.6-1, since a big threshold results in maaaany values(many countries))
    """
    dataset=getCO2ByCountryDataset(filename,year,threshold)

    #if input generated empty set we just plot an empty set with a message
    #that there is no data to plot, instead of trying to plot an empty set,
    #which crashes the program
    if len(dataset) == 0:
        dataset = pd.Series(0, index=['NO DATA'])
        dataset.plot()
        mpl.savefig("static/CO2ByCountry.png")
    else:
        dataset.plot(x="Country Code",y=year,kind="barh")
        mpl.savefig("static/CO2ByCountry.png")

    #use country code instead of name to fit all into the plot


    #mpl.savefig("static/CO2ByCountry.png")
    #mpl.show()

def plot_CO2(filename,fromYear,toYear,threshold):
    """
    This function plots the dataset for CO2 in file
    input:
            filename: filename in csv format with the data
            fromYear: gives data from this year (reasonable: 0)
            toYear: gives data up to this year (reasonable: 3000)
            threshold: min value and max value of temperature(y-value) (reasonable: having a value of f.example -10 to 0 wont generate anything, instead 0-10000 works perfect)
    """
    dataset=getCO2Dataset(filename,fromYear,toYear,threshold)

    #if input generated empty set we just plot an empty set with a message
    #that there is no data to plot
    if len(dataset) == 0:
        dataset = pd.Series(0, index=['NO CARBON DATA'])
        dataset.plot()
        mpl.savefig("static/carbon.png")
    else:
        dataset.plot(x="Year",y="Carbon")
        mpl.savefig("static/carbon.png")
    #i save the figure to a file in the static folder, but if you want
    #it to pop up in an app, you can uncomment the show() function
    #mpl.show()
def plot_Temperature(filename,fromYear,toYear,monthToPlot,threshold):
    """
    This function plots the dataset for temperature, takes in arguments and generates a set based on these in file
    input:
            filename: filename in csv format with the data
            fromYear: gives data from this year (reasonable:0)
            toYear: gives data up to this year (reasonable: 3000)
            monthToPlot: what month we want data from (format is January,February,March,April,May,June,July,August,September,October,November,December)
            threshold: min value and max value of temperature(y-value) (reasonable: Think temperatures, making the threshold between -10 and 0 in June wont generate a plot, here 0,30 would be perfect)
    """
    #get dataset from getTemperatureDataset and plot it
    dataset=getTemperatureDataset(filename,fromYear,toYear,monthToPlot,threshold)

    #if input generated empty set we just plot an empty set with a message
    #that there is no data to plot
    if len(dataset) == 0:
        dataset = pd.Series(0, index=['NO TEMPERATURE DATA'])
        dataset.plot()
        mpl.savefig("static/temperature.png")
    else:
        dataset.plot(x="Year",y=monthToPlot)
        mpl.savefig("static/temperature.png")

    #i save the figure to a file in the static folder, but if you want
    #it to pop up in an app, you can uncomment the show() function

    #mpl.show()


#if you run both at the same time you need to close the first to view the second
#but if you want to view one just comment out the other if you dont feel like running all of them
if __name__ == "__main__":
    plotCO2ByCountry("CO2_by_country.csv","2010",(0.6,1))
    plot_CO2("co2.csv",1816,3000,(0,1000))
    plot_Temperature("temperature.csv",0,3000,"June",(0,21))
