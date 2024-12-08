head -n 1176 input.txt > input_rules.txt
total=$(wc -l input.txt | cut -d' ' -f1)
echo $total
lines=$((($total)-1176))
echo $lines
tail -n $lines input.txt > input_pages.txt
