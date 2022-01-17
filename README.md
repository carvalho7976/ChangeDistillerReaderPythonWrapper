Source code of the .jar:
  https://github.com/carvalho7976/ChangeDestillerReader
  
To run the script:
python3 changeDistiller.py --pathA --pathB --commits --projectName --absolutePath  --mode 

 --pathA - path of the project to checkout
 --pathB - secodary path of the project (each path will be checked out via git)
 --commits - csv file of commits to be compared (commitA,commitB)
 --projectName - name of the project
 --absolutePath - absolute path of the main folder of the script 
 --mode - if tag, the script will compare all commits with tag and ignore the csv file
