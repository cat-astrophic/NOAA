# NOAA

This repo contains scripts to create annual datasets consisting of NOAA weather data for all sites in the United States. To create these datasets, follow the instructions below.

1. Set up the directory **path/NOAA/**
2. Make **path/NOAA/tar/** and **path/NOAA/raw_data/** and **path/NOAA/us_data/**
3. Download files from [**NOAA**](https://www.ncei.noaa.gov/data/global-summary-of-the-day/archive/) and store in **path/NOAA/tar/**
4. Run **NOAA_untar.py**
5. Run **NOAA_build.py**
