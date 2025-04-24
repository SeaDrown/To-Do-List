import math
class FurtherList():
    def __init__(self):
        self.List = []
        self.Title = "To Do List"

    def Add(self, value : str):
        self.List.append(value)

    def DisplayList(self):
        print(f"Displaying {self.Title}")
        count = len(self.List)

        if count > 0:
            spaceCount = math.floor(math.log10(count)) + 1
            currentLimit = 10

            for i, value in enumerate(self.List):
                if i+1 == currentLimit:
                    spaceCount -= 1
                    currentLimit *= 10

                print(f"#{i+1}{" "*spaceCount}| {value}")
    
    def SetTitle(self, newTitle):
        self.Title = newTitle

    @classmethod
    def LoadFromCSV(cls, fileName):
        newList = FurtherList()

        try:
            with open(fileName+".csv", "r") as file:
                for currentLine in file:
                    currentLine = currentLine.strip()
                    arguments = currentLine.split(",") # in this case, only 1 argument is needed.

                    newList.Add(*arguments)

        except FileNotFoundError:
            print(f"There is no such file {fileName}")
            return None
        
        return newList
    
    def Remove(item):
        pass

#newList = FurtherList.LoadFromCSV("template1")
#newList.DisplayList()

secondList = FurtherList()
secondList.SetTitle("Heheheha")

for i in range(1000):
    secondList.Add(f"Item {i}")

secondList.DisplayList()