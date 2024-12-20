import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               NAME TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main():
   while True:
       print("\n Youtube manager app with Database")
       print("------------------------------------")
       print("Please select an option")
       print("1. List all youtube videos")
       print("2. Add a youtube video")
       print("3. Update a youtube video details")
       print("4. delete a youtube video")
       print("5. Exit the application")
       print("----------------------------")
       choice = input("Enter your choice: ")
       if choice == "1":
           list_all_videos()
           print("----------------------------")
        #    print(list_all_videos())
       elif choice == "2":
           name= input("Enter the title of the video: ")
           time = input("Enter video duration: ")
           add_video(name, time)
           print("----------------------------")
           print("Video added successfully")
       elif choice == "3":
           video_id = input("Enter the video number you want to update: ")
           name= input("Enter the title of the video: ")
           time = input("Enter video duration: ")
           update_video(video_id,name, time)
           print("----------------------------")
           print("Video updated successfully")
       elif choice == "4":
           video_id = input("Enter the video number you want to delete: ")
           delete_video(video_id)
           print("----------------------------")
           print("Video deleted successfully")
       elif choice == "5":
           break   
       else:
              print("Invalid choice. Please try again")
              continue 
   conn.close()            
if __name__ == "__main__":
    main()