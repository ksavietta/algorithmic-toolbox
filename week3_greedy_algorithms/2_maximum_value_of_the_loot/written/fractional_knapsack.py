# Uses python3
import sys

# capacity = 50
# weights = [20, 50, 30]
# values = [60, 100, 120]
def get_optimal_value(capacity, weights, values):
    total_value = 0
    knapsack_capacity = capacity
    weight_val_ratios = []
    for ii in range(len(weights)):
        weight_val_ratios.append({'index': ii, 'ratio': values[ii]/weights[ii]})
    weight_val_ratios = sorted(weight_val_ratios, reverse=True, key=lambda k: k['ratio'])
    for weight_info in weight_val_ratios:
        if knapsack_capacity == 0:
            return total_value
        i_weight = weights[weight_info['index']]
        value = values[weight_info['index']]
        taken = min(i_weight, knapsack_capacity)
        knapsack_capacity = knapsack_capacity - taken
        total_value = total_value + taken * weight_info['ratio']
    return total_value
    # Output:
    # 180.0000

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
