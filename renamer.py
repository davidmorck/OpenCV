# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
#Ändra från annotations till mappen du vill ändra namnen i.
def main(): 
      
    for filename in os.listdir("images/fuck"):
        arr=filename.split(".")
        if arr[1]=="jpg":
            dst = arr[0]+ ".JPEG"
            src ='images/fuck/'+ filename 
            dst ='images/fuck/'+ dst 
            
            # rename() function will 
            # rename all the files 
            os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 