class reverse:
    def rev(self,number):
        r = 0
        while number > 0:
            s = number%10
            r = r*10 + s
            number = int(number/10)
            
        return r

number = int(input("Enter a number:\n"))
reve = reverse()
r = reve.rev(number)
print(r)