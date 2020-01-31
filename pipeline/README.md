# Viral Profiler Pipeline

## Description
![Pipeline](./resources/img/af_pipeline.png)

## Run
```
$ nextflow viral-profiler.nf --bamDir {BAM_DIR}
N E X T F L O W  ~  version 19.10.0
Launching `viral-profiler.nf` [pensive_cuvier] - revision: f327c18c5a
WARN: The access of `config` object is deprecated
V I R A L   P R O F I L E R
===========================
INPUT
   fastaFile: {config.fastaFile}
   bamDirectory: {BAM_DIR}

executor >  local (2)
executor >  local (2)
[7a/3ad15f] process > verifyDependencies  [100%] 1 of 1 ✔
[e0/97cb5c] process > pysamstatsVariation [100%] 1 of 1, failed: 1
[-        ] process > parseVariations     -


```

## Dependencies
* Nextflow
* Python 3
    * [pysamstats](https://www.google.com/search?q=pip+instll+pysamstats&oq=pip+instll+pysamstats&aqs=chrome..69i57j69i59j69i60l2j69i65j69i60l3.2666j0j1&sourceid=chrome&ie=UTF-8)

## Install
```
$ curl https://get.nextflow.io | bash   # Installs nextflow
$ pip install pysamstats
```

