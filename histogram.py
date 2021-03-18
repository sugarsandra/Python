import random
def histogram(number,times):
    print(number,':', end='')
    for i in range(times):
        print('*',end='')
    print('('+str(times)+')')

def randomList(number):
    lista=[]
    for i in range(number):
        lista.append(random.randint(1,6))
    return lista
        
def frequency(lista):
    freqs=[]
    nums=[]
    for num in lista:
        if num not in nums:
            nums.append(num)     # λίστα με τους αριθμούς
            times=lista.count(num)
            freqs.append(times)   # λίστα με τη συχνότητα

    return nums,freqs
    
def  frequency_histogram( ):
    N=int(input("Δώστε το πλήθος των τυχαιων αριθμών"))
    numList= randomList(N)
    print(numList)
    numbers,frequences = frequency(numList)
    for i in range(len(numbers)):     
        histogram(numbers[i], frequences[i] )
        
if __name__=='__main__':
    frequency_histogram()
