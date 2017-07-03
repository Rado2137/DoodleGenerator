import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nlabels', type=int)
parser.add_argument('--style-image', type=str)
parser.add_argument('--style-mask', type=str)
parser.add_argument('--target-mask', type=str)
parser.add_argument('--content-image', type=str)
parser.add_argument('--target-image-prefix', type=str)