import argparse


parser = argparse.ArgumentParser(description='unix like cp command implemented in python')
parser.add_argument('original_file', metavar='from', type=argparse.FileType('r', encoding="utf8"), nargs='+',
                    help='original file name.')
parser.add_argument('file_name', metavar='to', type=argparse.FileType('w', encoding="utf8"), nargs='+',
                    help='file name to copy')
args = parser.parse_args()
#print(args.original_file, args.original_file)

print(args.original_file[0].readlines())


    
