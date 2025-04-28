#soldan sağa sayıları 1 artırarak gidiyoruz fakat önceki sayıyı artırmadan,son indexe geldik mi sağdan sola işlem yaptırmaya başlıyoruz.

def sagdan_sola(array, index, step_count, n):
    if index > 0:
        array[index] +=1
        array[n - 1] += 1
        step_count += 1
        step_count = sagdan_sola(array, index - 1, step_count, n)

    return step_count

def soldan_saga(array, index, step_count, n):

    if index < n - 1:
        array[index] += 1
        step_count += 1

        step_count = soldan_saga(array, index + 1, step_count, n)
    else:
        step_count = sagdan_sola(array, index - 1, step_count, n)

    return step_count

def main():
    n = int(input())
    
    array = [0] * n
    step_count = 0 
    
    step_count = soldan_saga(array, 0, step_count, n)

    while array[-1] <= array[-2]:
        array[-1] += 1
        step_count += 1

    print(step_count)

if __name__ == "__main__":
    main()
