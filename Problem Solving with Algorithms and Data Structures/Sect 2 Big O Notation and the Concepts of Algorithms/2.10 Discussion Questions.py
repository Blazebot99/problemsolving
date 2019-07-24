"ONE"
for i in range(n):
   for j in range(n):
      k = 2 + 2
      
#A single layer nested loop, or one loop inside of another. O(n**2).

"TWO"
for i in range(n):
   k = 2 + 2
     
#A simple iterated for loop. O(n).

"THREE"
i = n
while i > 0:
   k = 2 + 2
   i = i // 2 
#A while loop that has the conditional halved each time. O(logn).

"FOUR"
for i in range(n):
   for j in range(n):
      for k in range(n):
         k = 2 + 2
#A triple nested loop. O(n**3)

"FIVE"
#same as "THREE". 

"SIX"
for i in range(n):
   k = 2 + 2
for j in range(n):
   k = 2 + 2
for k in range(n):
   k = 2 + 2
   
#Three simple, unnested loops. One might be tempted to say O(3n), but the n overpowers the 3 when n gets very large. O(n).