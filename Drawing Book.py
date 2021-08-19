n = int(input())
p = int(input().strip())

book_pages = tuple(range(1,n))
first_pages = (n//2) - (p//2)
end_pages = p//2
print(min(first_pages,end_pages))