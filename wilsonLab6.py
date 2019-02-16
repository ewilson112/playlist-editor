#Emily Wilson
#11-16-18
#HW6- Advanced Algorithms

#Using python 3

import sys

def parseFile(filename):
    lst = []
    infile = open(filename, 'r')
        
    for line in infile:
        line.strip()
        pieces = line.split(",")
        lst.append(pieces)
    return lst

def playlist_transformation (s , t , compareType):
    
    #Computes the edit distance for two playlists s and t, and prints the minimal edits required to transform playlist s into playlist t.
    #Inputs :
    #s: 1st playlist (format: list of (track name, artist , genre) triples) 
    #t: 2nd playlist (format: list of (track name, artist , genre) triples)
    #compareType: String indicating the type of comparison to make.
    #”Song” ( default ): songs in a playlist are considered equivalent if the (song
    #name, artist , genre) triples match.
    #”Genre”: songs in a playlist are considered equivalent if the same genre is
    #used.
    #”Artist”: songs in a playlist are considered equivalent if the same artist is
    #used.
    #Output: The minimum edit distance and the minimal edits required to transform
    #playlist s into playlist t. 
    
    print("Comparing playlist similarity by", compareType)

    table = [[0 for j in range(len(t) +1)] for i in range(len(s) + 1)]
     
    m = len(s)
    n = len(t)
    
    for i in range(m+1):
        table[i][0] = i
    for j in range(n+1):
        table[0][j] = j
         
    for i in range(0, m):
        for j in range(0, n):
            if compareType == "song" or compareType == "Song": #song
                if (s[i] == t[j]): 
                    table[i+1][j+1] = table[i][j]
                else:
                    minDelete = table[i][j+1] + 1
                    minInsert = table[i+1][j] + 1
                    minChange = table[i][j] + 1
                    table[i+1][j+1] = min(minDelete, minInsert, minChange)
            
            elif compareType == "genre" or compareType == "Genre": #genre
                if (s[i][2] == t[j][2]): 
                    table[i+1][j+1] = table[i][j]
                else:
                    minDelete = table[i][j+1] + 1
                    minInsert = table[i+1][j] + 1
                    minChange = table[i][j] + 1
                    table[i+1][j+1] = min(minDelete, minInsert, minChange)
           
            elif compareType == "artist" or compareType == "Artist": #artist
                if (s[i][1] == t[j][1]): 
                    table[i+1][j+1] = table[i][j]
                else:
                    minDelete = table[i][j+1] + 1
                    minInsert = table[i+1][j] + 1
                    minChange = table[i][j] + 1    
                    table[i+1][j+1] = min(minDelete, minInsert, minChange)
            else: #error
                print("not a valid compareType")
         
    maxValue = table[m][n]
    print(maxValue, "edits required to turn playlist 1 into playlist 2.")
    currentTable = maxValue
    
    answerF = []
    currentTable = table[m][n]
    col = []
    while (m > 0 or n > 0): 
      currentTable = table[m][n]
      
      if (m!= 0 and n!= 0):
          col.append(table[m-1][n-1])
      if (m!=0):
          col.append(table[m-1][n])
      if (n!=0):
          col.append(table[m][n-1])
           
      minCost = min(col)

      if minCost == currentTable:  #diag - leave alone
          x = 1, s[m-1]
          m-=1
          n-=1
          answerF.append(x)
          
      elif minCost == table[m-1][n-1]: #diag - replace
          x = 2, s[m-1], t[n-1]
          answerF.append(x)
          m-=1
          n-=1   
          
      elif minCost == table[m-1][n]: #up one - delete
          x = 3, s[m-1]
          m = m-1
          answerF.append(x)
           
      elif minCost == table[m][n-1]: #over one - append
          x = 4, t[n-1]
          n -= 1
          answerF.append(x)          
            
    for line in range(len(answerF)-1, -1, -1): 
        if answerF[line][0] == 1:
            print("Leave", answerF[line][1], "unchanged")
        elif answerF[line][0] == 2:
            print("Replace", answerF[line][1], "with", answerF[line][2])
        elif answerF[line][0] == 3:
            print("Delete", answerF[line][1])
        elif answerF[line][0] == 4:
           print("Insert", answerF[line][1])
         
def main():
    #c = "song"
    #a = parseFile("blues1.txt")
    #b = parseFile("blues2.txt")
    a = parseFile(sys.argv[1])
    b = parseFile(sys.argv[2])
    c = sys.argv[3]
    playlist_transformation(a, b, c)

main()