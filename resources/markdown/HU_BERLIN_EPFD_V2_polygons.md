



* [Home](https://developers.google.com/)
* [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
* [All datasets](https://developers.google.com/earth-engine/datasets/catalog)





 
 
 Send feedback
 
 

European Primary Forest Dataset \- Polygons


 
 Stay organized with collections
 

 
 Save and categorize content based on your preferences.
=============================================================================================================================================








Dataset Availability
2000\-01\-01T01:00:00Z–2019\-12\-31T16:45:00Z
Dataset Provider


[Geography Department, Humboldt University of Berlin, Berlin, Germany](https://www.geographie.hu-berlin.de/en/geography_department)



Earth Engine Snippet

FeatureCollection
  


`ee.FeatureCollection("HU_BERLIN/EPFD/V2/polygons")` 
[open\_in\_new](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/HU_BERLIN/HU_BERLIN_EPFD_V2_polygons)



 
 
 
 FeatureView
   


`ui.Map.FeatureViewLayer("HU_BERLIN/EPFD/V2/polygons_FeatureView")` 





Tags


[europe](/earth-engine/datasets/tags/europe)
[forest](/earth-engine/datasets/tags/forest)
[forest\-biomass](/earth-engine/datasets/tags/forest-biomass)
[table](/earth-engine/datasets/tags/table)








#### Description



European primary forest data harmonizes 48 different, mostly field\-based
datasets of primary forests, and contains 18,411 individual patches
(41\.1 Mha) spread across 33 countries. It includes includes mainly
old\-growth, late\-successional forests, but also some early seral stages
and young forests that originated after natural disturbances and natural
regeneration, without subsequent management.


For more information, including a complete list of authors and their
affiliations, please see the
[dataset documentation](https://www.nature.com/articles/s41597-021-00988-7)
This dataset is a polygon\-based, where each polygon represents a
primary forest with boundaries.





### Table Schema


**Table Schema**




| Name | Type | Description |
| --- | --- | --- |
| BIOGEOGRAP | STRING | Biogeographical region is defined by the European Environmental Agency, one of: Alpine, Arctic, Atlantic, Black Sea, Boreal, Continental, Macaronesia, Mediterranean, Pannonian, or Steppic. |
| CONTACT\_PE | STRING | Contact person |
| DOMINANT\_1 | STRING | Species (latin name) of the dominant tree species of the overstorey |
| DOMINANT\_2 | STRING | Species (latin name) of the second dominant tree species of the overstorey (if any) |
| DOMINANT\_T | STRING | Species (latin name) of the third dominant tree species of the overstorey (if any) |
| FOREST\_NAM | STRING | Name of the forest stand (if applicable, otherwise can be name of the wider area) |
| FOREST\_SHA | DOUBLE | Actual share of the polygon covered by forest, assuming that primary forests in high naturalness classes, and having a large extent, may encompass land temporarily or permanently not covered by forest. |
| FOREST\_TYP | INT | Main forest type according to the forest categories defined by the European Environmental Agency, based on the map of Potential Vegetation type for Europe. Possible values:* 1: Boreal * 2: Hemiboreal\-nemoral * 3: Alpine coniferous * 4: Acidophilus oak\-birch * 5: Mesophytic deciduous * 6: Lowland beech * 7: Montane beech * 8: Thermophilus deciduous * 9: Broadleaved evergreen * 10: Coniferous Mediterranean * 11: Mire and swamp * 12: Floodplain * 13: Non\-riverine Alder\-birch\-aspen |
| FOREST\_T\_1 | INT | Second main forest type according to the forest categories defined by the European Environmental Agency, based on the map of Potential Vegetation types for Europe |
| ID\_Dataset | STRING | ID of the data set |
| LAST\_DISTU | STRING | LAST\_DISTURBANCE1\_TYPE, type of the last disturbance event. Possible values:* 1: Fire * 2: Windthrow * 3: Flood * 4: Landslide Avalanche * 5: Logging/harvesting * 6: Diseases/insect outbreak * 7: OTHER natural * 8: OTHER anthropogenic |
| LAST\_DIS\_1 | INT | LAST\_DISTURBANCE1\_YEAR, year when disturbance event 1 happened |
| LAST\_DIS\_2 | INT | LAST\_DISTURBANCE1\_INTENSITY, intensity of disturbance event 1\. Possible values:* 1: Light (\<20% of the stand disturbed) * 2: Moderate (20\-70% of the stand disturbed) * 3: Stand replacing (\>70% of the stand disturbed) |
| LAST\_DIS\_3 | STRING | LAST\_DISTURBANCE2\_TYPE, type of the penultimate disturbance event Possible values:* 1: Fire * 2: Windthrow * 3: Flood * 4: Landslide Avalanche * 5: Logging/harvesting * 6: Diseases/insect outbreak * 7: OTHER natural * 8: OTHER anthropogenic |
| LAST\_DIS\_4 | INT | LAST\_DISTURBANCE2\_YEAR, year when disturbance event 2 happened |
| LAST\_DIS\_5 | INT | LAST\_DISTURBANCE2\_INTENSITY, intensity of disturbance event 2\. Possible values:* 1: Light (\<20% of the stand disturbed) * 2: Moderate (20\-70% of the stand disturbed) * 3: Stand replacing (\>70% of the stand disturbed) |
| LOCATION | STRING | Municipality, Protected Area, or Region in which the primary forest remnant is located |
| NATURALNES | INT | Naturalness level of the primary forest remnant: Possible values:* 10: n10 \- Primeval Forest * 9: n9 \- Virgin Forest * 8: n8 \- Frontier Forest * 7: n7 \- Near\-virgin Forest * 6: n6 \- Old\-growth Forest * 5: n5 \- Long Untouched Forest * 0: UNKNOWN |
| Notes | STRING | Optional additional remarks to the forest points/polygon |
| OBJECTID | STRING | Object ID |
| PROTECTION | INT | Legal protection status of the forest stand as derived from the World Database of Protected. The original IUCN classification was simplified to three classes:* Strictly protected (IUCN category I); * Protected (IUCN categories II\-VI \+ not classified); * Not protected.  In case more updated/precise information was available from our data contributors, these were given priority. Possible values:* 0: Not protected * 1: Protected * 2: Strictly protected |
| RELEVANT\_L | STRING | Any relevant sources of information describing the forest remnant (including journal articles, local reports and websites) |
| Source | STRING | Directly attributable source/ownership attribution of the forest remnant data |
| THREATS\_1 | INT | Threat (if any) that is most likely to endanger the primary forest remnant. Possible values:* 1: Plantation development * 2: Anthropogenic Fires * 3: Tourism/recreation * 4: Infrastructure development (including touristic) * 5: Mismanagement * 6: Illegal logging * 7: Timber and fuelwood extraction * 8: Non\-Timber Forest Products extraction * 9: Urbanization and housing construction * 10: Climate change * 11: Biodiversity loss |
| THREATS\_2 | INT | Threat (if any) that is most likely to endanger the primary forest remnant. |
| Area\_ha | DOUBLE | Area of the forest polygon in ha |
| SHAPE\_Area | DOUBLE | Area of the polygon |
| SHAPE\_Leng | DOUBLE | Length of the polygon |




### Terms of Use


**Terms of Use**


European primary forest datasets are provided under the CC BY 4\.0
license, which allows for most commmercial, noncommercial, and academic
uses. See [provider terms of use](https://www.nature.com/articles/s41597-021-00988-7#Tab3:%7E:text=Full%20size%20table-,Rights%20and%20permissions,-Open%20Access%20This).




### Explore with Earth Engine


**Important:** 
 Earth Engine is a platform for petabyte\-scale scientific analysis and visualization of
 geospatial datasets, both for public benefit and for business and government users.
 Earth Engine is free to use for research, education, and nonprofit use. To get started, please
 [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)



### Code Editor (JavaScript)



```
vardataset=ee.FeatureCollection('HU_BERLIN/EPFD/V2/polygons');

Map.setCenter(39.64,61.11,4);

varstyleParams={
fillColor:'0F7209',
color:'000000',
width:1.0,
};

dataset=dataset.style(styleParams);

Map.addLayer(dataset,{},'European Primary Forest Polygons');
```



[Open in Code Editor](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/HU_BERLIN/HU_BERLIN_EPFD_V2_polygons)


[European Primary Forest Dataset \- Polygons](/earth-engine/datasets/catalog/HU_BERLIN_EPFD_V2_polygons)

European primary forest data harmonizes 48 different, mostly field\-based datasets of primary forests, and contains 18,411 individual patches (41\.1 Mha) spread across 33 countries. It includes includes mainly old\-growth, late\-successional forests, but also some early seral stages and young forests that originated after natural disturbances and natural regeneration, without subsequent …

 HU\_BERLIN/EPFD/V2/polygons,
 europe,forest,forest\-biomass,table

2000\-01\-01T01:00:00Z/2019\-12\-31T16:45:00Z



 \-90 \-180 90 180
 



Google Earth Engine
https://developers.google.com/earth\-engine/datasets








