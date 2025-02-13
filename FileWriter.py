from IWrite import IWrite

class FileWriter(IWrite):
    def Write(self,data):
        print("write")
        with open("./keylogger.txt","a") as file:
            file.write(data)


if __name__ == "__main__":
    fw = FileWriter()
    fw.Write("test")