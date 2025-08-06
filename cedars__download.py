from pathlib import Path
from io import BytesIO, TextIOWrapper
import zipfile
import requests
import pandas as pd


def fetch_cedars_claims(year: int,
                        out_dir: Path | str = "cache",
                        timeout: int = 60,
                        force_refresh: bool = False) -> Path:
    """
    Download CPUC CEDARS record-level claims data for a given year,
    save it as a Parquet file locally, and return the absolute path.

    Parameters
    ----------
    year : int
        Calendar year to fetch (e.g., 2025).
    out_dir : Path | str, default "cache"
        Folder where the Parquet file will be stored.
    timeout : int, default 60
        Seconds to wait for the HTTP response before raising.
    force_refresh : bool, default False
        If True, re-download even when the Parquet file already exists.

    Returns
    -------
    Path
        Absolute path to the saved Parquet file.

    Raises
    ------
    requests.HTTPError
        If the HTTP request fails (non-200 status code).
    zipfile.BadZipFile
        If the downloaded content is not a valid ZIP archive.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True)

    parquet_path = out_dir / f"Get_Claims{year}.parquet"
    if parquet_path.exists() and not force_refresh:
        print(f"✔ Cached file found — skipping download:\n    {parquet_path.resolve()}")
        return parquet_path.resolve()

    url = f"https://cedars.cpuc.ca.gov/reports/download-record-level-report/all_pas/{year}/claims/"
    print(f"↓ Downloading {url}")

    # Request the ZIP archive
    resp = requests.get(url, timeout=timeout)
    resp.raise_for_status()

    # Unzip directly into a DataFrame
    with zipfile.ZipFile(BytesIO(resp.content)) as zf:
        csv_name = zf.namelist()[0]
        print(f"   Found in ZIP: {csv_name}")

        with zf.open(csv_name) as raw:
            df = pd.read_csv(
                TextIOWrapper(raw, encoding="utf-8"),
                sep=",",
                low_memory=False,
            )

    # Save to Parquet
    df.to_parquet(parquet_path, index=False)
    print(f"✔ Saved to:\n    {parquet_path.resolve()}")

    return parquet_path.resolve()
