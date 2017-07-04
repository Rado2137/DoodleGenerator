import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--labels', type=int)
parser.add_argument('--s-image', type=str)
parser.add_argument('--s-mask', type=str)
parser.add_argument('--t-mask', type=str)
parser.add_argument('--t-image-gen', type=str)
parser.add_argument('--content-image', type=str)