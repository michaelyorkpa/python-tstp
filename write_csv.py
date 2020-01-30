import csv
movies=[["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Fight"]]

with open("C:\\Users\\micha\\AppData\\Local\\Programs\\Python\\Python38\\st.csv","w") as f:
    write=csv.writer(f,delimiter=",")
    for movie_list in movies:
        write.writerow(movie_list)
    
