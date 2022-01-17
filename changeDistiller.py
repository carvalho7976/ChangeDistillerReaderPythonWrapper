import pydriller
import argparse
from csv import reader
import shutil
import subprocess

import git


          
def runJar(pathA, pathB, currentCommit, previousCommit):
    filesA = pathA.files()
    filesB = pathB.files()
    filesA = [x for x in filesA if x.endswith('.java')]
    filesB = [x for x in filesB if x.endswith('.java')]
    csvPath = args.absolutePath + args.projectName + "-results.csv"
    try:
        f = open(csvPath, "x")
    except:
        print("file exists")
    for file in filesA:
        file_temp = file.replace(args.absolutePath+"projectA", '')
        if any(file_temp in s for s in filesB):
            file2 = args.absolutePath+"projectB" + file_temp
            #classPreviousCommit classCurrentCommit csvPath projectName currentCommit previousCommit
            subprocess.call(['java', '-jar', 'ChangeDistillerReader-0.0.1-SNAPSHOT-jar-with-dependencies.jar',file2, file,csvPath, args.projectName,currentCommit,previousCommit])

     


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description='Extractor for changeDistiller')
    ap.add_argument('--pathA', required=True)
    ap.add_argument('--pathB', required=True)
    ap.add_argument('--commits', required=True, help='csv with list of commits to compare commitA and commitB')
    ap.add_argument('--projectName', required=True)
    ap.add_argument('--absolutePath', required=True)
    ap.add_argument('--mode', required=True,help='mode - tag for commits with tag, csv - for csv of commits')
    args = ap.parse_args()

    #folder with repo: projectA and projectB

    pathA = pydriller.Git(args.pathA)
    pathB = pydriller.Git(args.pathB)
    repo = git.Repo(args.pathA)
    tags = repo.tags
    with open(args.commits, 'r') as read_obj:
        csv_reader = reader(read_obj)
        i = 0
        commit_A = ''
        commit_B = ''
        if(args.mode == 'tag'):
            for tag in tags:
                if(i ==0):
                    commit_A = tag
                    i +=1
                else:
                 pathA.checkout(commit_A.tag)
                 pathB.checkout(tag.tag)
                 runJar(pathA,pathB,str(commit_A.tag),str(tag.tag))
                 commit_A = tag
        else:
            for row in csv_reader:
                pathA.checkout(row[0])
                pathB.checkout(row[1])
                runJar(pathA,pathB,row[0],row[1])
   
 