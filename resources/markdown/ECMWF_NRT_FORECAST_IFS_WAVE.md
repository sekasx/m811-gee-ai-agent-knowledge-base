



* [Home](https://developers.google.com/)
* [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
* [All datasets](https://developers.google.com/earth-engine/datasets/catalog)





 
 
 Send feedback
 
 

ECMWF Near\-Realtime IFS Wave Forecasts


 
 Stay organized with collections
 

 
 Save and categorize content based on your preferences.
=========================================================================================================================================








Dataset Availability
2024\-11\-12T12:00:00Z–2025\-07\-18T12:00:00Z
Dataset Provider


[ECMWF](https://www.ecmwf.int/en/forecasts/datasets/open-data)



Earth Engine Snippet


`ee.ImageCollection("ECMWF/NRT_FORECAST/IFS/WAVE")` 
[open\_in\_new](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ECMWF/ECMWF_NRT_FORECAST_IFS_WAVE)





Cadence
12 Hours
Tags


[climate](/earth-engine/datasets/tags/climate)
[ecmwf](/earth-engine/datasets/tags/ecmwf)
[forecast](/earth-engine/datasets/tags/forecast)
[global](/earth-engine/datasets/tags/global)
[ocean](/earth-engine/datasets/tags/ocean)








#### Description



This dataset contains 15\-day forecasts of the wave model fields
generated by the ECMWF Integrated Forecasting System (IFS) at 0\.25 degree
resolution. We refer to these as Near\-Realtime (NRT) because new products
are released twice a day after the release of the ECMWF realtime forecast
data, of which this is a subset. Data may be distributed and used
commercially with
[proper attribution](https://apps.ecmwf.int/datasets/licences/general/).


Products are available in Earth Engine starting with the implementation of
[Cycle 49r1](https://confluence.ecmwf.int/display/FCST/Implementation+of+IFS+Cycle+49r1)
on 2024\-11\-12; earlier products are not included. For general information
about how to use ECMWF NRT datasets, see their
[user documentation](https://confluence.ecmwf.int/display/DAC/ECMWF+open+data%3A+real-time+forecasts+from+IFS+and+AIFS).
Sources files are available in the
[Google Cloud marketplace](https://console.cloud.google.com/marketplace/product/bigquery-public-data/open-data-ecmwf).





### Bands



**Pixel Size**
  
28000 meters



**Bands**




| Name | Units | Min | Max | Description |
| --- | --- | --- | --- | --- |
| `mean_zero_crossing_wave_period_sfc` | seconds | 0\.889358\* | 17\.0074\* | The mean length of time between occasions where the sea/ocean surface crosses mean sea level. |
| `significant_height_of_combined_wind_waves_and_swell_sfc` | m | 0\.0172079\* | 15\.7469\* | The average height of the highest third of surface ocean/sea waves generated by wind and swell. It represents the vertical distance between the wave crest and the wave trough. |
| `mean_wave_direction_sfc` | deg | 0 | 360 | The mean direction of ocean/sea surface waves relative to the geographic location of the north pole (e.g., 0 means "coming from the north" and 90 "coming from the east"). |
| `peak_wave_period_sfc` | seconds | 1\.03074\* | 23\.9353\* | The period of the most energetic ocean waves generated by local winds and associated with swell. The wave period is the average time it takes for two consecutive wave crests, on the surface of the ocean/sea, to pass through a fixed point. |
| `mean_wave_period_sfc` | seconds | 1\.04071\* | 19\.5239\* | The average time it takes for two consecutive wave crests, on the surface of the ocean/sea, to pass through a fixed point. |


 \* estimated min or max value


### Image Properties


**Image Properties**




| Name | Type | Description |
| --- | --- | --- |
| creation\_day | INT | Day of the month when the forecast was created. |
| creation\_doy | INT | Day of the year when the forecast was created. |
| creation\_hour | INT | Hour of the day when the forecast was created. |
| creation\_month | INT | Month of the year when the forecast was created. |
| creation\_time | INT | Time, in unix epoch milliseconds, when forecast was created. |
| creation\_year | INT | Year when the forecast was created. |
| forecast\_hours | INT | Hours into the future, relative to `creation_time`, of the forecast. |
| forecast\_time | INT | Time, in unix epoch milliseconds, of the forecast. |
| model | STRING | The ECMWF forecasting model:* ifs: Integrated Forecasting System * aifs: Artificial Intelligence/Integrated Forecasting System |
| stream | STRING | The stream from which the variables were fetched. See the full list [here](https://codes.ecmwf.int/grib/format/mars/stream/). |




### Terms of Use


**Terms of Use**


[CC\-BY\-4\.0](https://spdx.org/licenses/CC-BY-4.0.html)




### DOIs


* [https://doi.org/10\.21957/open\-data](https://doi.org/10.21957/open-data)




### Explore with Earth Engine


**Important:** 
 Earth Engine is a platform for petabyte\-scale scientific analysis and visualization of
 geospatial datasets, both for public benefit and for business and government users.
 Earth Engine is free to use for research, education, and nonprofit use. To get started, please
 [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)



### Code Editor (JavaScript)



```
// Observe the ocean in the vicinity of the Caribbean islands and
// Gulf coast.
varaoi=ee.Geometry.Polygon(
[[
[-100.6052734375,31.751243295508836],
[-100.6052734375,6.080143483787566],
[-57.18730468750001,6.080143483787566],
[-57.18730468750001,31.751243295508836]
]],
null,false);

// Extract significant wave height forecasts made at noon on 2025/6/11.
varwave=
ee.ImageCollection('ECMWF/NRT_FORECAST/IFS/WAVE')
.filter(ee.Filter.eq('creation_doy',162))
.filter(ee.Filter.eq('creation_hour',12))
.sort('forecast_hours')
.select('significant_height_of_combined_wind_waves_and_swell_sfc');

// Display the observations at forecast hour 0 on the map.
varhour0=wave.first().clip(aoi);
Map.centerObject(hour0);
Map.addLayer(hour0,{min:0,max:5},'sig height fc=0');

// Animate the wave height forecasts over time.
varvideoArgs={
dimensions:540,
region:aoi,
framesPerSecond:7,
crs:'EPSG:3857',
min:0,
max:5,
};
print(ui.Thumbnail(wave,videoArgs));
```



[Open in Code Editor](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ECMWF/ECMWF_NRT_FORECAST_IFS_WAVE)


[ECMWF Near\-Realtime IFS Wave Forecasts](/earth-engine/datasets/catalog/ECMWF_NRT_FORECAST_IFS_WAVE)

This dataset contains 15\-day forecasts of the wave model fields generated by the ECMWF Integrated Forecasting System (IFS) at 0\.25 degree resolution. We refer to these as Near\-Realtime (NRT) because new products are released twice a day after the release of the ECMWF realtime forecast data, of which this is …

 ECMWF/NRT\_FORECAST/IFS/WAVE,
 climate,ecmwf,forecast,global,ocean

2024\-11\-12T12:00:00Z/2025\-07\-18T12:00:00Z



 \-90 \-180 90 180
 



Google Earth Engine
https://developers.google.com/earth\-engine/datasets

* [https://doi.org/10\.21957/open\-data](https://doi.org/https://www.ecmwf.int/en/forecasts/datasets/open-data)
* [https://doi.org/10\.21957/open\-data](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/ECMWF_NRT_FORECAST_IFS_WAVE)









