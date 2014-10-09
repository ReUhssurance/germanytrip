import MySQLdb
import heapq

#Establish MySQLdb Connection
db = MySQLdb.connect("localhost","root","password","trip");

#Create db Cursor
cur = db.cursor()

#sql = "select * from germany1"
#Get data and store in lists
gr = []
def get():
    temp = []
    y = 0
    db = []
    cur.execute("select * from germany1")
    rows = cur.fetchall()
    for row in rows:
        db.append(row)
    return db
   
#Set tuple to list to be able to manipulate
def convert():
    temp = []
    g = get()
    for i in g:
        for x in i:
            temp.append(x)
        gr.append(temp)
        temp = []

    for i in gr:
        i[3] = float(i[3])
        i[4] = float(i[4])
        if i[6] != None:
            i[6] = float(i[6])
        if i[7] != None:
            i[7] = float(i[7])
        if i[9] != None:    
            i[9] = float(i[9])
        if i[10] != None:
            i[10] = float(i[10])
    return gr

roughDraft = convert()
#print roughDraft
graph = []
def getRoutes(roughDraft):      #get possible routes from full database listing
    temp = []
    for i in roughDraft:
        if i[2] != None:
            temp.append(i[0])
            temp.append(i[2])
            temp.append(i[3])
            temp.append(i[4])
            graph.append(temp)
            temp = []
        if i[5] != None:
            temp.append(i[0])
            temp.append(i[5])
            temp.append(i[6])
            temp.append(i[7])
            graph.append(temp)
            temp = []
        if i[8] != None:
            temp.append(i[0])
            temp.append(i[8])
            temp.append(i[9])
            temp.append(i[10])
            graph.append(temp)
            temp = []
getRoutes(roughDraft)
print graph


def turnIt(change):     #change the order of a list
    temp = []
    temp.append(change[2])
    temp.append(change[0])
    temp.append(change[1])
    temp.append(change[3])
    return temp
    


def primsAlg(g, v):
    temp = []
    minST = []              #MST
    g1 = []
    time = 0
    mstCost = 0
    visitedVertices = []
    allVisited = False
    visitedVertices.append(v)   #assign initial vertex to visited
    for i in g:                 #get values to freq, v, w
        g1.append(turnIt(i))
    
    
    
    heapq.heapify(g1)       #create heap

    temp = heapq.heappop(g1)    #get first temp to compare
    
    while len(minST) < 22 - 1:
        
        while temp[2] in visitedVertices:   #ensure it hasn't been selected
            temp = heapq.heappop(g1)
        
                  
        minST.append(temp)          #set temp to the minimum spanning tree
        mstCost += temp[0]          #add cost up    
        time += temp[3]
        visitedVertices.append(temp[2])     #append w to visitedvertices
        print "Destination: ",temp[2],"Cost: Euro", 0.7693*mstCost,"Travel time: ", time       
        
        
        

primsAlg(graph, 'Stuttgart') 

   
    
    







db.close()
