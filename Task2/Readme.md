Task 1
1. Load the data into a Pandas Dataframe.
2. Which of the categorical features are nominal and which are ordinal?
3. Add a column that holds the total screen resolution for each device. Name it resolution.
4. Add a column that holds the DPI (dots per inch) of the screen width and name it DPI_w.
DPI of a digital image is calculated by dividing the total number of dots wide by the total
number of inches wide. Do not leave NaN/Infinite values.
5. Add a column that holds the ratio battery_power/talk_time and name it call_ratio. 6.
Do not leave NaN/Infinite values.
Change the memory column to hold the memory in GB instead of MB.
7. Include the output of the `describe()` function of the dataframe.
8. Convert the following features into categorical series in the Dataframe: speed,screen,cores


Task 2

1. How many phones do not have a camera at all (front or back)?
2. What is the average battery power for single-sim phones that have a camera or front camera
with a higher resolution than 12 megapixels?
3. What is the ID and price of the most expensive phone that has no wifi, a touch screen and
weighs more than 145 grams?
4. Create a pivot table that shows the percentage of phones with Bluetooth per generation,
pivoted around the phone generation and split by “ram” quartiles. (i.e. the rows are the
generation number and the columns are 4 quartiles of ram size).
5. Create a new Dataframe based on the original that has the following features: [id,
battery_power, ram, talk_time, Bluetooth, cores, sim, memory, price], and contains a random
sampling of half of the medium speed phones.
6. Using this new dataset, what is the maximum total talk time you can achieve if you use 3
phones, and which 3 phones will you use?
