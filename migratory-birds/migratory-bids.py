#!/usr/bin/python

def migratoryBirds(arr):
    birds = get_birds( arr )
    birds.sort()
    common_bird = 0
    max_birds = 0
    for b in birds:
        cnt = 0
        for a in arr:
            if b == a:
                cnt = cnt + 1
        if cnt > max_birds:
            max_birds = cnt
            common_bird = b
        print("{} : {} \n".format( b, cnt ) )
    return common_bird   

def get_birds( arr ):
    return list(dict.fromkeys( arr ) )

if __name__ == '__main__':
    arr_count = int( input().strip() )
    arr = list( map( int, input().rstrip().split() ) )
    
    print( migratoryBirds( arr ) )
