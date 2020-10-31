j = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(j):
    print((c*i).rjust(j-1)+c+(c*i).ljust(j-1))

#Top Pillars
for i in range(j+1):
    print((c*j).center(j*2)+(c*j).center(j*6,'-'))

#Middle Belt
for i in range((j+1)//2):
    print((c*j*5).center(j*6,'-'))    

#Bottom Pillars
for i in range(j+1):
    print((c*j).center(j*2)+(c*j).center(j*6))    

#Bottom Cone
for i in range(j-1,-1,-1):
    print((((c*i)).rjust(j)+c+(c*i).ljust(j)).rjust(j*6))



#split it
import textwrap
def wrap(string,o):
    return "\n".join(string[i:i+o] for i in range(0,len(string),o))
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

