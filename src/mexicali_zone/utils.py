import geopandas as gpd
import pandas as pd

from mexicali_zone.constants import SECTORS_MAP


def fill(df, columns):
    fills = [2, 3, 4, 4, 3]
    df["CVE_GEO"] = ""
    for column, amount in zip(columns, fills):
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].astype(int)
        df["CVE_GEO"] += df[column].astype(str).str.zfill(amount)
    if "geometry" in df.columns:
        df = gpd.GeoDataFrame(df, geometry="geometry", crs=df.crs)
    return df


def map_sector_to_sector(codigo_act: int) -> str:
    for sector in SECTORS_MAP:
        for low, high in sector["range"]:
            if low <= codigo_act <= high:
                return sector["sector"]