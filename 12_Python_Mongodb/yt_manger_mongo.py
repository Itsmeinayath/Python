from pymongo import MongoClient
from bson import ObjectId
# never expose the connection string in the code
client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.2cpnc.mongodb.net/ytmanager", tlsAllowInvalidCertificates=True)
#
# Here "ytmanager" is the name of the database
db = client["ytmanager"]

# Here "videos" is the name of the collection
video_collection = db["videos"]
print(video_collection)


def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']} Name: {video['name']} Time: {video['time']}")
        print("\n")


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print("Video added successfully")


def update_video(video_id, name, time):
    video_collection.update_one(
        # Here we are converting the string video_id to ObjectId
        {"_id": ObjectId(video_id)},
        {"$set": {"name": name, "time": time}})
    print("Video updated successfully")


def delete_video(video_id):
    # Here we are converting the string video_id to ObjectId
    video_collection.delete_one({"_id": ObjectId(video_id)})
    print("Video deleted successfully")


def main():
    while True:
        print("\nYoutube Manager")
        print("1: List all videos")
        print("2: Add a video")
        print("3: Update a video")
        print("4: Delete a video")
        print("5: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the ID of the video to be updated: ")
            name = input("Enter the new name of the video: ")
            time = input("Enter the new time of the video: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the ID of the video to be deleted: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()