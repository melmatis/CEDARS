# CEDARS Data Download

TL;DR: This will provide some utilities to download and manage CEDARS data to make it useful to load into your jupyter notebooks for analysis. 

### How to Use:

*cedars__download* is a python function to get CEDARS claims data from the web.To use the *cedars__download* function:

## Step 1: Install the packages to run the python function:

`%pip install requests`

`%pip install pandas`

*Here are a couple engine options; in the code, the engine is called in the `pd.read_parquet` function (see Step 4). Try fastparquet.*

`%pip install fastparquet`

`%pip install pyarrow` 

`%pip install pathlib`

## Step 2: Working Directory
save *cedars__download.py* in the same folder as the notebook you use to do analysis on CEDARS data

## Step 3: Define the Year(s)
create a variable called `year` and set it equal to a 4 digit year in integer form. For example:

`year = [2023]`

For multiple years: 

`year = [2023, 2024]`

## Step 4: Call the Data Download Function
use this code in your notebook to call the *cedars__download* function:

`from cedars__download import fetch_cedars_claims`

`local_path = fetch_cedars_claims(year)`

`print(local_path)`

For multiple years:

`from pathlib import Path`

```python
from pathlib import Path

paths = []
for y in years:
    p = fetch_cedars_claims(y)  # downloads (or returns cached) Parquet for that year
    if not Path(p).exists():
        print(f"Skipping {y}: no Parquet at {p}")
        continue
    paths.append(Path(p))



## Step 5: Create Dataframe
Make the claims data that you downloaded to a local path into a dataframe; also ensure the file exists first with this code:

`if not local_path.exists(): raise FileNotFoundError(f"No Parquet file for {year} at {local_path}")`

    
`claims_data= pd.read_parquet(local_path, engine="fastparquet")`

For multiple years:
`claims_data = []`

`for p in paths:`
    `df = pd.read_parquet(p, engine="fastparquet")`
   
    `claims_data.append(df)`

`claims_data = pd.concat(claims_data, ignore_index=True, sort=False) if claims_data else pd.DataFrame()`

## Step 6: Analysis 
Do analaysis on dataframe *claims_data*. 
