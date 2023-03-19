# Anastasija Bondare 221RDB395
# python3

def prepared_works(m, data): # Tiek sagatavots saraksts ar darbiem, 
# m - darbu skaits, data - saraksts, ar darbu izpildes laikiem, cik nepieciešams, lai apstrādātu katru sarakstu.
    list_of_jobs = [] # Izveidots tukšs saraksts, kur tiks saglabāti darbi.
    for i in range(m): # Apstrādā elementu i masīvā, kas atrodas starp 0 un m-1.
        work = [0, i, data[i]] # 0 - sākuma laiks, i - darba identifikators , data[i] - darba izpildes laiks.
        list_of_jobs.append(work) # Izdarītais darbs tiek pievienots sarakstam.
    return list_of_jobs # Kad visi darbi tika paveikti, funkcija return atgriež sarakstu, ar sagatavotiem darbiem.

def prepared_threads(n): # n - pavedienu skaits.
    list_of_threads = [] # Jauns, tukšs saraksts ar pavedieniem.
    for i in range(n): # Apstrādā elementu i masīvā, kas atrodas starp 0 un n-1.
        thread = [0, i] # Tiek izeidots pavediens sarakstā ar sākuma laiku 0 un i pozīciju.
        list_of_threads.append(thread) # Izveidotais pavediens tiek pievienots sarakstam.
    return list_of_threads # Tiek atgriezts saraksts ar izveidotajiem pavedieniem.

def parallel_processing(n, m, data):
    list_of_jobs = prepared_works(m, data) # Darbu saraksts, kam tika padota informācija par datu masīvu un darbu skaitu.
    list_of_threads = prepared_threads(n) # Pavedienu saraksts, kam tika padota informācija par pavedienu skaitu.
    output = [] # Izveido tukšu rezultātu sarakstu.

# Notiek darbu apstrāde.
    for work in list_of_jobs: # Iziet caur visiem darbiem sarakstā.
        # Meklē brīvo pavedienu starp visiem.
        first_thread = list_of_threads[0] # Atrod pirmo pavedienu sarakstā.
        first_thread_index = 0 # Pirmā pavediena indeks.
        # Šeit notiek for cikls, kas pārbauda katru pavedienu sarakstā. Ja kāds no pavedieniem beidzas ātrāk,
        # tad pirmais pavediens sarakstā pārņem cita pavediena pozīciju sarakstā.
        for i in range(len(list_of_threads)):
            if list_of_threads[i][0] < first_thread[0]:
                first_thread = list_of_threads[i]
                first_thread_index = i
        # Aprēķina darba sākuma laiku.
        outset = max(first_thread[0], work[0])
        # Pievieno jaunu darba rezultātu sarakstam.
        output.append((first_thread[1], outset))
        # Atjauno pavediena beigu laiku.
        list_of_threads[first_thread_index][0] = outset + work[2]

    return output # Atgriež sarakstu ar visiem veiktajiem darbiem un to laikiem.

def main():
    # Tiek ievadīts pavedienu skaits(n) un darbus skaits(m).
    n, m = map(int, input().split())

    # Tiek ievadīts saraksts, ar darbu izpildes laikiem.
    data = list(map(int, input().split()))
    
    result = parallel_processing(n, m, data)
    
    #Izdrukā rezultātu, pirmā kolonna apzīmēs pavedienu, otrā - sākuma laiku
    for thread, outset in result:
        print(thread, outset)

if __name__ == "__main__":
    main()