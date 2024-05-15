import timeit
import numpy as np

def measure_operation(data_type, operation, iterations=100000):
    if 'float' in data_type:
        setup_code = f"import numpy as np; x = np.array(np.random.rand(), dtype=np.{data_type}); y = np.array(np.random.rand(), dtype=np.{data_type})"
    else:    
        setup_code = f"import numpy as np; x = np.random.randint(1, 100, dtype=np.{data_type}).item(); y = np.random.randint(1, 100, dtype=np.{data_type}).item()"
    stmt_code = f"x {operation} y"
    times = timeit.repeat(stmt=stmt_code, setup=setup_code, repeat=5, number=iterations)
    average_time = np.mean(times)
    variance = np.var(times)
    return average_time, variance

data_types = ['int8', 'int16', 'int32', 'int64', 'float32', 'float64']
# data_types = ['int8', 'int16', 'int32', 'int64', 'float64']
# data_types = ['int8', 'int16', 'int32', 'int64']
operations = ['+', '*']

results = {}
for data_type in data_types:
    for operation in operations:
        avg_time, var_time = measure_operation(data_type, operation)
        results[(data_type, operation)] = (avg_time, var_time)


f = open("phone_runtime.txt", "w+")
for key, value in results.items():
    # print(f"{key[0]} {key[1]}: Avg Time = {value[0]*1e6:.2f} microseconds, Variance = {value[1]*1e12:.2f} picoseconds")
    f.write(f"{key[0]} {key[1]}: Avg Time = {value[0]*1e6:.2f} microseconds, Variance = {value[1]*1e12:.2f} picoseconds\n")
f.close
