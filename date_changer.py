"""

Take a file with mm/dd/yy dates and change them to dd/mm/yy

"""
import pandas as pd
import argparse


def getArgs():
    parser = argparse.ArgumentParser(description="Change date formats")
    parser.add_argument("--srcfile", "-s", help="Source file", required=True)
    parser.add_argument("--dstfile", "-d", help="Destination file", required=True)
    parser.add_argument(
        "--datefield",
        "-f",
        nargs="+",
        default=["Agent Check-in Time", "Enrollment Time"],
        help="Date field to change. Default = 'Agent Check-in Time', 'Enrollment Time'",
    )
    return parser.parse_args()


args = getArgs()

df = pd.read_csv(args.srcfile, parse_dates=args.datefield)
df.to_csv(args.dstfile, index=False)
