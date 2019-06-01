# !file: crud.py
import json


class System():

    def __init__(self):
        # create text file if it doesn't exist
        self.recordName = "todo.json"
        try:
            self.record = open(self.recordName, "r")
            self.record.close()
        except IOError:
            self.record = open(self.recordName, "w+")
            self.record.close()
        
        # read text file into list
        self.recordData = ""
        with open(self.recordName, "r") as jsonFile:
           self.recordData = jsonFile.read()
        self.recordData = json.loads(self.recordData)

        #print(self.recordData["todolist"])


    def delay(self):
        print("Press enter to continue.")
        input()



    def checkWhere(self, thisValue):
        """
        Returns the key for a given value.
        In the event no key is found the method closes the whole program.
        """

        self.thisValue = thisValue

        for key in self.recordData["todolist"].keys():
            if self.recordData["todolist"][key] == self.thisValue:
                return key
        print("ERROR: keyless value! EXITING")
        exit()



    def checkPresent(self, entry):
        """
        Checks if a particular entry is present (exists)
        in the record.  Returns true if entry
        exists, false if it doesn't (record is unique).
        """
        if entry in self.recordData["todolist"].values():
            return True
        else:
            return False


    def save(self):
        """
        Writes the dictionary data back to the json file.
        """

        # make the dictionary into JSON format
        self.savedData = json.dumps(self.recordData)

        with open(self.recordName, "w") as jsonFile:
            jsonFile.write(self.savedData)


    def create(self, entry):
        
        self.newEntry = entry.strip()
        
        # add entry if it's new
        if self.checkPresent(self.newEntry) == False:
            # add the entry to the end of the dictionary
            self.newkey = 1
            for key in self.recordData["todolist"].keys():
                self.newkey = max(self.newkey, int(key))
                #if (int(key) > newkey): self.newkey = int(key)
            self.newkey += 1

            # write the new record
            self.recordData["todolist"][str(self.newkey)] = self.newEntry
            # save to the json file
            self.save()




    def read(self):
        # format data from the dictionary into list
        self.readData = []
        for value in self.recordData["todolist"].values():
            self.readData.append(value)

        return self.readData


    def delete(self, target):
        # removes value (target) from dictionary

        self.target = target

        if(self.checkPresent(target)):
            del self.recordData["todolist"][self.checkWhere(target)]
            # save to the json file
            self.save()
        else:
            print("ERROR: value not present in dictionary.")
            self.delay()


        
        
            
    def update(self, old, new):
        
        self.old = old.strip()
        self.new = new.strip()
        if (self.checkPresent(old) == True):
            self.recordData["todolist"][self.checkWhere(self.old)] = self.new
            self.save()

            
        else:
            print("ERROR: target not present in record")
            print(self.old)
            print(self.new)
            self.delay()
