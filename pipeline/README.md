# Viral Profiler Pipeline

## Description
![Pipeline](./resources/img/af_pipeline.png)

## Run
```
$ nextflow viral-profiler.nf --bamDir {BAM_DIR}
N E X T F L O W  ~  version 19.10.0
Launching `../viral-profiler.nf` [small_baekeland] - revision: 623c9e78ce
V I R A L   P R O F I L E R
===========================
INPUT
   fastaFile: {config.fastaFile}
   bamDirectory: {BAM_DIR}

executor >  local (2)
[50/c1309e] process > verifyDependencies [100%] 1 of 1 ✔
[cc/8dda59] process > variantCall        [  0%] 0 of 1
```

## Dependencies
* Nextflow
* bcftools

## Install
[bcftools](http://www.htslib.org/download/)

```
$ curl https://get.nextflow.io | bash   # Installs nextflow
```

