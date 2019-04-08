# !file: crud.py

class System():

    def __init__(self):
        # create text file if it doesn't exist
        self.recordName = "todo.txt"
        try:
            self.record = open(self.recordName, "r")
            self.record.close()
        except IOError:
            self.record = open(self.recordName, "w+")
            self.record.close()


        # read text file into list
        self.recordData = []
        with open(self.recordName, "r") as info:
            self.recordData = info.readlines()

    def delay(self):
        print("Press enter to continue.")
        input()


    def checkPresent(self, entry):
        """
        Checks if a particular entry is present (exists)
        in the record.  Returns true if entry
        exists, false if it doesn't (record is unique).
        """

        with open(self.recordName, "r") as info:
            collection = info.read().split(":")
            if entry in collection:
                return True
            else:
                return False



    def create(self, entry):
        
        self.newEntry = entry
        
        # add entry if it's new
        if self.checkPresent(self.newEntry) == False:
            with open(self.recordName, "a") as info:
                info.write(self.newEntry + ":")
        

    def read(self):
        self.readData = []
        with open(self.recordName, "r") as info:
            self.readData = info.read()

        # format data
        self.readData = self.readData.split(":")
        while '' in self.readData:
            self.readData.remove('')
        
        return self.readData


    def delete(self, target):
        
        self.target = target

        if (self.checkPresent(self.target) == True):
            # overwrite file but without particular entry
            
            with open(self.recordName, "r+") as info:
                self.recordData = info.read().split(":")
                self.recordData.remove(self.target)
                info.seek(0)
                for entry in self.recordData:
                    info.write(entry + ":")
                info.truncate()
        else:
            print("ERROR: target not present in record")
            self.delay()
        
        
            
    def update(self, old, new):
        
        self.old = old
        self.new = new

        self.delete(self.old)
        self.create(self.new)
