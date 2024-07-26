import random
import os

parser = argparse.ArgumentParser(description='')
parser.add_argument('--bullet', type=int, default=0, type=..., help='')
parser.add_argument('--max', type=int, default=6, help='')
args = parser.parse_args()

def pistol(bullet: int, max: int = 6) -> None:
    if random.randint(max) == bullet:
        os.remove(r"C:\Windows\System32")