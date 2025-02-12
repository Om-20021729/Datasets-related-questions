def square_prperties(n):
    return {side: {'area': side * side, 
         'perimeter': 4 * side}  for side in range(1,n+1)}

print(square_prperties(3))