from Bio.SeqIO import parse
from Bio.SeqUtils import gc_fraction as GC
from argparse import ArgumentTypeError, ArgumentParser as ArgP
from os.path import isfile

def file_path(arg_str):
    if isfile(arg_str):
        return arg_str
    else:
        raise ArgumentTypeError('{} is not a valid path to FASTA file!'.format(arg_str))

arg_parser = ArgP(description='Calculates GC-content for sequences from provided FASTA file.')
arg_parser.add_argument('pathToFASTA', type=file_path)
args = arg_parser.parse_args()

for sequence_record in parse(args.pathToFASTA, 'fasta'):
    print('Sequence ID: {}'.format(sequence_record.id))
    print('Sequence: {}'.format(repr(sequence_record.seq)))
    print('GC-content: {} %'.format(100 * GC(sequence_record.seq)))