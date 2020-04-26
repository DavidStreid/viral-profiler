#!/usr/bin/env nextflow

bamDir = params.bamDir
fastaFile = params.fasta
pVal = config.vCallpvalThreshold
outDir = 'vcf'

println """\
         V I R A L   P R O F I L E R
         ===========================
         INPUT
            fastaFile: ${fastaFile}
            bamDirectory: ${bamDir}
            Output Directory: ./${outDir} (in working directory)
         """
         .stripIndent()

process verifyDependencies {
	shell:
	'''
    readonly required_commands=(basename bcftools)
    for cmd in $required_commands; do
      if [ -z $(command -v $cmd) ]
      then
        echo "No binary found for ${cmd}"
        exit 1
      fi
    done
	'''
}


process variantCall {
    input:
    val bamDir
    val fastaFile

    shell:
    '''
    bamFiles=$(find !{bamDir} -type f -name "*.bam")
    for BAM in $bamFiles
    do
        bam_name=$(echo $BAM | xargs -n 1 basename)
        bcftools mpileup -f !{fastaFile} $BAM | bcftools call --consensus-caller --pval-threshold !{pVal} > ${bam_name}.vcf
    done

    vcf_out=!{baseDir}/vcf
    mkdir -p ${vcf_out} && mv *.vcf ${vcf_out}
    '''
}
