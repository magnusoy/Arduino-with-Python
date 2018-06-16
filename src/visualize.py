#!/usr/bin/python
"""
Class to present and plot
data gathered from Arduino.

Code by: Magnus Øye, Dated: 16.06-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Arduino-with-Python
"""

# importing nessary libraries
import matplotlib.pyplot as plt
from matplotlib.style import use
from drawnow import drawnow
import pandas as pd


class Visualize:
    """Visualize is a simply library to
        present and plot gathered data from
        the Arduino."""

    def __init__(self):
        """Initialize data, creating a
            pandas dataframe storing data from
            file.
            Parameters
            ----------
            datapath : str
                data location"""
        self.values = []
        self.data = None

    def collectData(self, filename):
        """Collect data from file and
            present it in pandas dataframe
            Parameters
            ----------
            filename: str
                filepath to data
           Returns
            ----------
            data : Dataframe
                Dataframe of all the entries"""
        self.data = pd.read_csv(filename, error_bad_lines=False, encoding="latin-1")
        return self.data.dropna()
    
    def viewDataHead(self):
        """Presents dataframe of first
            5 entires
           Returns
            ----------
            data : Dataframe
                Dataframe of the first 5 entries"""
        return self.data.head()
    
    def viewDataInformation(self):
        """Presents dataframe with
            information
           Returns
            ----------
            data : Dataframe
                Data information"""
        return self.data.info()

    def getColumns(self):
        """Presents dataframe with
            information
           Returns
            ----------
            columns : panda object
                column names"""
        return self.data.columns
    
    def plot(self, x, y):
        """Creates and showcase a line
            graph.
            Parameters
            ----------
            x: pandas dataframe
                ex. data['A']
            y: pandas dataframe
                ex. data['B']
            interactive_mode: boolean
                turns on live plotting
            
            Returns
            -------
            fig: matplotlib figure
                figure"""
        use("seaborn")
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel= "X-value", ylabel='Y-value',
        title='Line Graph')
        plt.show()
        return fig

    def livePlot(self, data):
        """Creates a plot that updates in real time
            Parameters
            ----------
            data: str
                datastream from serial"""
        self.values.append(data)
        use("seaborn")
        def makeFig():
            plt.plot(self.values)
            
        drawnow(makeFig)
        plt.pause(0.00001)

    def turnOnInteractiveMode(self, switch):
        if switch == True:
            plt.ion()
            return True
        elif switch == False:
            plt.ioff()
            return False
    
    def savePlot(self, figure, filename):
        """Save plot as image
            Parameter
            ---------
            figure: matplotlib figure
                plot figure
            filename: str
                filepath"""
        figure.savefig(filename)
