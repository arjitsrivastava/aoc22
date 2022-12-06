def solution(stream_size):
    f = open('day_6_input.txt').readlines()[0].strip()
    current_idx = 0
    for i in range(0, len(f) - stream_size):
        current_stream = f[i:i + stream_size]
        if len(set(current_stream)) == stream_size:
            current_idx = i
            break
        current_idx += 1
    print(current_idx + stream_size)


if __name__ == "__main__":
    solution(stream_size=4)
    solution(stream_size=14)
