from src.Generators.JobsGenerator import JobsGenerator
from src.Util.Utils import Utils

ops = JobsGenerator().generate()
operations = sorted(ops, key=lambda x: x.get_duration())
operations_durations = []
for op in operations:
    operations_durations.append(op.get_duration())
    print(op.get_duration(), end=", ")
print("\n")
operations_durations.sort()

sum_duration, avg_duration = 0, 0

for operation in operations:
    sum_duration += operation.get_duration()

sum_duration = round(sum_duration, 2)
avg_duration = round(sum_duration / 7, 2)
print(sum_duration)
print(avg_duration)

operations_len = len(operations)
i, j = 0, 0
chunks = []

# print(Utils.split(sum_duration, 7))
print(Utils.split(operations_durations, 7))

# for chunk in :
#     print('chunk: {}, sum: {}'.format(chunk, sum(chunk)))

# while operations_len > 0:
#     counter = 0
#     chunks_i = []
#     while counter < avg_duration:
#         counter += operations[j].get_duration()
#         chunks_i.append(operations[j])
#         j += 1
#         operations_len -= 1
#     chunks.append(chunks_i)
#     i += 1

# for chunk in chunks:
#     for ch in chunk:
#         print(ch.get_duration(), end=", ")
#     print("\n")
