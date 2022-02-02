"""

Take a file with mm/dd/yy dates and change them to dd/mm/yy

"""
import pandas as pd
import argparse, datetime


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

mydateparser = lambda x: datetime.datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p")

df = pd.read_csv(args.srcfile, parse_dates=args.datefield, date_parser=mydateparser)
df.to_csv(args.dstfile, index=False)
