import cv2
import time
import random
import dropbox

start_time = time.time()


def take_photo():
    video_capture_object = cv2.VideoCapture(0)
    result = True
    number = random.randint(0, 100)
    while result:
        ret, frame = video_capture_object.read()
        image_name = "img" + str(number) + ".jpg"
        cv2.imwrite(image_name, frame)
        result = False
    return image_name
    print("Snapshot Taken")
    video_capture_object.release()
    cv2.destroyAllWindows()


def upload_files(image_name):
    access_token = "sl.BFVMDIsXMo74zULZt3tk2Es27f29zh07sKvyr_2vME9mRPB0JYIJfzJC9dhZN09LRQ8qkPQo_gYYftp0n3ea3QiZwdVSePxZJoOnr3jPXUbzr_x819Z8Byt7MMKhVBL3xJI-GFwz02PU"
    file1 = image_counter
    file_from = file1
    file_to = "/new_folder/" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(
            f.read, file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File are uploaded")


def main():
    while (True):
        if ((time.time() - start_time) >= 300):
            photo = take_photo()
            upload_files(photo)


main()
