#!/usr/bin/python
"""
Class to present and plot
data gathered from Arduino.

Code by: Magnus Øye, Dated: 15.06-2018
Contact: magnus.oye@gmail.com
Website: https://github.com/magnusoy/Arduino-with-Python
"""

# importing nessary libraries
import matplotlib.pyplot as plt
from matplotlib.style import use
import pandas as pd

class Visualize:
    """Visualize is a simply library to
        present and plot gathered data from
        the Arduino."""

    def __init__(self, datapath):
        """Initialize data, creating a
            pandas dataframe storing data from
            file.
            Parameters
            ----------
            datapath : str
                data location"""
        self.datapath = datapath
        self.data = pd.read_csv(self.datapath, error_bad_lines=False, encoding="latin-1")

    def collectData(self):
        """Presents dataframe
           Returns
            ----------
            data : Dataframe
                Dataframe of all the entries"""
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
    
    def lineplot(self, x, y):
        """Creates and showcase a line
            graph.
            Parameters
            ----------
            x: pandas dataframe
                ex. data['A']
            y: pandas dataframe
                ex. data['B']
            
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
    
    def savePlot(self, figure, filename):
        """Save plot as image
            Parameter
            ---------
            figure: matplotlib figure
                plot figure
            filename: str
                filepath"""
        figure.savefig(filename)
