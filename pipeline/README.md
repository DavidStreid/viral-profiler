# Viral Profiler Pipeline

## Description
![Pipeline](./resources/img/af_pipeline.png)

## Run
0. Verify dependencies (below) are installed
1. Update the nextflow.config w/ the reference FASTA location
2. Run `nextflow viral-profiler.nf --bamDir {BAM_DIR}`

E.g.
```
$ nextflow viral-profiler.nf --bamDir /PATH/TO/BAM_DIR --fasta /PATH/TO/FASTA_IDX.FA
N E X T F L O W  ~  version 20.01.0
Launching `viral-profiler.nf` [nasty_lorenz] - revision: 2e53dcbf4d
WARN: The access of `config` object is deprecated
V I R A L   P R O F I L E R
===========================
INPUT
   fastaFile: /PATH/TO/FASTA_IDX.FA
   bamDirectory: /PATH/TO/BAM_DIR
   Output Directory: ./vcf (in working directory)

executor >  local (2)
[1a/335d54] process > verifyDependencies [100%] 1 of 1  ✔
[d4/ece1d2] process > variantCall        [  0%] 0 of 1                                                      
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

