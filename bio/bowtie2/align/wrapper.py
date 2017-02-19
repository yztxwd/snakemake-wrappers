__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

assert len(snakemake.input.sample) == 1, "input->sample must have 1 (single-end) or 2 (paired-end) elements."

if len(snakemake.input.sample) == 1:
    reads = "-U {}".format(*snakemake.input.sample)
else:
    reads = "-1 {} -2 {}".format(*snakemake.input.sample)

shell(
    "(bowtie2 --threads {snakemake.threads} {snakemake.params} "
    "-x {snakemake.params.index} {reads} "
    "| samtools view -Sbh -o {snakemake.output[0]} -) {log}")
