import random
import time
import webbrowser

break_count = 0
total_breaks = 5

my_fav_songs = ['https://www.youtube.com/watch?v=eiGdsH1g20k',
                'https://www.youtube.com/watch?v=JGwWNGJdvx8',
                'https://www.youtube.com/watch?v=kffacxfA7G4',
                'https://www.youtube.com/watch?v=euCqAq6BRa4',
                'https://www.youtube.com/watch?v=op4B9sNGi0k',
                'https://www.youtube.com/watch?v=vvLBXO94EfA',
                'https://www.youtube.com/watch?v=czkGKhQm-54']
print("The Program Started on " + time.ctime())  #To display time
while(break_count < total_breaks):
    time.sleep(2*60*60) # Break time 2 Hrs
    webbrowser.open(random.choice(my_fav_songs))  #Rxtracting Song randomly from your favourite songs
    break_count += 1
