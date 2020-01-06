class Number:
    def __init__(self, array):
        self.array = array
    
    def sort(self):
        numbers = self.array
        for i in range(0, len(numbers)):
            minimum = i
        
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[minimum]:
                    minimum = j

            numbers[minimum], numbers[i] = numbers[i], numbers[minimum]

        print("Numbers have been sorted!:",numbers)
        return numbers
    
    def checkForAltSet(self, num2):
        numbers = self.array
        check = False
        
        letterCounter = 0
        while check == False:
            for i in range(0, (len(numbers) - len(num2) + 1)):
                letterCounter = 0
                for j in range(len(num2)):
                    if numbers[i + j] == num2[j]:
                        letterCounter += 1
                if letterCounter == len(num2):
                    check = True
            
        print(check)

numbers1 = [3, 2, 4, 9, 8, 7]#Python'da array'ler static olarak kullanılıyor bundan ötürü kullanıcı değeri olarak alamıyorum
numbers2 = [3, 4]#NUMPY kütüphanesi ile bu olayı çözebiliyoruz lakin farklı metotlar kullanamıyoruz.
SampleNum1 = Number(numbers1)
SampleNum1.sort()
SampleNum2 = Number(numbers2)
SampleNum2.sort()
SampleNum1.checkForAltSet(numbers2)