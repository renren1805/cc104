import time

arr_kdm = list(range(1_000_000))
start_kdm = time.time()
x_kdm = arr_kdm[500_000] # constant time
end_kdm = time.time()
print("O(1) access time:", end_kdm - start_kdm)

target_kdm = 999_999
start_kdm = time.time()
found_kdm = target_kdm in arr_kdm # linear search
end_kdm = time.time()
print("O(n) search time:", end_kdm - start_kdm)
