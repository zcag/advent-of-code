import statistics

input = [int(i) for i in open('input').read().strip().split(',')]
median = round(statistics.median(input))
res = [abs(i-median) for i in input]
print(sum(res))

