python main.py | uniq > input_valid
awk '{s+=$1} END {printf "%.0f", s}' input_valid

