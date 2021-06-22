import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self,fileFrom , fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(fileFrom, 'rb') 
        dbx.files_upload(f.read(), fileTo) 

def main(): 
        access_token = 'CrjnNLeU8pMAAAAAAAAAAdK87A7CoyFxBotCN6nT_cOzUOoNAo0BOsN-5QXYd7w5' 
        transferData = TransferData(access_token) 
        file_from = input("Enter the file path to transfer : -") 
        file_to = input("enter the full path to upload to dropbox:- ") # This is the full path to upload the file to, including name that you wish the file to be called once uploaded. 
        transferData.upload_file(file_from, file_to) 
        print("file has been moved !!!") 
main()
        

