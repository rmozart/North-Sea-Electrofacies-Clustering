# North-Sea-Electrofacies-Clustering
A Machine-Learning study for a geophysical well-log dataset from the North Sea region.


## Index 

- [North-Sea-Electrofacies-Clustering](#north-sea-electrofacies-clustering)
  - [Introduction](#introduction)
  - [The Repository](#therepository)
  - [Methodology](#methodology)
    - [data_preparation](#01_data_preparation)
    - [log_prediction](#02_log_prediction)
    - [facies_prediction](#03_facies_prediction)
    - [well_clustering](#04_well_clustering)
    - [tabnet_experiments](#05_tabnet_experiments)
  - [Contact](#contact)
    - [Personal](#personal)
  - [Disclaimer](#disclaimer)


## Introduction 

This repository is based on a research in Machine Learning and Deep Learning applied to Geology and Geophysics studies. The data in this repository is public and consists of geophysical well log surveys and geological facies interpretations from the North Sea Basin. The data was made publicly available by the [Norwegian Digitalization Agency](https://www.regjeringen.no/en/dep/kmd/organisation/etater-og-virksomheter-under-kommunal--og-moderniseringsdepartementet/Subordinate-agencies-and-institutions/digitaliseringsdirektoratet/id2684200/).

Suggestions and contributions of all kinds are very welcome. To write future codes and push, please refer to the [contact](#contact) section.     

## The Repository

The repository consists of the folders for the data available to reproduce the experiments, the license information, some model results, checkpoint data to avoid excessive RAM usage, the source code, and the main scripts where the ML analysis is made. The structure can be check below:

```
├── Checkpoints  
│   ├── df_main.csv.gz  
|   ├── final_df.csv.gz
│   └── ...
├── Data  
│   ├── Lithology code data.xlsx  
|   ├── location of geolink wells.png
│   └── NPD stratigraphic picks north sea.xlsx
│   └── ...
├── License  
│   ├── GEOLINK License_cc_by_4.pdf   
|   ├── License_README_data.docx 
├── Models
│   ├── Results 
│     ├── randomized_cross_validation_randomclassifier.xlsx  
|     ├── grid_n_search_tabnet.csv
│     └── ...
├── Scripts 
│   ├── clustering.ipynb
|   ├── data_preparation.ipynb
│   └── ...
├── Source
│   ├── Utils
|     ├── multi_df.py 
│     └── wellog.py
│     └── well_plot.py
└── README.md  
```

## Methodology

Under the ``Scripts`` folder the necessary notebooks to reproduce each experiments using the Norwegian dataset are available. A brief description of each notebook objective is presented below following the chronological order. In order to facilitate the dataset reading in each notebook, copies of the necessary data to processed in each step are available under the folder ``checkpoints``.

  - data_preparation.ipynb: contains data processing tasks needed to prepare the dataset for the machine learning studies. It combines a data driven approach with the domain knowledge to appropriately curate the dataset.

  - log_prediction.ipynb: contains a study case of missing geophysical log prediction. The feature selection and ML prediction steps are also present on this notebook. 

  - facies_prediction.ipynb: contains a study case of lithological facies classification using machine learning algorithms.

  - well_clustering.ipynb: contains a study case of well clustering based on geophysical logs and lithological information.

  - tabnet_experiments.ipynb: contains a study case of lithological facies classification using the [Tabnet Model](https://arxiv.org/abs/1908.07442) under the [Pytorch version](https://github.com/dreamquark-ai/tabnet).


## Contact

### Personal

- Reinaldo Mozart - **ML and AI applied to the O&G domain Researcher** - cmmozart@gmail.com
  
- Matheus Oliveira - **ML and AI applied to the O&G domain Researcher** - matheusoliveira.geo@gmail.com


## Disclaimer

The data used in this repository is licensed under the [**Norwegian open data license**](https://data.norge.no/nlod/en/2.0/). In additon, we attribute and acknowledge the [**Geolink**](https://www.geolink-s2.com/) company for providing the data.

