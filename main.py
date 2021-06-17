"""
Wierdtext v0.1
"""
import argparse
from modules import decoder
from modules import encoder


parser = argparse.ArgumentParser(description='Shhhh. It\'s top secret.')
parser.add_argument("--mode", type=str, choices=["encode", "decode"], required=True, help="Choose between encoding and decoding text")
parser.add_argument("--text", type=str, help="The text to be processed")
parser.add_argument("--file", type=str, help="File with text to be processed")

args = parser.parse_args()

if args.text:
    text = args.text
elif args.file:
    with open(args.file, 'r') as f:
        text = f.read()[:-1]
else:
    print("error: --text or --file argument required")
    exit()


if __name__ == "__main__":
    if args.mode == "encode":
        result = encoder.encoder(text)
    elif args.mode == "decode":
        result = decoder.decoder(text)
    print(result)
