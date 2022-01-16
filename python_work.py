import time
import argparse

parser = argparse.ArgumentParser(description="Argument parser.")
parser.add_argument('--time', default=10, type=int, help='Running time of job')

args = parser.parse_args()

print("Python job start")

sleep_time = args.time
time.sleep(sleep_time)

print("Python job done.")
