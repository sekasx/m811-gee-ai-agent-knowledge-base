



* [Home](https://developers.google.com/)
* [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
* [All datasets](https://developers.google.com/earth-engine/datasets/catalog)





 
 
 Send feedback
 
 

Preview National Intertidal Digital Elevation Model 25m 1\.0\.0


 
 Stay organized with collections
 

 
 Save and categorize content based on your preferences.
=================================================================================================================================================================








Dataset Availability
1986\-08\-16T00:00:00Z–2017\-07\-31T23:59:59Z
Dataset Provider


[Geoscience Australia](https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat)


[NGIS](https://ngis.com.au/)



Earth Engine Snippet


`ee.Image("projects/ngis-cat/assets/DEA/NIDEM")` 
[open\_in\_new](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ngis-cat/projects_ngis-cat_assets_DEA_NIDEM)





Tags


[australia](/earth-engine/datasets/tags/australia)
[dem](/earth-engine/datasets/tags/dem)
[elevation\-topography](/earth-engine/datasets/tags/elevation-topography)
[ga](/earth-engine/datasets/tags/ga)








#### Description



The National Intertidal Digital Elevation Model (NIDEM; Bishop\-Taylor et
al. 2018, 2019\) is a continental\-scale elevation dataset for Australia's
exposed intertidal zone. NIDEM provides the first three\-dimensional
representation of Australia's intertidal sandy beaches and shores, tidal
flats and rocky shores and reefs at 25 m spatial resolution, addressing a
key gap between the availability of sub\-tidal bathymetry and terrestrial
elevation data. NIDEM was generated by combining global tidal modelling with
a 30\-year time series archive of spatially and spectrally calibrated Landsat
satellite data managed within the Digital Earth Australia (DEA) platform.
NIDEM complements existing intertidal extent products, and provides data to
support a new suite of use cases that require a more detailed understanding
of the three\-dimensional topography of the intertidal zone, such as
hydrodynamic modelling, coastal risk management and ecological habitat
mapping.


For more information, please see the
[DEA Intertidal Elevation](https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat#basics)





### Bands



**Pixel Size**
  
25 meters



**Bands**




| Name | Units | Min | Max | Description |
| --- | --- | --- | --- | --- |
| `nidem` | m | \-5 | 3\.9 | Primary product: elevation in meter units relative to modelled Mean Sea Level (MSL). [Band details](https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat#details) |
| `nidem_mask` | None | Quality flag. [Band details](https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat#details) |
| `nidem_uncertainty` | m | 0 | 0\.3 | Uncertainty meters. [Band details](https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat#details) |
| `nidem_unfiltered` | m | \-5 | 3\.9 | Un\-cleaned elevation in meters. [Band details](https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat#details) |


**nidem\_mask Class Table**




| Value | Color | Description |
| --- | --- | --- |
| 1 | \#00ff00 | above 25 m relative to Mean Sea Level (MSL) |
| 2 | \#ff0000 | below \-25 m relative to Mean Sea Level (MSL) |
| 3 | \#ffff00 | invalid elevation estimates |




### Terms of Use


**Terms of Use**


[CC\-BY\-4\.0](https://spdx.org/licenses/CC-BY-4.0.html)




### Citations



Citations:
* Bishop\-Taylor, R., Sagar, S., Lymburner, L., \& Beaman, R. J. (2019\).
Between the tides: Modelling the elevation of Australia's exposed intertidal
zone at continental scale. Estuarine, Coastal and Shelf Science, 223,
115\-128\.
[doi:10\.1016/j.ecss.2019\.03\.006](https://doi.org/10.1016/j.ecss.2019.03.006)





### DOIs


* [https://doi.org/10\.1016/j.ecss.2019\.03\.006](https://doi.org/10.1016/j.ecss.2019.03.006)




### Explore with Earth Engine


**Important:** 
 Earth Engine is a platform for petabyte\-scale scientific analysis and visualization of
 geospatial datasets, both for public benefit and for business and government users.
 Earth Engine is free to use for research, education, and nonprofit use. To get started, please
 [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)



### Code Editor (JavaScript)



```
varnidem=ee.Image('projects/ngis-cat/assets/DEA/NIDEM');

varelevation=nidem.select('nidem');
varelevationVis={
min:-2.5,
max:1.5,
palette:[
'440154','471365','482475','463480','414487','3b528b','355f8d',
'2f6c8e','2a788e','25848e','21918c','1e9c89','22a884','2fb47c',
'44bf70','5ec962','7ad151','9bd93c','bddf26','dfe318','fde725'
],
};
Map.setCenter(122.36,-18.10,11);
Map.addLayer(
elevation,elevationVis,
'National Intertidal Digital Elevation Model (NIDEM; m)');
```



[Open in Code Editor](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/ngis-cat/projects_ngis-cat_assets_DEA_NIDEM)


[Preview National Intertidal Digital Elevation Model 25m 1\.0\.0](/earth-engine/datasets/catalog/projects_ngis-cat_assets_DEA_NIDEM)

The National Intertidal Digital Elevation Model (NIDEM; Bishop\-Taylor et al. 2018, 2019\) is a continental\-scale elevation dataset for Australia's exposed intertidal zone. NIDEM provides the first three\-dimensional representation of Australia's intertidal sandy beaches and shores, tidal flats and rocky shores and reefs at 25 m spatial resolution, addressing a key …

 projects/ngis\-cat/assets/DEA/NIDEM,
 australia,dem,elevation\-topography,ga

1986\-08\-16T00:00:00Z/2017\-07\-31T23:59:59Z



 \-44\.41 108\.81 \-9\.13 157\.82
 



Google Earth Engine
https://developers.google.com/earth\-engine/datasets

* [https://doi.org/10\.1016/j.ecss.2019\.03\.006](https://doi.org/https://cmi.ga.gov.au/data-products/dea/325/dea-intertidal-elevation-landsat)
* [https://doi.org/10\.1016/j.ecss.2019\.03\.006](https://doi.org/https://ngis.com.au/)
* [https://doi.org/10\.1016/j.ecss.2019\.03\.006](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/projects_ngis-cat_assets_DEA_NIDEM)









