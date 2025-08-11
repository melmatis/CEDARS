# CEDARS Data Download

TL;DR: This will provide some utilities to download and manage CEDARS data to make it useful to load into your jupyter notebooks for analysis. 

### How to Use:

*cedars__download* is a python function to get CEDARS claims data from the web.To use the *cedars__download* function:

## Step 1: Install the packages to run the python function:

`%pip install requests`

`%pip install pandas`

*### Here are a couple engine options; engine is called in the `pd.read_parquet` function (see Step 4). Try fastparquet.*

`%pip install fastparquet`

`%pip install pyarrow` 

## Step 2: Working Directory
save *cedars__download.py* in the same folder as the notebook you use to do analysis on CEDARS data

## Step 3: Call the Data Download Function
use this code in your notebook to call the *cedars__download* function:

`from cedars__download import fetch_cedars_claims`

`local_path = fetch_cedars_claims(year)`

`print(local_path)`

## Step 4: Create Dataframe
Make the claims data that you downloaded to a local path into a dataframe; also ensure the file exists first with this code:

`if not local_path.exists(): raise FileNotFoundError(f"No Parquet file for {year} at {local_path}")`

    
`claims_data= pd.read_parquet(local_path, engine="fastparquet")`

## Step 5: Analysis 
Do analaysis on dataframe *claims_data*. For example, my analysis is in *CEDARS_DataAnalysis*.
