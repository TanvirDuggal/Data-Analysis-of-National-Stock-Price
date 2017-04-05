# Data-Analysis-of-National-Stock-Price
National Stock Price, extract data from Quandl.com and pickles it in our computer hard disk. Then we can plot a well maintained graph out of it. Through this graph we can study the stock variations of a particular company over the years.

This project is made in python, using popular libraries pandas and matplotlib. To extract data from Quandl their API is used. Pickling helps the user to store extracted data in the hard disk and use it later for plotting the graph, this will prevent from downloading data every time in a process which takes time.

You can later update the downloaded data and then plot it again with the updated values.

To get the name of the company whose data you wish to plot, one needs to go to quandl.com and search for "Indian NSE", this will provide name of the company along with their "Quandl Code". Just enter the Quandl Code in the project and you will be able to store and plot the data.

As per the graph it contains three partitions, one which uses "Line Graph" to show the "Opening value" of the stock, second is a "Candlstick graph" that calculates the total price from opening, closing, high, low, last, total trade and turnover. Third is two "Line Graph", of "Closing value" which shows the profit or lose of the stock at the closing of stock. 

Currently we have one pickle stored in computer, its the retrieved data of "L&T", from quandl. 
To view the graph of it. 
1. Run the project enter "NSE/LTTS", and press enter. 
2. It will ask whether we want to update or plot from existing data.
3. For now we will plot from existing data, so type "2" and press enter.
4. If everything goes well, you will be able to see the graph.

If you want to plot a fresh graph, 
1. Go to "www.quandl.com", and search for "Indian NSE".
2. This will give you list all the companies under NSE with their Quandl Code.
3. Copy the Quandl Code and paste it on the project and it will download and plot the graph out of it.
