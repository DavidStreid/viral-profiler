#!/usr/bin/env nextflow

bamDir = params.bamDir
fastaFile = config.fastaFile
pVal = config.vCallpvalThreshold

println """\
         V I R A L   P R O F I L E R
         ===========================
         INPUT
            fastaFile: ${fastaFile}
            bamDirectory: ${bamDir}
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

    output:
    file '*.vcf' into vcfFiles

    shell:
    '''
    bamFiles=$(find !{bamDir} -type f -name "*.bam")
    for BAM in $bamFiles
    do
        # /Users/Bike_Thoughts/Documents/jhu/spr20/irp/data/bam/ZH9471_3071997.hpv.bam
        bam_name=$(echo $BAM | xargs -n 1 basename)
        bcftools mpileup -f !{fastaFile} $BAM | bcftools call --consensus-caller --pval-threshold !{pVal} > ${bam_name}.vcf
    done
    '''
}
