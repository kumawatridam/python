import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
music = pd.read_csv("indian_music_itunes.csv")    #load dataset
print("First 5 Rows:")  
print(music.head())           # head shows only 5 rows
print("\nColumns:")           # shows column name
print(music.columns)
# combine important columns 
music["features"] = (
    music["artist"].fillna("")+" "+
    music["album"].fillna("")+" "+
    music["genre"].fillna("")
)
print(music["features"].head())
#  convert text into numbers
cv = CountVectorizer()
matrix = cv.fit_transform(music["features"]) 
# comparing similar songs
similarity = cosine_similarity(matrix)
print(similarity)
#Recommanded songs
def recommend(song_name):
    song_name = song_name.lower()
    music["song_name"] = music["song_name"].str.lower()
    if song_name not in music["song_name"].values:
        print("song not found!")
        return
    index = music[music["song_name"]==song_name].index[0]
    distances=list(enumerate(similarity[index]))   #enumerate create index for each song
    songs_list = sorted(distances,key = lambda x:x[1],reverse = True)
    print("\nRecmmanded songs:\n") 
    for i in songs_list[1:6]:
        print("\n Song:",music.iloc[i[0]].song_name)
        print("\n Artist:",music.iloc[i[0]].artist)
        print("\n _____________________________________________")
# take input  from the user
song = input("Enter  song name:")
# call the function
recommend(song)        
