import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

populationMean=statistics.mean(data)
StandardDeviation=statistics.stdev(data)

print("Mean of Population Data:-",populationMean)
print("Standard Deviation of Population Data:-",StandardDeviation)

fig=ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataSet=[]

    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)

    Mean=statistics.mean(dataSet)
    return Mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    print("Mean of sampling distribution:-",mean)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]

    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)

    show_fig(mean_list)
setup()