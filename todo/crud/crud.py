# !file: crud.py

class System():

    def __init__(self):
        # create text file if it doesn't exist
        self.recordName = "todo.txt"
        self.record = open(self.recordName, "w+")
        self.record.close()


        # read text file into list
        self.recordData = []
        with open(self.recordName, "r") as info:
            self.recordData = info.readlines()


    def checkPresent(self, entry):
        """
        Checks if a particular entry is present (exists)
        in the record.  Returns true if entry
        exists, false if it doesn't (record is unique).
        """
        with open(self.recordName, "r") as info:
            if self.newEntry + "\n" in info.readlines():
                return True
            else:
                return False

    def create(self, entry):
        
        self.newEntry = entry
        
        # add entry if it's new
        if self.checkPresent(self.newEntry) == False:
            with open(self.recordName, "a") as info:
                info.write(self.newEntry + "\n")
        

    def read(self):
        self.readData = []
        with open(self.recordName, "r") as info:
            self.readData = info.readlines()
        return self.readData


    def delete(self, target):
        
        self.target = target

        if self.checkPresent(self.target) == False:
            print("ERROR: target not present in record")
            return
        
        # overwrite file but without particular entry
        with open(self.recordName, "r+") as info:
            self.recordData = info.readlines()
            self.recordData.remove(self.target + '\n')
            info.seek(0)
            for entry in self.recordData:
                info.write(entry)
            info.truncate()
            
    def update(self, old, new):
        
        self.old = old
        self.new = new

        self.delete(self.old)
        self.create(self.new)
