import argparse
import re
import matplotlib.pyplot as plt
import numpy as np


def parse_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
        pattern = r'(\d{4}/\d{2}/\d{2}) (\d{2}:\d{2}:\d{2}) Throughput: (\d+\.\d+) Mbps'
        
        for line in lines:
            line = line.strip()
        
            match = re.search(pattern, line)
            if match:
                data.append(float(match.group(3)))
    
    return data


parser = argparse.ArgumentParser()

parser.add_argument("-system", "--System", help = "Pass System Name")
parser.add_argument("-rust", "--Rust", help = "Pass Rust file path")
parser.add_argument("-go", "--Go", help = "Pass Go file path")

args = parser.parse_args()

rust_data = parse_file(args.Rust)
go_data = parse_file(args.Go)

length = min(len(rust_data), len(go_data))

rust_data = rust_data[:length]
go_data = go_data[:length]

xpoints = np.arange(1, length + 1)

plt.plot(xpoints, rust_data, label = "Rust")
plt.plot(xpoints, go_data, label = "Go")

plt.savefig(f"{args.System}.png")