'''
Question : You have been asked to help study the population of birds migrating across the continent. 
           Each type of bird you are interested in will be identified by an integer value. Each time a particular 
           kind of bird is spotted, its id number will be added to your array of sightings. 
           You would like to be able to find out which type of bird is most common given a list of sightings. 
           Your task is to print the type number of that bird and if two or more types of birds are equally common, 
           choose the type with the smallest ID number.

Link : https://www.hackerrank.com/challenges/migratory-birds/problem
'''

def migratoryBirds(arr):
    count = [0 for _ in range(max(arr)+1)]
    for i in arr:
        count[i] += 1
    
    return count.index(max(count))
    
if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    
    print(result)
