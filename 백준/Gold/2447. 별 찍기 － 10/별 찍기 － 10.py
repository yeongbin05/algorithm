def star(n):
    
    if n==1:
        return ['*']
    
    else:
        arr=[]
        draw_stars=star(n//3)
        for stars in draw_stars:
            arr.append(stars*3)
        for stars in draw_stars:
            arr.append(stars+' '*(n//3)+stars)
        for stars in draw_stars:
            arr.append(stars*3)

    return arr
            
        

       
   
print('\n'.join(star(int(input()))))
