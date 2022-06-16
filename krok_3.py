import os
import rawpy
import exifread

path = r"C:\Users\User\Desktop\zachod_rgb\zdjecia"

textfile = open("data_godzina_zdjec.txt", "w")

for n in os.listdir(path):
    pw = str(os.path.join(path, n))
    with open(pw, 'rb') as f:
        tags = exifread.process_file(f)
        for key, value in tags.items():
            if key is not 'JPEGThumbnail':  # do not print (uninteresting) binary thumbnail data
                if key == 'EXIF DateTimeOriginal':
                    a,b = str(value).split()
                    h, m, s = str(b).split(':')
                    h = int(h)
                    m = int(m)
                    s = int(s)
                    sekundy = h * 3600 + m * 60 + s + 3385
                    h = int(sekundy/3600)
                    m = int((sekundy - h * 3600)/60)
                    s = sekundy - h*3600 - m * 60
                    textfile.write("2022_05_31" + " " + str(h) + ":" + str(m) + ":" + str(s) + "\n")
textfile.close()