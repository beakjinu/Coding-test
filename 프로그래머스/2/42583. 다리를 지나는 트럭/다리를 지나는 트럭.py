from queue import Queue

def solution(bridge_length, weight, truck_weights):
    time = 0
    idx = 0
    current_weight = 0

    bridge = Queue(maxsize=bridge_length)
    for _ in range(bridge_length):
        bridge.put(0)

    n = len(truck_weights)
    while current_weight > 0 or idx < n:
        time += 1
        current_weight -= bridge.get()

        if idx < n and current_weight + truck_weights[idx] <= weight:
            w = truck_weights[idx]
            idx += 1
            bridge.put(w)
            current_weight += w
        else:
            bridge.put(0)

    return time
