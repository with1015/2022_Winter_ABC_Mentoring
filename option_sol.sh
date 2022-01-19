#!/bin/bash


# Usage helper function
usage() {
  echo "Usage: $0 [-j <int>] [-s <int>]"
  echo "  -j  the number of jobs to run"
  echo "  -s  sleep time (sec)"
  echo "  -h  print help message"
  exit 1;
}


# Get option arguments
while getopts ":j:s:h" opt; do
  case "${opt}" in
    s)
        sleep_time=${OPTARG}
        ;;
    j)
        num_job=${OPTARG}
        ;;
    h|*)
        usage
        ;;    
  esac
done

shift $((OPTIND-1))


# Run python works via arguments
for idx in `seq ${num_job}`
do
  python3 python_work.py --time ${sleep_time} &
done

wait
echo "All works done"
