print("Park Run Timer\n~~~~~~~~~~~~~~\n")
print("Let's go!\n")

total_runners = 0
total_time = 0
fastest_time = float('inf')
slowest_time = 0
fastest_runner = None

while True:
    line = input('> ')
    if line == "END":
        break

    items = line.split("::")
    if len(items) != 2:
        print("Error in data stream. Ignoring. Carry on.")
        continue

    try:
        runner_number = int(items[0])
        time = int(items[1])
    except ValueError:
        print("Error in data stream. Ignoring. Carry on.")
        continue

    total_runners += 1
    total_time += time
    if time < fastest_time:
        fastest_time = time
        fastest_runner = runner_number
    if time > slowest_time:
        slowest_time = time

if total_runners == 0:
    print("No data found. Nothing to do. What a pity.")
else:
    avg_time = total_time / total_runners
    print(f"Total Runners: {total_runners}")
    print(
        f"Average Time:  {int(avg_time // 60)} minutes, {int(avg_time % 60)} seconds")
    print(
        f"Fastest Time:  {int(fastest_time // 60)} minutes, {int(fastest_time % 60)} seconds")
    print(
        f"Slowest Time:  {int(slowest_time // 60)} minutes, {int(slowest_time % 60)} seconds")
    print(f"\nBest Time Here: Runner #{fastest_runner}")
    