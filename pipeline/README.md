# Viral Profiler Pipeline

## Description
![Pipeline](./resources/img/af_pipeline.png)

## Run
0. Verify dependencies (below) are installed
1. Update the nextflow.config w/ the reference FASTA location
2. Run `nextflow viral-profiler.nf --bamDir {BAM_DIR}`

E.g.
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
## Install
### Dependencies
* Nextflow
* bcftools
* java (for nextflow)

### Steps
1. bcftools - Go to [bcftools](http://www.htslib.org/download/) and follow the instructions. Afterwards, add bcftools to path.
2. java - Go to the [java JDK download page](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html) and follow the instructions
3. nextflow - Once java is installed, run the command below. For more information, go to the [nextflow documentation](https://www.nextflow.io/)
    * Recommended that after install, you add `nextflow` to your path  
```
$ curl https://get.nextflow.io | bash   # Installs nextflow
```

