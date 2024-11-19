import json

youtube = "youtube.txt"

def load_data():
    try:
        with open(youtube,"r") as file:
            return json.load(file)
            # test =  json.load(file)
            # # print(type (test))
            # print(test)
    except FileNotFoundError:
        return []

    # finally:
    #     pass

def save_data_helper(videos):
    with open(youtube,"w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*50)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['title']}, Duration: {video['time']}")
    print("\n")
    print("*"*50)

def add_video(videos):
    name = input("Enter the title of the video: ")
    time = input("Enter video duration: ")
    videos.append({"title":name,"time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update: "))
    if 1 <= index <len(videos):
        name = input("Enter the title of the video: ")
        time = input("Enter video duration: ")
        videos[index-1] = {"title":name,"time":time}
        save_data_helper(videos)
    else:
        print("Invalid video number. Please try again")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to delete: "))
    if 1 <= index <len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video number. Please try again")
        

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager Application")
        print("----------------------------")
        print("Please select an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("3. delete a youtube video")
        print("5. Exit the application")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again")
                continue

if __name__ == "__main__":
    main()
