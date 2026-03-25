#  Plotting a time series

In this example you will plot the value of bitcoin as a function
of time.

The aim of the exercise is to run the script [bit_coin.py](https://github.com/cmcneile/streamlit_tutorial/blob/main/scripts/bit_coin.py)

* Download the script bit_coin.py
* In the anaconda prompt run:  **streamlit run bit_coin.pea**

The web App should look like the below in the browser

![lineplot screenshot](https://raw.githubusercontent.com/cmcneile/streamlit_tutorial/refs/heads/main/pictures/lineEg.png)

## Exercise 1

The file
[gdp.csv](https://github.com/datasets/gdp/blob/main/data/gdp.csv)
contains the GDP value for different counteries.

* Create a Web App that plots the GDP of Afghanistan as a function
of year using the above data set.

* Create a Web App that plots the GDP of Afghanistan and Algeria as a function of year on the same graph. [This example may be a good example](https://docs.streamlit.io/develop/api-reference/charts/st.pyplot)

* Use [select box](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox) to select which country to plot the GDP. 