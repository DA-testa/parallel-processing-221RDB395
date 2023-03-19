# Anastasija Bondare 221RDB395
# python3

def p_works(m, data):
    # Sagatavo sarakstu ar darbiem
    jobs = []
    for i in range(m):
        job = [0, i, data[i]]
        jobs.append(job)
    return jobs

def p_threads(n):
    # Sagatavo sarakstu ar patvaļīgiem pavedieniem
    threads = []
    for i in range(n):
        thread = [0, i]
        threads.append(thread)
    return threads

def parallel_processing(n, m, data):
    jobs = p_works(m, data)
    threads = p_threads(n)
    output = []

# Notiek darbu apstrāde
    for job in jobs:
        # Atrod vietu, kur beidzas pavediens
        mini_thread = threads[0]
        min_t_id = 0
        for i in range(len(threads)):
            if threads[i][0] < mini_thread[0]:
                mini_thread = threads[i]
                min_t_id = i
        # Aprēķina sākuma laiku
        start_time = max(mini_thread[0], job[0])
        # Pievieno darba rezultātu sarakstam
        output.append((mini_thread[1], start_time))
        # Atjauno pavediena beigu laiku
        threads[min_t_id][0] = start_time + job[2]

    return output

def main():
    # n un m ievade
    n, m = map(int, input().split())

    #Otrā ievade
    data = list(map(int, input().split()))
    
    result = parallel_processing(n, m, data)
    
    #Izdrukā rezultātu
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()