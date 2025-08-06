cedars__download is a python function to grad CEDARS claims data from the web
to use the cedars__download function:

Step #1: save cedars__download.py in the same folder as the notebook you use to do analysis on CEDARS data

Step #2: use this code in your notebook to call the cedars__download function:

from cedars__download import fetch_cedars_claims
local_path = fetch_cedars_claims(year)
print(local_path)

Step#3 Make the claims data that you downloaded to a local path into a dataframe; also ensure the file exists first with this code:

if not local_path.exists():
    raise FileNotFoundError(f"No Parquet file for {year} at {local_path}")
# read it
claims_data= pd.read_parquet(local_path, engine="pyarrow")

Step#4 Do analaysis on dataframe "claims_data". Happy coding! :)
