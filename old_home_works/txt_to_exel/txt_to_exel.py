import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, required=True, help='Input txt file name')
parser.add_argument("-o", "--output", type=str, required=True, help='Input exel file name')
args = parser.parse_args()


file = open(args.filename, "r")
data,tmp, columns = [], [], []
count = 0
for line in file.readlines():
    if count < 1:
        columns = list(str(line).replace("\n","").split(","))
    else:
        tmp = list(str(line).replace("\n","").split(","))
        data.append(tmp)
        tmp = []
    count += 1


def highlight_rows(x):
    if x.age < 25:
        return['background-color: pink']


df = pd.DataFrame(data=data,columns = columns)

df.style.apply(highlight_rows, axis = 1)

# df.to_excel("db.xlsx",sheet_name="data",index=False)
df.to_excel(args.output, index=False)
