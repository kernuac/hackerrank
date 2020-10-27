"""
    n : the number of pages in the book
    p : the page number to turn to
"""
def page_count( n, p ):
   if( n % 2 == 0 ):
        n = n + 1
   return min( ( p / 2,  ( n - p ) / 2 ) )


def main():
    n = int( input() )
    p = int( input() )

    result = page_count( n, p )
    print( result )

if __name__=='__main__':
    main()
