"""
Time limit: 1.00 s Memory limit: 512 MB
In a movie festival n movies will be shown. You know the starting 
and ending time of each movie. 

What is the maximum number of movies you can watch entirely?

Input

The first input line has an integer n: the number of movies.

After this, there are n lines that describe the movies. Each line has two integers a and b: the starting and ending times of a movie.

Output

Print one integer: the maximum number of movies.

Constraints
1 ≤ n ≤ 2⋅10 ** 5
1 ≤ a < b ≤ 10 ** 9

Example

Input:
3
3 5
4 9
5 8

Output:
2
"""

def main():
    n = int(input())
    start_finish = [[int(i) for i in input().split()] for _ in range(n)]
    start_finish.sort(key= lambda x:x[1])
    
    current_end_time = 0
    
    movies = 0

    for start, end in start_finish:
        if start >= current_end_time:
            movies += 1
            current_end_time = end

    print(movies)

if __name__ == "__main__":
    main()