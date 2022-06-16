import cv2 as cv
import os


path = r"C:\Users\User\Desktop\zachod_rgb\sformatowane"


list_of_images = os.listdir(path)
# dlugosc = 24

file = open("wspolrzedne.txt", "r")


cord_list_file = file.readlines()

# wielkosc uzglednianego obszaru - 800x1300
h = 800
w = 1300

lista_danych_rgb = []
lista_list_jasnosc = []
pozycja_srodka_slonca = []

for i in range(len(list_of_images)):
    pw = str(os.path.join(path, list_of_images[i]))

    x1, y1 = cord_list_file[i].split()
    x1 = int(x1)
    y1 = int(y1)

    img = cv.imread(pw)[y1:(y1+h),x1:(x1+w)]

    rgb_list = [0 for i in range(16)]
    ilosc_do_pozycji = 0
    ilosc_rgb = 0
    suma_y_do_pozycji = 0
    suma_x_do_pozycji = 0
    suma_r = 0
    suma_g = 0
    suma_b = 0

    for akt_wysokosc in range(h):
        for akt_szerokosc in range(w):
            r, g, b = img[akt_wysokosc, akt_szerokosc]
            r = int(r)
            g = int(g)
            b = int(b)
            suma = r + g + b
            rgb_list[int(suma / 50)] += 1
            if suma >= 750:
                suma_x_do_pozycji += akt_szerokosc
                suma_y_do_pozycji += akt_wysokosc
                ilosc_do_pozycji += 1
            if suma >= 200:
                ilosc_rgb += 1
                suma_r += r
                suma_g += g
                suma_b += b


    przewidywana_pozycja_x = int(suma_x_do_pozycji/ilosc_do_pozycji)
    przewidywana_pozycja_y = int(suma_y_do_pozycji/ilosc_do_pozycji)

    pozycja_srodka_slonca.append((przewidywana_pozycja_x,przewidywana_pozycja_y))
    lista_danych_rgb.append([suma_r,suma_g,suma_b,ilosc_rgb])
    lista_list_jasnosc.append([rgb_list])


textfile = open("dane_rgb3.txt", "w")
for element in lista_danych_rgb:
    textfile.write(str(element) + "\n")
textfile.close()

