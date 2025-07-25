



* [Home](https://developers.google.com/)
* [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
* [All datasets](https://developers.google.com/earth-engine/datasets/catalog)





 
 
 Send feedback
 
 

Global 3\-class PALSAR\-2/PALSAR Forest/Non\-Forest Map


 
 Stay organized with collections
 

 
 Save and categorize content based on your preferences.
=========================================================================================================================================================








Dataset Availability
2007\-01\-01T00:00:00Z–2018\-01\-01T00:00:00Z
Dataset Provider


[JAXA EORC](https://www.eorc.jaxa.jp/ALOS/en/dataset/fnf_e.htm)



Earth Engine Snippet


`ee.ImageCollection("JAXA/ALOS/PALSAR/YEARLY/FNF")` 
[open\_in\_new](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_ALOS_PALSAR_YEARLY_FNF)





Tags


[alos](/earth-engine/datasets/tags/alos)
[alos2](/earth-engine/datasets/tags/alos2)
[classification](/earth-engine/datasets/tags/classification)
[eroc](/earth-engine/datasets/tags/eroc)
[forest](/earth-engine/datasets/tags/forest)
[forest\-biomass](/earth-engine/datasets/tags/forest-biomass)
[jaxa](/earth-engine/datasets/tags/jaxa)
[landcover](/earth-engine/datasets/tags/landcover)
[palsar](/earth-engine/datasets/tags/palsar)
[palsar2](/earth-engine/datasets/tags/palsar2)
[sar](/earth-engine/datasets/tags/sar)








#### Description



A newer version of this dataset with 4 classes for 2017\-2020 can be found in
[JAXA/ALOS/PALSAR/YEARLY/FNF4](/earth-engine/datasets/catalog/JAXA_ALOS_PALSAR_YEARLY_FNF4)


The global forest/non\-forest map (FNF) is generated by
classifying the SAR image (backscattering coefficient) in the
global 25m resolution PALSAR\-2/PALSAR SAR mosaic so that strong and
low backscatter pixels are assigned as "forest" and "non\-forest",
respectively. Here, "forest" is defined as the natural forest
with the area larger than 0\.5 ha and forest cover over 10%. This
definition is the same as the Food and Agriculture Organization
(FAO) definition. Since the radar backscatter from the forest
depends on the region (climate zone), the classification of
Forest/Non\-Forest is conducted by using a region\-dependent
threshold of backscatter. The classification accuracy is
checked by using in\-situ photos and high\-resolution optical
satellite images. Detailed information is available in the provider's
[Dataset Description](https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/DatasetDescription_PALSAR2_Mosaic_FNF_revE.pdf).


Attention:


* Backscatter values may vary significantly from path to path
over high latitude forest areas. This is due to the change of
backscattering intensity caused by freezing trees in winter.
Please note that this may affect the classification of
forest/non\-forest.





### Bands



**Pixel Size**
  
25 meters



**Bands**




| Name | Min | Max | Description |
| --- | --- | --- | --- |
| `fnf` | 1 | 3 | Forest/Non\-Forest landcover classification |


**fnf Class Table**




| Value | Color | Description |
| --- | --- | --- |
| 1 | \#006400 | Forest |
| 2 | \#feff99 | Non\-Forest |
| 3 | \#0000ff | Water |




### Terms of Use


**Terms of Use**


JAXA retains ownership of the dataset and cannot guarantee
any problem caused by or possibly caused by using the datasets.
Anyone wishing to publish any results using the datasets should
clearly acknowledge the ownership of the data in the publication.




### Citations



Citations:
* Masanobu Shimada, Takuya Itoh, Takeshi Motooka, Manabu Watanabe,
Shiraishi Tomohiro, Rajesh Thapa, and Richard Lucas, "New Global
Forest/Non\-forest Maps from ALOS PALSAR Data (2007\-2010\)", Remote Sensing
of Environment, 155, pp. 13\-31, December 2014\.
[doi:10\.1016/j.rse.2014\.04\.014\.](https://doi.org/10.1016/j.rse.2014.04.014)





### Explore with Earth Engine


**Important:** 
 Earth Engine is a platform for petabyte\-scale scientific analysis and visualization of
 geospatial datasets, both for public benefit and for business and government users.
 Earth Engine is free to use for research, education, and nonprofit use. To get started, please
 [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)



### Code Editor (JavaScript)



```
vardataset=ee.ImageCollection('JAXA/ALOS/PALSAR/YEARLY/FNF')
.filterDate('2017-01-01','2017-12-31');
varforestNonForest=dataset.select('fnf');
varforestNonForestVis={
min:1,
max:3,
palette:['006400','feff99','0000ff'],
};
Map.setCenter(136.85,37.37,4);
Map.addLayer(forestNonForest,forestNonForestVis,'Forest/Non-Forest');
```



[Open in Code Editor](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/JAXA/JAXA_ALOS_PALSAR_YEARLY_FNF)


[Global 3\-class PALSAR\-2/PALSAR Forest/Non\-Forest Map](/earth-engine/datasets/catalog/JAXA_ALOS_PALSAR_YEARLY_FNF)

A newer version of this dataset with 4 classes for 2017\-2020 can be found in JAXA/ALOS/PALSAR/YEARLY/FNF4 The global forest/non\-forest map (FNF) is generated by classifying the SAR image (backscattering coefficient) in the global 25m resolution PALSAR\-2/PALSAR SAR mosaic so that strong and low backscatter pixels are assigned as "forest" and …

 JAXA/ALOS/PALSAR/YEARLY/FNF,
 alos,alos2,classification,eroc,forest,forest\-biomass,jaxa,landcover,palsar,palsar2,sar

2007\-01\-01T00:00:00Z/2018\-01\-01T00:00:00Z



 \-90 \-180 90 180
 



Google Earth Engine
https://developers.google.com/earth\-engine/datasets








