#!/usr/bin/env nextflow

bamDir = params.bamDir
fastaFile = config.fastaFile

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
    readonly required_commands=(pysamstats basename)
    for cmd in $required_commands; do
      if [ -z $(command -v $cmd) ]
      then
        echo "No binary found for ${cmd}"
        exit 1
      fi
    done
	'''
}

process pysamstatsVariation {
    input:
    val bamDir
    val fastaFile

    output:
    file '*.variation' into variationFiles

	shell:
	'''
	bamFiles=$(find !{bamDir} -type f -name "*.bam")
    for BAM in $bamFiles
    do
        # /Users/Bike_Thoughts/Documents/jhu/spr20/irp/data/bam/ZH9471_3071997.hpv.bam
        bam_name=$(echo $BAM | xargs -n 1 basename)
	    pysamstats --fasta !{fastaFile} --type variation $BAM > ${bam_name}.variation
    done
	'''
}

process parseVariations {
    input:
    file variationFiles

	shell:
	'''
    for vFile in !{variationFiles}
    do
        base_name=$(echo $vFile | xargs -n 1 basename)
        dockerReadDir=/data
        dockerWriteDir=/parsed

        # Resolve symbolic link
        dataDir=$(dirname $(readlink $vFile))

        docker run --mount type=bind,source=$dataDir,target=$dockerReadDir,readonly \
                   --mount type=bind,source="$(pwd)",target=$dockerWriteDir \
                   pysamstats-variant-parser:1.0 $dockerReadDir/$vFile $dockerWriteDir/$base_name.parsed
    done
	'''
}
