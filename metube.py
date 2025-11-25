import json, time, cv2, os

with open("files/metube/vids.json", "r") as f:
    vids = json.loads(f.read())

def post(name, content, ftype):
    if name in vids:
        while True:
            confirm = input(f'Video "{name}" already exsists! Are you sure you want post and overwrite video? (y/n): ').lower()
            if confirm == "y" or confirm == "n":
                break
            print('Please only enter "y", meaning yes or "n", meaning no. Capitalisation does not matter.')
        if confirm == "n":
            return
    with open("files/metube/vids/" + name + ftype, "wb") as f:
        f.write(content)
    vids[name] = {"path": name + ftype, "date": time.strftime("%d.%m.%Y %H:%M:%S")}
    with open("files/metube/vids.json", "w") as f:
        json.dump(vids, f, indent=4)

def openvid(path, title):

    def play():
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow(title, frame)
                cv2.waitKey(25)
            else:
                break

    cap = cv2.VideoCapture("files/metube/vids/" + path)

    if not cap.isOpened():
        print("Error opening video file")
        cap.release()
        cv2.destroyAllWindows()
        return
    play()
    if path.split(".")[-1] == "gif":
        for i in range(10):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            play()

    cap.release()

    cv2.destroyAllWindows()

def view(vid):
    if vid in vids:
        print("Video found, opening...")
        path = vids[vid]["path"]
        openvid(path, vid)
        
    else:
        print("Video not found")

def app():
    print("Welcome to MeTube!")
    while True:
        print("Please choose an option:")
        print(" 1. Post video")
        print(" 2. View video")
        print(" 3. List videos")
        print(" 4. Delete video")
        print(" 5. Exit")
        while True:
            try:
                opt = int(input("What do you want to do? (1/2/3/4/5): "))
                if not opt > 5 or opt < 1:
                    break
            except:
                pass
            print("Please only enter numbers from 1 to 5.")
        if opt == 1:
            print("Please enter video path:")
            path = input()
            try:
                with open(path, "rb") as f:
                    vid = f.read()
                name = input("Please enter video name:\n")
                ftype = "." + path.split(".")[-1]
                post(name, vid, ftype)
            except FileNotFoundError:
                print("File path does not exsist.")
        elif opt == 2:
            print("Please enter video name:")
            name = input()
            view(name)
        elif opt == 3:
            print("Here is a list of videos:\n")
            for i in vids:
                print(f'"{i}":\n  -Time posted: {vids[i]["date"]}\n  -File name: {vids[i]["path"]}\n')
        elif opt == 4:
            vid = input("Please enter video name to delete:\n")
            if vid in vids:
                while True:
                    confirm = input(f'Are you sure you want to delete "{vid}"? (y/n): ').lower()
                    if confirm == "y" or confirm == "n":
                        break
                    print('Please only enter "y", meaning yes or "n", meaning no. Capitalisation does not matter.')
                if confirm == "y":
                    os.remove("files/metube/vids/" + vids[vid]["path"])
                    del vids[vid]
                    with open("files/metube/vids.json", "w") as f:
                        json.dump(vids, f, indent=4)
                    print(f'Removed {vid}')
        elif opt == 5:
            break

app()