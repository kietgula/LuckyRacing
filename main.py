import random
import pygame
import sys
from pygame.locals import *

CHIEURONGCUASO = 720
CHIEUDAICUASO = 1280

# FONT = pygame.font.SysFont('Corbel', 35)

# Khai báo chung
soDemXepHang = 1
TRAI = (random.randrange(-20, 0), 0)
PHAI = (random.randrange(0, 20), 0)
LEN = (0, random.randrange(-20, 0))
XUONG = (0, random.randrange(0, 20))
huong1 = huong2 = huong3 = huong4 = huong5 = (0, 0)
x1 = x2 = x3 = x4 = x5 = y1 = y2 = y3 = y4 = y5 = 0

# NhacDua=pygame.mixer.music.load("")


# Khai báo mũi tên đánh dấu xe
muiTen = pygame.image.load("MuiTen.png")
# Khai báo hiệu ứng spell

# Khai báo map
MAP1 = pygame.image.load("map1.png")
MAP2 = pygame.image.load("map2.png")
MAP3 = pygame.image.load("map3.png")
MAP4 = pygame.image.load("map4.png")
MAP5 = pygame.image.load("map5.png")

# khai báo xe


# set 1
xe1_quaiXanh = pygame.image.load("QuaiXanh.png")
xe1_quaiDen = pygame.image.load("QuaiDen.png")
xe1_quaiDo = pygame.image.load("QuaiDo.png")
xe1_quaiBlue = pygame.image.load("QuaiBlue.png")
xe1_quaiHong = pygame.image.load("QuaiPink.png")
# set 2
xe2_xeDo = pygame.image.load("XeDoPhai.png")
xe2_xeBlue = pygame.image.load("XeBluePhai.png")
xe2_xeHong = pygame.image.load("XeHongPhai.png")
xe2_xeVang = pygame.image.load("XeVangPhai.png")
xe2_xeXanh = pygame.image.load("XeXanhPhai.png")
# set 3
xe3_meoDen = pygame.image.load("MeoDenPhai.png")
xe3_meoDo = pygame.image.load("MeoDoPhai.png")
xe3_meoVang = pygame.image.load("MeoVangPhai.png")
xe3_meoXam = pygame.image.load("MeoXamPhai.png")
xe3_meoXanh = pygame.image.load("MeoXanhPhai.png")
# set 4
xe4_CaoBoi = pygame.image.load("NguoiCaoBoiPhai.png")
xe4_CaoBoiGai = pygame.image.load("NguoiCaoBoiGaiPhai.png")
xe4_Ninja = pygame.image.load("NguoiNinjaPhai.png")
xe4_NinjaGai = pygame.image.load("NguoiNinjaGaiPhai.png")
xe4_Robot = pygame.image.load("NguoiRobotPhai.png")
# set 5
xe5_Kiet = pygame.image.load("TeamKiet_1.png")
xe5_Khang = pygame.image.load("TeamKR_1.png")
xe5_Loc = pygame.image.load("TeamLoc_1.png")
xe5_Minh = pygame.image.load("TeamMinh_1.png")
xe5_Long = pygame.image.load("TeamLong_1.png")

# phần khai báo tạm
# phần khai báo tạm
tongTien = 10
map = 1
xe = 1
SoundOn = True
SoLuongQuayDau = 5
SoLuongDungLai = 5
SoLuongHoanDoi = 5
SoLuongVeDich = 5
meoVang = 1
meoXanh = 2
meoXam = 1
meoDo = 2
meoDen = 1
TeamKiet = 1
TeamKhang = 2
TeamLoc = 1
TeamMinh = 1
TeamLong = 2
NguoiCaoBoi = 1
NguoiCaoBoiGai=2
NguoiNinja=1
NguoiNinjaGai=2
NguoiRobot=1
xeCuoc = 0
SoLanChoi = SoLanHang = SoLanHang2 = SoLanHang3 = SoLanHang4 = SoLanHang5 = 0


# -----------------------------MenuZone---------------------------------
#######################################################################
# Hàm main chính: Khởi tạo và gọi hàm MainMenu()
def main():
    global MANHINHCUASO
    global CHIEURONGCUASO, CHIEUDAICUASO
    pygame.init()
    pygame.mixer.music.load("NhacNen.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    MANHINHCUASO = pygame.display.set_mode((CHIEUDAICUASO, CHIEURONGCUASO))
    pygame.display.set_caption('Lucky Race')
    login()


# Hàm chọn user và save game
def login():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    global tongTien
    global USER
    global user
    global SoLuongVeDich, SoLuongDungLai, SoLuongHoanDoi, SoLuongQuayDau
    global SoLanChoi, SoLanHang1, SoLanHang2, SoLanHang3, SoLanHang4, SoLanHang5
    screen = pygame.display.set_mode((1280, 720))
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 510 <= mouse[0] <= 769 and 308 <= mouse[1] <= 367:
                    ClickSound.play()
                    USER = open('user1.txt', "r")
                    user = 1
                    tongTien = int(USER.readline())
                    SoLuongDungLai = int(USER.readline())
                    SoLuongVeDich = int(USER.readline())
                    SoLuongHoanDoi = int(USER.readline())
                    SoLuongQuayDau = int(USER.readline())
                    SoLanChoi = int(USER.readline())
                    SoLanHang1 = int(USER.readline())
                    SoLanHang2 = int(USER.readline())
                    SoLanHang3 = int(USER.readline())
                    SoLanHang4 = int(USER.readline())
                    SoLanHang5 = int(USER.readline())

                    MainMenu()
                if 510 <= mouse[0] <= 769 and 393 <= mouse[1] <= 450:
                    ClickSound.play()
                    USER = open('user2.txt', "r")
                    user = 2
                    tongTien = int(USER.readline())
                    SoLuongDungLai = int(USER.readline())
                    SoLuongVeDich = int(USER.readline())
                    SoLuongHoanDoi = int(USER.readline())
                    SoLuongQuayDau = int(USER.readline())
                    SoLanChoi = int(USER.readline())
                    SoLanHang1 = int(USER.readline())
                    SoLanHang2 = int(USER.readline())
                    SoLanHang3 = int(USER.readline())
                    SoLanHang4 = int(USER.readline())
                    SoLanHang5 = int(USER.readline())
                    MainMenu()
                if 510 <= mouse[0] <= 769 and 475 <= mouse[1] <= 531:
                    ClickSound.play()
                    USER = open('user3.txt', "r")
                    user = 3
                    tongTien = int(USER.readline())
                    SoLuongDungLai = int(USER.readline())
                    SoLuongVeDich = int(USER.readline())
                    SoLuongHoanDoi = int(USER.readline())
                    SoLuongQuayDau = int(USER.readline())
                    SoLanChoi = int(USER.readline())
                    SoLanHang1 = int(USER.readline())
                    SoLanHang2 = int(USER.readline())
                    SoLanHang3 = int(USER.readline())
                    SoLanHang4 = int(USER.readline())
                    SoLanHang5 = int(USER.readline())
                    MainMenu()
                if 510 <= mouse[0] <= 769 and 557 <= mouse[1] <= 612:
                    ClickSound.play()
                    USER = open('user4.txt', "r")
                    user = 4
                    tongTien = int(USER.readline())
                    SoLuongDungLai = int(USER.readline())
                    SoLuongVeDich = int(USER.readline())
                    SoLuongHoanDoi = int(USER.readline())
                    SoLuongQuayDau = int(USER.readline())
                    SoLanChoi = int(USER.readline())
                    SoLanHang1 = int(USER.readline())
                    SoLanHang2 = int(USER.readline())
                    SoLanHang3 = int(USER.readline())
                    SoLanHang4 = int(USER.readline())
                    SoLanHang5 = int(USER.readline())
                    MainMenu()
                if 510 <= mouse[0] <= 769 and 639 <= mouse[1] <= 692:
                    ClickSound.play()
                    USER = open('user5.txt', "r")
                    user = 5
                    tongTien = int(USER.readline())
                    SoLuongDungLai = int(USER.readline())
                    SoLuongVeDich = int(USER.readline())
                    SoLuongHoanDoi = int(USER.readline())
                    SoLuongQuayDau = int(USER.readline())
                    SoLanChoi = int(USER.readline())
                    SoLanHang1 = int(USER.readline())
                    SoLanHang2 = int(USER.readline())
                    SoLanHang3 = int(USER.readline())
                    SoLanHang4 = int(USER.readline())
                    SoLanHang5 = int(USER.readline())
                    MainMenu()
        background = pygame.image.load("login.png")
        screen.blit(background, (0, 0))
        pygame.display.update()


def save():
    global SoLuongDungLai, SoLuongVeDich, SoLuongHoanDoi, SoLuongQuayDau
    global SoLanChoi, SoLanHang1, SoLanHang2, SoLanHang3, SoLanHang4, SoLanHang5
    if user == 1:
        USER = open("user1.txt", "w")
        USER.write(str(tongTien) + "\n")
        USER.write(str(SoLuongDungLai) + "\n")
        USER.write(str(SoLuongVeDich) + "\n")
        USER.write(str(SoLuongHoanDoi) + "\n")
        USER.write(str(SoLuongQuayDau) + "\n")
        USER.write(str(SoLanChoi) + "\n")
        USER.write(str(SoLanHang1) + "\n")
        USER.write(str(SoLanHang2) + "\n")
        USER.write(str(SoLanHang3) + "\n")
        USER.write(str(SoLanHang4) + "\n")
        USER.write(str(SoLanHang5) + "\n")

    if user == 2:
        USER = open("user2.txt", "w")
        USER.write(str(tongTien) + "\n")
        USER.write(str(SoLuongDungLai) + "\n")
        USER.write(str(SoLuongVeDich) + "\n")
        USER.write(str(SoLuongHoanDoi) + "\n")
        USER.write(str(SoLuongQuayDau) + "\n")
        USER.write(str(SoLanChoi) + "\n")
        USER.write(str(SoLanHang1) + "\n")
        USER.write(str(SoLanHang2) + "\n")
        USER.write(str(SoLanHang3) + "\n")
        USER.write(str(SoLanHang4) + "\n")
        USER.write(str(SoLanHang5) + "\n")
    if user == 3:
        USER = open("user3.txt", "w")
        USER.write(str(tongTien) + "\n")
        USER.write(str(SoLuongDungLai) + "\n")
        USER.write(str(SoLuongVeDich) + "\n")
        USER.write(str(SoLuongHoanDoi) + "\n")
        USER.write(str(SoLuongQuayDau) + "\n")
        USER.write(str(SoLanChoi) + "\n")
        USER.write(str(SoLanHang1) + "\n")
        USER.write(str(SoLanHang2) + "\n")
        USER.write(str(SoLanHang3) + "\n")
        USER.write(str(SoLanHang4) + "\n")
        USER.write(str(SoLanHang5) + "\n")

    if user == 4:
        USER = open("user4.txt", "w")
        USER.write(str(tongTien) + "\n")
        USER.write(str(SoLuongDungLai) + "\n")
        USER.write(str(SoLuongVeDich) + "\n")
        USER.write(str(SoLuongHoanDoi) + "\n")
        USER.write(str(SoLuongQuayDau) + "\n")
        USER.write(str(SoLanChoi) + "\n")
        USER.write(str(SoLanHang1) + "\n")
        USER.write(str(SoLanHang2) + "\n")
        USER.write(str(SoLanHang3) + "\n")
        USER.write(str(SoLanHang4) + "\n")
        USER.write(str(SoLanHang5) + "\n")
    if user == 5:
        USER = open("user5.txt", "w")
        USER.write(str(tongTien) + "\n")
        USER.write(str(SoLuongDungLai) + "\n")
        USER.write(str(SoLuongVeDich) + "\n")
        USER.write(str(SoLuongHoanDoi) + "\n")
        USER.write(str(SoLuongQuayDau) + "\n")
        USER.write(str(SoLanChoi) + "\n")
        USER.write(str(SoLanHang1) + "\n")
        USER.write(str(SoLanHang2) + "\n")
        USER.write(str(SoLanHang3) + "\n")
        USER.write(str(SoLanHang4) + "\n")
        USER.write(str(SoLanHang5) + "\n")


# Hàm vẽ và bấm nút MainMenu()
def MainMenu():
    global MANHINHCUASO
    global CHIEURONGCUASO, CHIEUDAICUASO

    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    MANHINHCUASO = pygame.display.set_mode((CHIEUDAICUASO, CHIEURONGCUASO))
    BG = pygame.transform.scale(pygame.image.load("BG_MainMenu.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                if 500 < mouse[0] < 865 and 350 < mouse[1] < 405:  # PLAY BUTTON
                    ClickSound.play()
                    return ChonMapVaSetXe()
                if 500 < mouse[0] < 865 and 425 < mouse[1] < 485:  # SHOP BUTTON
                    ClickSound.play()
                    return Shop()
                if 500 < mouse[0] < 865 and 500 < mouse[1] < 555:  # OPTIONS BUTTON
                    ClickSound.play()
                    return Option()
                if 500 < mouse[0] < 865 and 575 < mouse[1] < 625:  # MINIGAME
                    ClickSound.play()
                    return MiniGame()
                if 500 < mouse[0] < 865 and 645 < mouse[1] < 700:  # QUIT BUTTON
                    ClickSound.play()
                    save()
                    pygame.quit()
                    sys.exit()
                if 171 < mouse[0] < 330 and 440 < mouse[1] < 535:
                    ClickSound.play()
                    History()
                if 1050 < mouse[0] < 1225 and 600 < mouse[1] < 700:
                    ClickSound.play()  # LOGOUT BUTTON
                    login()

        MANHINHCUASO.blit(BG, (0, 0))
        font = pygame.font.SysFont('Corbel', 35)
        text = font.render(str(tongTien), True, (255, 255, 255))
        MANHINHCUASO.blit(text, (150, 650))
        pygame.display.update()


# Hàm chọn map, chọn xe các kiểu để vào game
def ChonMapVaSetXe():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    screen_height = 720
    screen_width = 1280
    screen = pygame.display.set_mode([screen_width, screen_height])
    BG = pygame.image.load("BG_Choose.png")
    Map1 = pygame.transform.scale(pygame.image.load("Map1.png"), (156, 104))
    Map2 = pygame.transform.scale(pygame.image.load("Map2.png"), (156, 104))
    Map3 = pygame.transform.scale(pygame.image.load("Map3.png"), (156, 104))
    Map4 = pygame.transform.scale(pygame.image.load("Map4.png"), (156, 104))
    Map5 = pygame.transform.scale(pygame.image.load("Map5.png"), (156, 104))
    xe1 = pygame.transform.scale(pygame.image.load("QuaiXanh.png"), (156, 250))
    xe2 = pygame.transform.scale(pygame.image.load("XeXanhTrai.png"), (145, 93))
    xe3 = pygame.transform.scale(pygame.image.load("MeoDoTrai2.png"), (145, 93))
    xe4 = pygame.transform.scale(pygame.image.load("NguoiCaoBoiPhai.png"), (145, 93))
    xe5 = pygame.transform.scale(pygame.image.load("TeamMinh_1.png"), (145, 93))
    global map
    global xe
    map = 0
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                if 125 <= mouse[1] <= 283 and 30 <= mouse[0] <= 270:
                    ClickSound.play()
                    map = 1
                if 125 <= mouse[1] <= 283 and 300 <= mouse[0] <= 540:
                    ClickSound.play()
                    map = 2
                if 125 <= mouse[1] <= 283 and 565 <= mouse[0] <= 805:
                    ClickSound.play()
                    map = 3
                if 330 <= mouse[1] <= 485 and 152 <= mouse[0] <= 391:
                    ClickSound.play()
                    map = 4
                if 330 <= mouse[1] <= 485 and 482 <= mouse[0] <= 720:
                    ClickSound.play()
                    map = 5
                # ----------------------#

                if 1000 <= mouse[0] <= 1080 and 130 <= mouse[1] <= 165:
                    ClickSound.play()
                    xe = 1
                if 1000 <= mouse[0] <= 1080 and 205 <= mouse[1] <= 245:
                    ClickSound.play()
                    xe = 2
                if 1000 <= mouse[0] <= 1080 and 265 <= mouse[1] <= 325:
                    ClickSound.play()
                    xe = 3
                if 1000 <= mouse[0] <= 1080 and 335 <= mouse[1] <= 400:
                    ClickSound.play()
                    xe = 4
                if 1000 <= mouse[0] <= 1080 and 400 <= mouse[1] <= 465:
                    ClickSound.play()
                    xe = 5
                if 535 <= mouse[0] <= 750 and 555 <= mouse[1] <= 615 and xe != 0 and map != 0:
                    ClickSound.play()
                    return ChonTienCuocVaXeCuoc()
                if 535 <= mouse[0] <= 750 and 635 <= mouse[1] <= 695:
                    ClickSound.play()
                    return MainMenu()
            screen.blit(BG, (0, 0))
            if map == 1:
                screen.blit(Map1, (227, 603))
            if map == 2:
                screen.blit(Map2, (227, 603))
            if map == 3:
                screen.blit(Map3, (227, 603))
            if map == 4:
                screen.blit(Map4, (227, 603))
            if map == 5:
                screen.blit(Map5, (227, 603))
            if xe == 1:
                screen.blit(xe1, (1100, 605))
            if xe == 2:
                screen.blit(xe2, (1100, 605))
            if xe == 3:
                screen.blit(xe3, (1100, 605))
            if xe == 4:
                screen.blit(xe4, (1100, 605))
            if xe == 5:
                screen.blit(xe5, (1100, 605))
            mouse = pygame.mouse.get_pos()
            pygame.display.update()


def ChonTienCuocVaXeCuoc():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    global map
    global xe
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5
    global tienCuoc
    tienCuoc = 0
    global xeCuoc
    screen_height = 720
    screen_width = 1280
    screen = pygame.display.set_mode([screen_width, screen_height])
    Map1 = pygame.transform.scale(pygame.image.load("Map1.png"), (440, 255))
    Map2 = pygame.transform.scale(pygame.image.load("Map2.png"), (440, 250))
    Map3 = pygame.transform.scale(pygame.image.load("Map3.png"), (440, 250))
    Map4 = pygame.transform.scale(pygame.image.load("Map4.png"), (440, 250))
    Map5 = pygame.transform.scale(pygame.image.load("Map5.png"), (440, 250))
    x1, y1 = 733, 194
    x2, y2 = 933, 194
    x3, y3 = 1133, 194
    x4, y4 = 833, 350
    x5, y5 = 1033, 350
    BG = pygame.image.load("BG_Money.png")
    ##font=pygame.font.SysFont('consolas',30)

    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                # chọn tiền cược
                if 162 <= mouse[0] <= 286 and 468 <= mouse[1] <= 530:
                    ClickSound.play()
                    tienCuoc = 10
                elif 313 <= mouse[0] <= 435 and 468 <= mouse[1] <= 530:
                    ClickSound.play()
                    tienCuoc = 20
                elif 460 <= mouse[0] <= 588 and 468 <= mouse[1] <= 530:
                    ClickSound.play()
                    tienCuoc = 50
                elif 162 <= mouse[0] <= 286 and 557 <= mouse[1] <= 615:
                    ClickSound.play()
                    tienCuoc = 100
                elif 313 <= mouse[0] <= 435 and 557 <= mouse[1] <= 615:
                    ClickSound.play()
                    tienCuoc = 500
                elif 460 <= mouse[0] <= 588 and 557 <= mouse[1] <= 615:
                    ClickSound.play()
                    tienCuoc = 9999
                # chọn xe
                elif 715 <= mouse[0] <= 815 and 175 <= mouse[1] <= 245:
                    ClickSound.play()
                    xeCuoc = 1
                elif 915 <= mouse[0] <= 1015 and 175 <= mouse[1] <= 245:
                    ClickSound.play()
                    xeCuoc = 2
                elif 1115 <= mouse[0] <= 1215 and 175 <= mouse[1] <= 245:
                    ClickSound.play()
                    xeCuoc = 3
                elif 830 <= mouse[0] <= 930 and 345 <= mouse[1] <= 405:
                    ClickSound.play()
                    xeCuoc = 4
                elif 1030 <= mouse[0] <= 1130 and 345 <= mouse[1] <= 405:
                    ClickSound.play()
                    xeCuoc = 5
                # button
                elif 1011 <= mouse[0] <= 1218 and 545 <= mouse[1] <= 605:
                    ClickSound.play()
                    return RunGame()
                elif 1011 <= mouse[0] <= 1218 and 625 <= mouse[1] <= 685:
                    ClickSound.play()
                    return ChonMapVaSetXe()
            ##text=pygame.font.render(tienCuoc,True,(0,255,0),(0,0,0))
            screen.blit(BG, (0, 0))
            # vẽ bản đồ
            if map == 1:
                screen.blit(Map1, (138, 101))
            elif map == 2:
                screen.blit(Map2, (138, 101))
            elif map == 3:
                screen.blit(Map3, (138, 101))
            elif map == 4:
                screen.blit(Map4, (138, 101))
            elif map == 5:
                screen.blit(Map5, (138, 101))
            # vẽ xe
            VeXe(xe)
            # vẽ biểu tượng chọn tiền
            if tienCuoc == 10:
                pygame.draw.circle(screen, "RED", (180, 500), 10)
            elif tienCuoc == 20:
                pygame.draw.circle(screen, "RED", (325, 500), 10)
            elif tienCuoc == 50:
                pygame.draw.circle(screen, "RED", (480, 500), 10)
            elif tienCuoc == 100:
                pygame.draw.circle(screen, "RED", (180, 585), 10)
            elif tienCuoc == 500:
                pygame.draw.circle(screen, "RED", (325, 585), 10)
            elif tienCuoc == 9999:
                pygame.draw.circle(screen, "RED", (480, 585), 10)
            # vẽ biểu tượng chọn xe
            if xeCuoc == 1:
                screen.blit(muiTen, (x1, y1 + 20))
            if xeCuoc == 2:
                screen.blit(muiTen, (x2, y2 + 20))
            if xeCuoc == 3:
                screen.blit(muiTen, (x3, y3 + 20))
            if xeCuoc == 4:
                screen.blit(muiTen, (x4, y4 + 20))
            if xeCuoc == 5:
                screen.blit(muiTen, (x5, y5 + 20))
            ##screen.blit(tienCuoc,(345,655))
            font = pygame.font.SysFont('Corbel', 35)
            text = font.render(str(tongTien), True, (255, 255, 255))
            MANHINHCUASO.blit(text, (350, 650))
            mouse = pygame.mouse.get_pos()
            pygame.display.update()


# Hàm vẽ và bấm nút Option
def Option():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    global MANHINHCUASO
    global CHIEURONGCUASO, CHIEUDAICUASO
    BG = pygame.transform.scale(pygame.image.load("BG_Option.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                if 800 <= mouse[0] <= 835 and 280 <= mouse[1] <= 305:  # SOUNDBUTTON
                    ClickSound.play()
                    SoundOnOff()
                # Full Screen
                # Instructions
            if ev.type == MOUSEBUTTONDOWN:
                if 430 <= mouse[0] <= 880 and 440 <= mouse[1] <= 500:
                    ClickSound.play()
                    Instructions()
                # Credits
                if 434 <= mouse[0] <= 885 and 533 <= mouse[1] <= 587:
                    ClickSound.play()
                    Credits()
                if 430 <= mouse[0] <= 880 and 620 <= mouse[1] <= 675:
                    ClickSound.play()
                    MainMenu()
        MANHINHCUASO.blit(BG, [0, 0])
        pygame.display.update()


# Hàm tắt mở âm thanh
def SoundOnOff():
    global SoundOn
    if SoundOn:
        pygame.mixer.music.set_volume(0)
        SoundOn = False
        print("Tat")
    elif not SoundOn:
        pygame.mixer.music.set_volume(0.3)
        SoundOn = True
        print("Bat")


def Instructions():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    global MANHINHCUASO
    global CHIEURONGCUASO, CHIEUDAICUASO
    BG = pygame.transform.scale(pygame.image.load("BG_Instructions.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                if 426 <= mouse[0] <= 880 and 645 <= mouse[1] <= 700:
                    ClickSound.play()
                    Option()
        MANHINHCUASO.blit(BG, [0, 0])
        pygame.display.update()


def Credits():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    global MANHINHCUASO
    global CHIEURONGCUASO, CHIEUDAICUASO
    BG = pygame.transform.scale(pygame.image.load("BG_Credits.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                if 426 <= mouse[0] <= 880 and 645 <= mouse[1] <= 700:
                    ClickSound.play()
                    Option()
        MANHINHCUASO.blit(BG, [0, 0])
        pygame.display.update()


def Shop():
    global SoLuongQuayDau, SoLuongDungLai, SoLuongHoanDoi, SoLuongVeDich
    global tongTien
    MANHINHCUASO = pygame.display.set_mode((CHIEUDAICUASO, CHIEURONGCUASO))
    BG = pygame.transform.scale(pygame.image.load("BG_Shop.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    MuaDo = pygame.mixer.Sound("NhacMuaBua.mp3")
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:  # tương tác với phím
                if event.key == K_ESCAPE:
                    return MainMenu()
            elif event.type == MOUSEBUTTONDOWN:
                if 1036 <= mouse[0] <= 1212 and 642 <= mouse[1] <= 691:
                    return MainMenu()
                elif 12 <= mouse[0] <= 708 and 20 <= mouse[1] <= 102:
                    MuaDo.play()
                    SoLuongDungLai = SoLuongDungLai + 1
                    tongTien = tongTien - 50
                elif 12 <= mouse[0] <= 708 and 120 < mouse[1] <= 202:
                    MuaDo.play()
                    SoLuongVeDich = SoLuongVeDich + 1
                    tongTien = tongTien - 100
                elif 12 <= mouse[0] <= 705 and 220 <= mouse[1] <= 302:
                    MuaDo.play()
                    SoLuongHoanDoi = SoLuongHoanDoi + 1
                    tongTien = tongTien - 250
                elif 12 <= mouse[0] <= 705 and 320 <= mouse[1] <= 402:
                    MuaDo.play()
                    SoLuongQuayDau = SoLuongQuayDau + 1
                    tongTien = tongTien - 400

            MANHINHCUASO.blit(BG, (0, 0))
            font = pygame.font.SysFont('Corbel', 35)
            text = font.render(str(tongTien), True, (255, 255, 255))
            textBuaDungLai = font.render(str(SoLuongDungLai), True, (255, 255, 255))
            textBuaVeDich = font.render(str(SoLuongVeDich), True, (255, 255, 255))
            textBuaHoanDoi = font.render(str(SoLuongHoanDoi), True, (255, 255, 255))
            textBuaQuayDau = font.render(str(SoLuongQuayDau), True, (255, 255, 255))
            MANHINHCUASO.blit(text, (150, 650))
            MANHINHCUASO.blit(textBuaDungLai, (46, 46))
            MANHINHCUASO.blit(textBuaVeDich, (46, 146))
            MANHINHCUASO.blit(textBuaHoanDoi, (46, 246))
            MANHINHCUASO.blit(textBuaQuayDau, (46, 346))
            pygame.display.update()


def History():
    global SoLanChoi, SoLanHang1, SoLanHang2, SoLanHang3, SoLanHang4, SoLanHang5
    global CHIEURONGCUASO, CHIEUDAICUASO
    BG = pygame.transform.scale(pygame.image.load("BG_History.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    MANHINHCUASO.blit(BG, (0, 0))
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render(str(SoLanChoi), True, (255, 255, 255))
    text1 = font.render(str(SoLanHang1), True, (255, 255, 255))
    text2 = font.render(str(SoLanHang2), True, (255, 255, 255))
    text3 = font.render(str(SoLanHang3), True, (255, 255, 255))
    text4 = font.render(str(SoLanHang4), True, (255, 255, 255))
    text5 = font.render(str(SoLanHang5), True, (255, 255, 255))
    MANHINHCUASO.blit(text, (600, 260))
    MANHINHCUASO.blit(text1, (285, 386))
    MANHINHCUASO.blit(text2, (422, 386))
    MANHINHCUASO.blit(text3, (571, 386))
    MANHINHCUASO.blit(text4, (706, 386))
    MANHINHCUASO.blit(text5, (855, 386))
    pygame.display.update()
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                if 436 < mouse[0] < 885 and 623 < mouse[1] < 675:
                    MainMenu()


def ScreenScore():
    ClickSound = pygame.mixer.Sound("NhacClick.mp3")
    global huong1, huong2, huong3, huong4, huong5
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5
    global xe
    global MANHINHCUASO
    global CHIEURONGCUASO, CHIEUDAICUASO
    global SoLanChoi
    SoLanChoi = SoLanChoi + 1
    BG = pygame.transform.scale(pygame.image.load("BG_ScreenScore.png"), (CHIEUDAICUASO, CHIEURONGCUASO))
    pygame.mixer.music.pause()
    pygame.mixer.music.load("NhacChienThang.mp3")
    pygame.mixer.music.play()
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == MOUSEBUTTONDOWN:
                if 534 <= mouse[0] <= 790 and 640 <= mouse[1] <= 685:
                    ClickSound.play()
                    pygame.mixer.music.pause()
                    RunGame()
                if 1044 <= mouse[0] <= 1233 and 640 <= mouse[1] <= 690:
                    ClickSound.play()
                    pygame.mixer.music.pause()
                    pygame.mixer.music.load("NhacNen.mp3")
                    pygame.mixer.music.play()
                    MainMenu()
        MANHINHCUASO.blit(BG, [0, 0])
        XepHangXe()
        VeXe(xe)
        VeDanhDauXe()
        font = pygame.font.SysFont('Corbel', 35)
        text = font.render(str(tongTien), True, (255, 255, 255))
        MANHINHCUASO.blit(text, (150, 650))
        pygame.display.update()


def XepHangXe():
    global x1, y1
    if huong1 == 1:
        x1 = 490
        y1 = 175
    elif huong1 == 2:
        x1 = 490
        y1 = 300
    elif huong1 == 3:
        x1 = 490
        y1 = 420
    elif huong1 == 4:
        x1 = 960
        y1 = 229
    elif huong1 == 5:
        x1 = 960
        y1 = 369

    global x2, y2
    if huong2 == 1:
        x2 = 490
        y2 = 175
    elif huong2 == 2:
        x2 = 490
        y2 = 300
    elif huong2 == 3:
        x2 = 490
        y2 = 420
    elif huong2 == 4:
        x2 = 960
        y2 = 229
    elif huong2 == 5:
        x2 = 960
        y2 = 369

    global x3, y3
    if huong3 == 1:
        x3 = 490
        y3 = 175
    elif huong3 == 2:
        x3 = 490
        y3 = 300
    elif huong3 == 3:
        x3 = 490
        y3 = 420
    elif huong3 == 4:
        x3 = 960
        y3 = 229
    elif huong3 == 5:
        x3 = 960
        y3 = 369

    global x4, y4
    if huong4 == 1:
        x4 = 490
        y4 = 175
    elif huong4 == 2:
        x4 = 490
        y4 = 300
    elif huong4 == 3:
        x4 = 490
        y4 = 420
    elif huong4 == 4:
        x4 = 960
        y4 = 229
    elif huong4 == 5:
        x4 = 960
        y4 = 369

    global x5, y5
    if huong5 == 1:
        x5 = 490
        y5 = 175
    elif huong5 == 2:
        x5 = 490
        y5 = 300
    elif huong5 == 3:
        x5 = 490
        y5 = 420
    elif huong5 == 4:
        x5 = 960
        y5 = 229
    elif huong5 == 5:
        x5 = 960
        y5 = 369


# -----------------------------GameZone---------------------------------#
########################################################################
# Hàm game chính
def RunGame():
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5
    global huong1, huong2, huong3, huong4, huong5
    global map
    global xe
    global xeCuoc
    global tienCuoc
    global soDemXepHang
    soDemXepHang = 1
    global tongTien
    speed = 50
    pygame.mixer.music.pause()



    # Xác định vị trí ban đầu
    if map == 1:
        pygame.mixer.music.load("map1.mp3")
        pygame.mixer.music.play()
        huong1 = huong2 = huong3 = huong4 = huong5 = 'phai'
        x1 = x2 = x3 = x4 = x5 = 35
        y1 = y2 = y3 = y4 = y5 = 60
    elif map == 2:
        pygame.mixer.music.load("map2.mp3")
        pygame.mixer.music.play()
        huong1 = huong2 = huong3 = huong4 = huong5 = 'phai'
        x1 = x2 = x3 = x4 = x5 = 65
        y1 = y2 = y3 = y4 = y5 = 105
    elif map == 3:
        pygame.mixer.music.load("map3.mp3")
        pygame.mixer.music.play()
        huong1 = huong2 = huong3 = huong4 = huong5 = 'phai'
        x1 = x2 = x3 = x4 = x5 = 0
        y1 = y2 = y3 = y4 = y5 = 250
    elif map == 4:
        pygame.mixer.music.load("map4.mp3")
        pygame.mixer.music.play()
        huong1 = huong2 = huong3 = huong4 = huong5 = 'phai'
        x1 = x2 = x3 = x4 = x5 = 40
        y1 = y2 = y3 = y4 = y5 = 155
    elif map == 5:
        pygame.mixer.music.load("map5.mp3")
        pygame.mixer.music.play()
        huong1 = huong2 = huong3 = huong4 = huong5 = 'phai'
        x1 = x2 = x3 = x4 = x5 = 35
        y1 = y2 = y3 = y4 = y5 = 170

    while True:  # Chạy tẹt bô
        mouse = pygame.mouse.get_pos()  # hàm lấy toạ độ chuột
        for event in pygame.event.get():  # Event tương tác khi xe chạy
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:  # tương tác với phím
                if event.key == K_SPACE:
                    if speed == 50:
                        speed = 1
                    else:
                        speed = 50
                elif event.key == K_1:
                    Spell('Stop')
                elif event.key == K_2:
                    Spell('VeDich')
                elif event.key == K_3:
                    Spell('HoanDoi')
                elif event.key == K_4:
                    Spell('QuayDau')

        # Gọi hàm chuyển động xe (Hàm này xác định vị trí và hướng dịch chuyển của xe)
        ChuyenDongXe()
        # Check tới đích
        XepHang()
        # Hàm check kết thúc đua khi cả 5 xe tới đích:
        if (soDemXepHang == 6):
            soDemXepHang = 1
            tongTien = TienSauCuoc(tienCuoc, xeCuoc)
            print(tongTien)
            ScreenScore()
        # Hàm vẽ xe và map (Hàm này vẽ map và xe theo toạ độ rút trích từ hàm ChuyenDongXe())
        QuayDauXe()
        VeMap(map)
        VeXe(xe)
        VeDanhDauXe()
        VeSoLuongBua()
        pygame.display.flip()
        # time (Hàm này điều chỉnh tốc độ của vòng lặp)
        pygame.time.delay(speed)

        # phần test thông số (Hàm này để check toạ độ xe 1)
        print(x1, y1)
        print(speed)


# Hàm này đảm nhận việc cập nhật toạ độ của các xe
def ChuyenDongXe():
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5
    global huong1, huong2, huong3, huong4, huong5
    SpellStop()
    huong1 = CheckCua(x1, y1, huong1)
    huong2 = CheckCua(x2, y2, huong2)
    huong3 = CheckCua(x3, y3, huong3)
    huong4 = CheckCua(x4, y4, huong4)
    huong5 = CheckCua(x5, y5, huong5)

    x1, y1 = TocDoX(x1, huong1), TocDoY(y1, huong1)
    x2, y2 = TocDoX(x2, huong2), TocDoY(y2, huong2)
    x3, y3 = TocDoX(x3, huong3), TocDoY(y3, huong3)
    x4, y4 = TocDoX(x4, huong4), TocDoY(y4, huong4)
    x5, y5 = TocDoX(x5, huong5), TocDoY(y5, huong5)


# Hàm này xác định vị trí mà hướng xe dịch chuyển sẽ thay đổi (cua)
def CheckCua(x, y, huong):
    global map
    # check map
    if map == 1:
        if 55 >= x >= 15 and 80 >= y >= 40:
            return 'phai'
        if 1220 <= x <= 1250 and 60 <= y <= 90:
            return 'xuong'
        elif 1220 <= x <= 1250 and 620 <= y <= 650:
            return 'trai'
        elif 935 <= x <= 965 and 620 <= y <= 650:
            return 'len'
        elif 935 <= x <= 965 and 145 <= y <= 175:
            return 'trai'
        elif 55 <= x <= 85 and 145 <= y <= 175:
            return 'xuong'
        elif 55 <= x <= 85 and 625 <= y <= 655:
            return 'phai'
        elif 740 <= x <= 770 and 625 <= y <= 655:
            return 'len'
        elif 740 <= x <= 770 and 335 <= y <= 365:
            return 'trai'
        elif 310 <= x <= 340 and 335 <= y <= 365 and huong == 'trai':
            return 'finish'
        return huong
    elif map == 2:
        if x == 65 and y == 105:
            return 'phai'
        elif 615 >= x >= 585 and 115 >= y >= 85:
            return 'xuong'
        elif 615 >= x >= 585 and 615 >= y >= 585:
            return 'trai'
        elif 110 >= x >= 80 and 615 >= y >= 585:
            return 'len'
        elif 110 >= x >= 80 and 280 >= y >= 250:
            return 'phai'
        elif 1220 >= x >= 1190 and 280 >= y >= 250:
            return 'xuong'
        elif 1210 >= x >= 1190 and 610 >= y >= 580:
            return 'trai'
        elif 700 >= x >= 670 and 610 >= y >= 580:
            return 'len'
        elif 700 >= x >= 670 and 115 >= y >= 85:
            return 'phai'
        elif 1225 >= x >= 1195 and 115 >= y >= 85 and huong == 'phai':
            return 'finish'
        return huong;
    elif map == 3:  # giả sử map là map cho sẵn
        if x == 0 and y == 250:
            return 'phai'
        if (1220 <= x <= 1250 and 235 <= y <= 265):
            return 'xuong'
        elif (1220 <= x <= 1250 and 655 <= y <= 685):
            return 'trai'  # trái
        elif (925 <= x <= 955 and 655 <= y <= 685):
            return 'len'  # lêns
        elif (925 <= x <= 955 and 20 <= y <= 50):
            return 'trai'  # trái
        elif (300 <= x <= 330 and 20 <= y <= 50):
            return 'xuong'  # xuống
        elif (300 <= x <= 330 and 660 <= y <= 690):
            return 'phai'  # phải
        elif 820 <= x <= 850 and 660 <= y <= 690:
            return 'len'  # lên
        elif (820 <= x <= 850 and 370 <= y <= 400):
            return 'trai'  # trái
        elif (70 <= x <= 100 and 370 <= y <= 400):
            return 'xuong'  # xuống
        elif (70 <= x <= 100 and 650 <= y <= 680 and huong == 'xuong'):
            return 'finish'
        return huong
    elif map == 4:
        if 55 >= x >= 25 and 170 >= y >= 140:
            return 'phai'
        elif 730 >= x >= 700 and 170 >= y >= 140:
            return 'len'
        elif 730 >= x >= 700 and 50 >= y >= 20:
            return 'phai'
        elif 1245 >= x >= 1215 and 50 >= y >= 20:
            return 'xuong'
        elif 1245 >= x >= 1215 and 675 >= y >= 645:
            return 'trai'
        elif 1015 >= x >= 985 and 675 >= y >= 645:
            return 'len'
        elif 1015 >= x >= 985 and 185 >= y >= 155:
            return 'trai'
        elif 785 >= x >= 755 and 185 >= y >= 155:
            return 'xuong'
        elif 785 >= x >= 755 and 695 >= y >= 665:
            return 'trai'
        elif 560 >= x >= 530 and 695 >= y >= 665:
            return 'len'
        elif 560 >= x >= 530 and 455 >= y >= 425:
            return 'trai'
        elif 155 >= x >= 125 and 455 >= y >= 425:
            return 'len'
        elif 155 >= x >= 125 and 335 >= y >= 300:
            return 'trai'
        elif 50 >= x >= 20 and 335 >= y >= 300 and huong == 'trai':
            return 'finish'
        return huong

    elif map == 5:
        if 50 >= x >= 20 and 190 >= y >= 160:
            return 'phai'
        elif 645 >= x >= 615 and 190 >= y >= 160:
            return 'len'
        elif 645 >= x >= 615 and 40 >= y >= 10:
            return 'phai'
        elif 1250 >= x >= 1220 and 40 >= y >= 10:
            return 'xuong'
        elif 1250 >= x >= 1220 and 690 >= y >= 660:
            return 'trai'
        elif 155 >= x >= 125 and 690 >= y >= 660:
            return 'len'
        elif 155 >= x >= 125 and 295 >= y >= 265:
            return 'phai'
        elif 615 >= x >= 585 and 295 >= y >= 265:
            return 'xuong'
        elif 615 >= x >= 585 and 425 >= y >= 395:
            return 'phai'
        elif 1090 >= x >= 1060 and 425 >= y >= 395:
            return 'len'
        elif 1090 >= x >= 1060 and 200 >= y >= 170:
            return 'trai'
        elif 860 >= x >= 830 and 200 >= y >= 170 and huong == 'trai':
            return 'finish'
        return huong


# Hàm này cập nhật toạ độ X
def TocDoX(x, huong):
    if huong == 'phai':
        return x + random.randrange(-7, 25)
    elif huong == 'trai':
        return x - random.randrange(-7, 25)
    elif huong == 'stop':
        return x
    elif huong == 'finish':
        return x

    return x


# Hàm này cập nhật toạ độ Y
def TocDoY(y, huong):
    if huong == 'xuong':
        return y + random.randrange(-7, 25)
    elif huong == 'len':
        return y - random.randrange(-7, 25)
    elif huong == 'stop':
        return y
    elif huong == 'finish':
        return y
    return y


# ----------------------------Vẽ---------------------------#
def VeMap(map):
    global MAP1, MAP3, MANHINHCUASO
    if map == 1:
        MANHINHCUASO.blit(MAP1, (0, 0))
    elif map == 2:
        MANHINHCUASO.blit(MAP2, (0, 0))
    elif map == 3:
        MANHINHCUASO.blit(MAP3, (0, 0))
    elif map == 4:
        MANHINHCUASO.blit(MAP4, (0, 0))
    elif map == 5:
        MANHINHCUASO.blit(MAP5, (0, 0))


def QuayDauXe():
    global xe2_xeDo, xe2_xeBlue, xe2_xeHong, xe2_xeVang, xe2_xeXanh
    global xe3_meoDen, xe3_meoDo, xe3_meoVang, xe3_meoXam, xe3_meoXanh
    global xe4_CaoBoi, xe4_CaoBoiGai, xe4_Ninja, xe4_NinjaGai, xe4_Robot
    global xe5_Kiet, xe5_Khang, xe5_Loc, xe5_Minh, xe5_Long
    global meoXanh, meoVang, meoXam, meoDo, meoDen
    global NguoiCaoBoi, NguoiCaoBoiGai, NguoiNinja, NguoiNinjaGai, NguoiRobot
    global TeamKiet, TeamKhang, TeamLoc, TeamMinh, TeamLong
    if xe == 2:
        if huong1 == 'phai':
            xe2_xeDo = pygame.image.load('XeDoPhai.png')
        elif huong1 == 'trai':
            xe2_xeDo = pygame.image.load('XeDoTrai.png')
        elif huong1 == 'len':
            xe2_xeDo = pygame.image.load('XeDoLen.png')
        elif huong1 == 'xuong':
            xe2_xeDo = pygame.image.load('XeDoXuong.png')

        if huong2 == 'phai':
            xe2_xeBlue = pygame.image.load('XeBluePhai.png')
        elif huong2 == 'trai':
            xe2_xeBlue = pygame.image.load('XeBlueTrai.png')
        elif huong2 == 'len':
            xe2_xeBlue = pygame.image.load('XeBlueLen.png')
        elif huong2 == 'xuong':
            xe2_xeBlue = pygame.image.load('XeBlueXuong.png')

        if huong3 == 'phai':
            xe2_xeHong = pygame.image.load('XeHongPhai.png')
        elif huong3 == 'trai':
            xe2_xeHong = pygame.image.load('XeHongTrai.png')
        elif huong3 == 'len':
            xe2_xeHong = pygame.image.load('XeHongLen.png')
        elif huong3 == 'xuong':
            xe2_xeHong = pygame.image.load('XeHongXuong.png')

        if huong4 == 'phai':
            xe2_xeVang = pygame.image.load('XeVangPhai.png')
        elif huong4 == 'trai':
            xe2_xeVang = pygame.image.load('XeVangTrai.png')
        elif huong4 == 'len':
            xe2_xeVang = pygame.image.load('XeVangLen.png')
        elif huong4 == 'xuong':
            xe2_xeVang = pygame.image.load('XeVangXuong.png')

        if huong5 == 'phai':
            xe2_xeXanh = pygame.image.load('XeXanhPhai.png')
        elif huong5 == 'trai':
            xe2_xeXanh = pygame.image.load('XeXanhTrai.png')
        elif huong5 == 'len':
            xe2_xeXanh = pygame.image.load('XeXanhLen.png')
        elif huong5 == 'xuong':
            xe2_xeXanh = pygame.image.load('XeXanhXuong.png')

    elif xe == 3:
        if huong1 == 'phai':
            if meoDen == 1:
                xe3_meoDen = pygame.image.load('MeoDenPhai.png')
                meoDen = 2
            else:
                xe3_meoDen = pygame.image.load('MeoDenPhai2.png')
                meoDen = 1
        elif huong1 == 'trai':
            if meoDen == 1:
                xe3_meoDen = pygame.image.load('MeoDenTrai.png')
                meoDen = 2
            else:
                xe3_meoDen = pygame.image.load('MeoDenTrai2.png')
                meoDen = 1
        elif huong1 == 'len':
            if meoDen == 1:
                xe3_meoDen = pygame.image.load('MeoDenPhai.png')
                meoDen = 2
            else:
                xe3_meoDen = pygame.image.load('MeoDenPhai2.png')
                meoDen = 1
        elif huong1 == 'Xuong':
            if meoDen == 1:
                xe3_meoDen = pygame.image.load('MeoDenTrai.png')
                meoDen = 2
            else:
                xe3_meoDen = pygame.image.load('MeoDenTrai2.png')
                meoDen = 1

        if huong2 == 'phai':
            if meoDo == 1:
                xe3_meoDo = pygame.image.load('MeoDoPhai.png')
                meoDo = 2
            else:
                xe3_meoDo = pygame.image.load('MeoDoPhai2.png')
                meoDo = 1
        elif huong2 == 'trai':
            if meoDo == 1:
                xe3_meoDo = pygame.image.load('MeoDoTrai.png')
                meoDo = 2
            else:
                xe3_meoDo = pygame.image.load('MeoDoTrai2.png')
                meoDo = 1
        elif huong2 == 'len':
            if meoDo == 1:
                xe3_meoDo = pygame.image.load('MeoDoPhai.png')
                meoDo = 2
            else:
                xe3_meoDo = pygame.image.load('MeoDoPhai2.png')
                meoDo = 1
        elif huong2 == 'xuong':
            if meoDo == 1:
                xe3_meoDo = pygame.image.load('MeoDoTrai.png')
                meoDo = 2
            else:
                xe3_meoDo = pygame.image.load('MeoDoTrai2.png')
                meoDo = 1

        if huong3 == 'phai':
            if meoVang == 1:
                xe3_meoVang = pygame.image.load('MeoVangPhai.png')
                meoVang = 2
            else:
                xe3_meoVang = pygame.image.load('MeoVangPhai2.png')
                meoVang = 1
        elif huong3 == 'trai':
            if meoVang == 1:
                xe3_meoVang = pygame.image.load('MeoVangTrai.png')
                meoVang = 2
            else:
                xe3_meoVang = pygame.image.load('MeoVangTrai2.png')
                meoVang = 1
        elif huong3 == 'len':
            if meoVang == 1:
                xe3_meoVang = pygame.image.load('MeoVangPhai.png')
                meoVang = 2
            else:
                xe3_meoVang = pygame.image.load('MeoVangPhai2.png')
                meoVang = 1
        elif huong3 == 'xuong':
            if meoVang == 1:
                xe3_meoVang = pygame.image.load('MeoVangTrai.png')
                meoVang = 2
            else:
                xe3_meoVang = pygame.image.load('MeoVangTrai2.png')
                meoVang = 1

        if huong4 == 'phai':
            if meoXam == 1:
                xe3_meoXam = pygame.image.load('MeoXamPhai.png')
                meoXam = 2
            else:
                xe3_meoXam = pygame.image.load('MeoXamPhai2.png')
                meoXam = 1
        elif huong4 == 'trai':
            if meoXam == 1:
                xe3_meoXam = pygame.image.load('MeoXamTrai.png')
                meoXam = 2
            else:
                xe3_meoXam = pygame.image.load('MeoXamTrai2.png')
                meoXam = 1
        elif huong4 == 'len':
            if meoXam == 1:
                xe3_meoXam = pygame.image.load('MeoXamPhai.png')
                meoXam = 2
            else:
                xe3_meoXam = pygame.image.load('MeoXamPhai2.png')
                meoXam = 1
        elif huong4 == 'xuong':
            if meoXam == 1:
                xe3_meoXam = pygame.image.load('MeoXamTrai.png')
                meoXam = 2
            else:
                xe3_meoXam = pygame.image.load('MeoXamTrai2.png')
                meoXam = 1

        if huong5 == 'phai':
            if meoXanh == 1:
                xe3_meoXanh = pygame.image.load('MeoXanhPhai.png')
                meoXanh = 2
            elif meoXanh == 2:
                xe3_meoXanh = pygame.image.load('MeoXanhPhai2.png')
                meoXanh = 1
        elif huong5 == 'trai':
            if meoXanh == 1:
                xe3_meoXanh = pygame.image.load('MeoXanhTrai.png')
                meoXanh = 2
            elif meoXanh == 2:
                xe3_meoXanh = pygame.image.load('MeoXanhTrai2.png')
                meoXanh = 1
        elif huong5 == 'len':
            if meoXanh == 1:
                xe3_meoXanh = pygame.image.load('MeoXanhPhai.png')
                meoXanh = 2
            elif meoXanh == 2:
                xe3_meoXanh = pygame.image.load('MeoXanhPhai2.png')
                meoXanh = 1
        elif huong5 == 'xuong':
            if meoXanh == 1:
                xe3_meoXanh = pygame.image.load('MeoXanhTrai.png')
                meoXanh = 2
            elif meoXanh == 2:
                xe3_meoXanh = pygame.image.load('MeoXanhTrai2.png')
                meoXanh = 1
    elif xe == 4:
        if huong1 == 'phai':
            if meoDen == 1:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiPhai.png')
                NguoiCaoBoi = 2
            else:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiPhai2.png')
                NguoiCaoBoi = 1
        elif huong1 == 'trai':
            if NguoiCaoBoi == 1:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiTrai.png')
                NguoiCaoBoi = 2
            else:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiTrai2.png')
                NguoiCaoBoi = 1
        elif huong1 == 'len':
            if meoDen == 1:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiPhai.png')
                NguoiCaoBoi = 2
            else:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiPhai2.png')
                NguoiCaoBoi = 1
        elif huong1 == 'Xuong':
            if NguoiCaoBoi == 1:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiTrai.png')
                NguoiCaoBoi = 2
            else:
                xe4_CaoBoi = pygame.image.load('NguoiCaoBoiTrai2.png')
                NguoiCaoBoi = 1

        if huong2 == 'phai':
            if NguoiCaoBoiGai == 1:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiPhai.png')
                NguoiCaoBoiGai = 2
            else:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiGaiPhai2.png')
                NguoiCaoBoiGai = 1
        elif huong2 == 'trai':
            if NguoiCaoBoiGai == 1:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiGaiTrai.png')
                meoDo = 2
            else:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiGaiTrai2.png')
                NguoiCaoBoiGai = 1
        elif huong2 == 'len':
            if NguoiCaoBoiGai == 1:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiPhai.png')
                NguoiCaoBoiGai = 2
            else:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiGaiPhai2.png')
                NguoiCaoBoiGai = 1
        elif huong2 == 'xuong':
            if NguoiCaoBoiGai == 1:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiGaiTrai.png')
                meoDo = 2
            else:
                xe4_CaoBoiGai = pygame.image.load('NguoiCaoBoiGaiTrai2.png')
                NguoiCaoBoiGai = 1

        if huong3 == 'phai':
            if NguoiNinja == 1:
                xe4_Ninja = pygame.image.load('NguoiNinjaPhai.png')
                NguoiNinja = 2
            else:
                xe4_Ninja = pygame.image.load('NguoiNinjaPhai2.png')
                NguoiNinja = 1
        elif huong3 == 'trai':
            if NguoiNinja == 1:
                xe4_Ninja = pygame.image.load('NguoiNinjaTrai.png')
                NguoiNinja = 2
            else:
                xe4_Ninja = pygame.image.load('NguoiNinjaTrai2.png')
                NguoiNinja = 1
        elif huong3 == 'len':
            if NguoiNinja == 1:
                xe4_Ninja = pygame.image.load('NguoiNinjaPhai.png')
                NguoiNinja = 2
            else:
                xe4_Ninja = pygame.image.load('NguoiNinjaPhai2.png')
                NguoiNinja = 1
        elif huong3 == 'xuong':
            if NguoiNinja == 1:
                xe4_Ninja = pygame.image.load('NguoiNinjaTrai.png')
                NguoiNinja = 2
            else:
                xe4_Ninja = pygame.image.load('NguoiNinjaTrai2.png')
                NguoiNinja = 1

        if huong4 == 'phai':
            if NguoiNinjaGai == 1:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiPhai.png')
                NguoiNinjaGai = 2
            else:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiPhai2.png')
                NguoiNinjaGai = 1
        elif huong4 == 'trai':
            if NguoiNinjaGai == 1:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiTrai.png')
                NguoiNinjaGai = 2
            else:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiTrai2.png')
                NguoiNinjaGai = 1
        elif huong4 == 'len':
            if NguoiNinjaGai == 1:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiPhai.png')
                NguoiNinjaGai = 2
            else:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiPhai2.png')
                NguoiNinjaGai = 1
        elif huong4 == 'xuong':
            if NguoiNinjaGai == 1:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiTrai.png')
                NguoiNinjaGai = 2
            else:
                xe4_NinjaGai = pygame.image.load('NguoiNinjaGaiTrai2.png')
                NguoiNinjaGai = 1

        if huong5 == 'phai':
            if NguoiRobot == 1:
                xe4_Robot = pygame.image.load('NguoiRobotPhai.png')
                NguoiRobot = 2
            elif NguoiRobot == 2:
                xe4_Robot = pygame.image.load('NguoiRobotPhai2.png')
                NguoiRobot = 1
        elif huong5 == 'trai':
            if NguoiRobot == 1:
                xe4_Robot = pygame.image.load('NguoiRobotTrai.png')
                NguoiRobot = 2
            elif NguoiRobot == 2:
                xe4_Robot = pygame.image.load('NguoiRobotTrai2.png')
                NguoiRobot = 1
        elif huong5 == 'len':
            if NguoiRobot == 1:
                xe4_Robot = pygame.image.load('NguoiRobotPhai.png')
                NguoiRobot = 2
            elif NguoiRobot == 2:
                xe4_Robot = pygame.image.load('NguoiRobotPhai2.png')
                NguoiRobot = 1
        elif huong5 == 'xuong':
            if NguoiRobot == 1:
                xe4_Robot = pygame.image.load('NguoiRobotTrai.png')
                NguoiRobot = 2
            elif NguoiRobot == 2:
                xe4_Robot = pygame.image.load('NguoiRobotTrai2.png')
                NguoiRobot = 1
    # xe5
    elif xe == 5:
        if huong1 == 'phai':
            if TeamKiet == 1:
                xe5_Kiet = pygame.image.load('TeamKiet_1.png')
                TeamKiet = 2
            else:
                xe5_Kiet = pygame.image.load('TeamKiet_2.png')
                TeamKiet = 1
        elif huong1 == 'trai':
            if TeamKiet == 1:
                xe5_Kiet = pygame.image.load('TeamKiet_1T.png')
                TeamKiet = 2
            else:
                xe3_meoDen = pygame.image.load('TeamKiet_2T.png')
                TeamKiet = 1
        elif huong1 == 'len':
            if TeamKiet == 1:
                xe5_Kiet = pygame.image.load('TeamKiet_1.png')
                TeamKiet = 2
            else:
                xe5_Kiet = pygame.image.load('TeamKiet_2.png')
                TeamKiet = 1
        elif huong1 == 'Xuong':
            if TeamKiet == 1:
                xe5_Kiet = pygame.image.load('TeamKiet_1T.png')
                TeamKiet = 2
            else:
                xe3_meoDen = pygame.image.load('TeamKiet_2T.png')
                TeamKiet = 1

        if huong2 == 'phai':
            if TeamKhang == 1:
                xe5_Khang = pygame.image.load('TeamKR_1.png')
                TeamKhang = 2
            else:
                xe5_Khang = pygame.image.load('TeamKR_2.png')
                TeamKhang = 1
        elif huong2 == 'trai':
            if TeamKhang == 1:
                xe5_Khang = pygame.image.load('TeamKR_1T.png')
                TeamKhang = 2
            else:
                xe5_Khang = pygame.image.load('TeamKR_2T.png')
                TeamKhang = 1
        elif huong2 == 'len':
            if TeamKhang == 1:
                xe5_Khang = pygame.image.load('TeamKR_1.png')
                TeamKhang = 2
            else:
                xe5_Khang = pygame.image.load('TeamKR_2.png')
                TeamKhang = 1
        elif huong2 == 'xuong':
            if TeamKhang == 1:
                xe5_Khang = pygame.image.load('TeamKR_1T.png')
                TeamKhang = 2
            else:
                xe5_Khang = pygame.image.load('TeamKR_2T.png')
                TeamKhang = 1

        if huong3 == 'phai':
            if TeamLoc == 1:
                xe5_Loc = pygame.image.load('TeamLoc_1.png')
                TeamLoc = 2
            else:
                xe5_Loc = pygame.image.load('TeamLoc_2.png')
                TeamLoc = 1
        elif huong3 == 'trai':
            if TeamLoc == 1:
                xe5_Loc = pygame.image.load('TeamLoc_1T.png')
                TeamLoc = 2
            else:
                xe5_Loc = pygame.image.load('TeamLoc_2T.png')
                TeamLoc = 1
        elif huong3 == 'len':
            if TeamLoc == 1:
                xe5_Loc = pygame.image.load('TeamLoc_1.png')
                TeamLoc = 2
            else:
                xe5_Loc = pygame.image.load('TeamLoc_2.png')
                TeamLoc = 1
        elif huong3 == 'xuong':
            if TeamLoc == 1:
                xe5_Loc = pygame.image.load('TeamLoc_1T.png')
                TeamLoc = 2
            else:
                xe5_Loc = pygame.image.load('TeamLoc_2T.png')
                TeamLoc = 1

        if huong4 == 'phai':
            if TeamMinh == 1:
                xe5_Minh = pygame.image.load('TeamMinh_1.png')
                TeamMinh = 2
            else:
                xe5_Minh = pygame.image.load('TeamMinh_2.png')
                TeamMinh = 1
        elif huong4 == 'trai':
            if TeamMinh == 1:
                xe5_Minh = pygame.image.load('TeamMinh_1T.png')
                TeamMinh = 2
            else:
                xe5_Minh = pygame.image.load('TeamMinh_2T.png')
                TeamMinh = 2
        elif huong4 == 'len':
            if TeamMinh == 1:
                xe5_Minh = pygame.image.load('TeamMinh_1.png')
                TeamMinh = 2
            else:
                xe5_Minh = pygame.image.load('TeamMinh_2.png')
                TeamMinh = 1

        elif huong4 == 'xuong':
            if TeamMinh == 1:
                xe5_Minh = pygame.image.load('TeamMinh_1T.png')
                TeamMinh = 2
            else:
                xe5_Minh = pygame.image.load('TeamMinh_2T.png')
                TeamMinh = 2

        if huong5 == 'phai':
            if TeamLong == 1:
                xe5_Long = pygame.image.load('TeamLong_1.png')
                TeamLong = 2
            elif TeamLong == 2:
                xe5_Long = pygame.image.load('TeamLong_2.png')
                TeamLong = 1
        elif huong5 == 'trai':
            if TeamLong == 1:
                xe5_Long = pygame.image.load('TeamLong_1T.png')
                TeamLong = 2
            elif TeamLong == 2:
                xe5_Long = pygame.image.load('TeamLong_2T.png')
                TeamLong = 1
        elif huong5 == 'len':
            if TeamLong == 1:
                xe5_Long = pygame.image.load('TeamLong_1.png')
                TeamLong = 2
            elif TeamLong == 2:
                xe5_Long = pygame.image.load('TeamLong_2.png')
                TeamLong = 1
        elif huong5 == 'xuong':
            if TeamLong == 1:
                xe5_Long = pygame.image.load('TeamLong_1T.png')
                TeamLong = 2
            elif TeamLong == 2:
                xe5_Long = pygame.image.load('TeamLong_2T.png')
                TeamLong = 1


def VeXe(xe):
    if xe == 1:
        MANHINHCUASO.blit(xe1_quaiXanh, (x1, y1))
        MANHINHCUASO.blit(xe1_quaiDen, (x2, y2))
        MANHINHCUASO.blit(xe1_quaiDo, (x3, y3))
        MANHINHCUASO.blit(xe1_quaiBlue, (x4, y4))
        MANHINHCUASO.blit(xe1_quaiHong, (x5, y5))
    elif xe == 2:
        MANHINHCUASO.blit(xe2_xeDo, (x1, y1))
        MANHINHCUASO.blit(xe2_xeBlue, (x2, y2))
        MANHINHCUASO.blit(xe2_xeHong, (x3, y3))
        MANHINHCUASO.blit(xe2_xeVang, (x4, y4))
        MANHINHCUASO.blit(xe2_xeXanh, (x5, y5))
    elif xe == 3:
        MANHINHCUASO.blit(xe3_meoDen, (x1 - 20, y1 - 20))
        MANHINHCUASO.blit(xe3_meoDo, (x2 - 20, y2 - 20))
        MANHINHCUASO.blit(xe3_meoVang, (x3 - 20, y3 - 20))
        MANHINHCUASO.blit(xe3_meoXam, (x4 - 20, y4 - 20))
        MANHINHCUASO.blit(xe3_meoXanh, (x5 - 20, y5 - 20))
    elif xe == 4:
        MANHINHCUASO.blit(xe4_CaoBoi, (x1 - 20, y1 - 40))
        MANHINHCUASO.blit(xe4_CaoBoiGai, (x2 - 20, y2 - 40))
        MANHINHCUASO.blit(xe4_Ninja, (x3 - 20, y3 - 40))
        MANHINHCUASO.blit(xe4_NinjaGai, (x4 - 20, y4 - 40))
        MANHINHCUASO.blit(xe4_Robot, (x5 - 20, y5 - 40))
    elif xe == 5:
        MANHINHCUASO.blit(xe5_Kiet, (x1 - 20, y1 - 40))
        MANHINHCUASO.blit(xe5_Khang, (x2 - 20, y2 - 40))
        MANHINHCUASO.blit(xe5_Loc, (x3 - 20, y3 - 40))
        MANHINHCUASO.blit(xe5_Minh, (x4 - 20, y4 - 40))
        MANHINHCUASO.blit(xe5_Long, (x5 - 20, y5 - 40))


def VeDanhDauXe():
    if xeCuoc == 1:
        MANHINHCUASO.blit(muiTen, (x1, y1 - 50))
    elif xeCuoc == 2:
        MANHINHCUASO.blit(muiTen, (x2, y2 - 50))
    elif xeCuoc == 3:
        MANHINHCUASO.blit(muiTen, (x3, y3 - 50))
    elif xeCuoc == 4:
        MANHINHCUASO.blit(muiTen, (x4, y4 - 50))
    elif xeCuoc == 5:
        MANHINHCUASO.blit(muiTen, (x5, y5 - 50))

def VeSoLuongBua():
    font = pygame.font.SysFont('Corbel', 35)
    textBuaDungLai = font.render(str(SoLuongDungLai), True, (255, 255, 255))
    textBuaVeDich = font.render(str(SoLuongVeDich), True, (255, 255, 255))
    textBuaHoanDoi = font.render(str(SoLuongHoanDoi), True, (255, 255, 255))
    textBuaQuayDau = font.render(str(SoLuongQuayDau), True, (255, 255, 255))

    if map==1:
        MANHINHCUASO.blit(textBuaDungLai, (38,272))
        MANHINHCUASO.blit(textBuaVeDich,(38,312))
        MANHINHCUASO.blit(textBuaHoanDoi, (38, 352))
        MANHINHCUASO.blit(textBuaQuayDau, (38, 392))
    elif map==2:
        MANHINHCUASO.blit(textBuaDungLai, (53, 263))
        MANHINHCUASO.blit(textBuaVeDich, (53, 303))
        MANHINHCUASO.blit(textBuaHoanDoi, (53, 343))
        MANHINHCUASO.blit(textBuaQuayDau, (53, 383))
    elif map==3:
        MANHINHCUASO.blit(textBuaDungLai, (53, 263))
        MANHINHCUASO.blit(textBuaVeDich, (53, 303))
        MANHINHCUASO.blit(textBuaHoanDoi, (53, 343))
        MANHINHCUASO.blit(textBuaQuayDau, (53, 383))
    elif map==4:
        MANHINHCUASO.blit(textBuaDungLai, (53, 380))
        MANHINHCUASO.blit(textBuaVeDich, (53, 420))
        MANHINHCUASO.blit(textBuaHoanDoi, (53, 460))
        MANHINHCUASO.blit(textBuaQuayDau, (53, 500))
    elif map==5:
        MANHINHCUASO.blit(textBuaDungLai, (53, 320))
        MANHINHCUASO.blit(textBuaVeDich, (53, 360))
        MANHINHCUASO.blit(textBuaHoanDoi, (53, 400))
        MANHINHCUASO.blit(textBuaQuayDau, (53, 440))
# ----------------Xử lý kết quả---------------#
def XepHang():
    global huong1, huong2, huong3, huong4, huong5
    global soDemXepHang

    if huong1 == 'finish':
        huong1 = soDemXepHang
        soDemXepHang = soDemXepHang + 1
    if huong2 == 'finish':
        huong2 = soDemXepHang
        soDemXepHang = soDemXepHang + 1
    if huong3 == 'finish':
        huong3 = soDemXepHang
        soDemXepHang = soDemXepHang + 1
    if huong4 == 'finish':
        huong4 = soDemXepHang
        soDemXepHang = soDemXepHang + 1
    if huong5 == 'finish':
        huong5 = soDemXepHang
        soDemXepHang = soDemXepHang + 1


def TienSauCuoc(tienCuoc, xeCuoc):
    global tongTien
    global huong1, huong2, huong3, huong4, huong5
    global SoLanHang1, SoLanHang2, SoLanHang3, SoLanHang4, SoLanHang5
    if xeCuoc == 1:
        SoLanHang1 = SoLanHang1 + 1
        return tongTien + tienCuoc * (3 - huong1)
    elif xeCuoc == 2:
        SoLanHang2 = SoLanHang2 + 1
        return tongTien + tienCuoc * (3 - huong2)
    elif xeCuoc == 3:
        SoLangHang3 = SoLanHang3 + 1
        return tongTien + tienCuoc * (3 - huong3)
    elif xeCuoc == 4:
        SoLanHang4 = SoLanHang4 + 1
        return tongTien + tienCuoc * (3 - huong4)
    elif xeCuoc == 5:
        SoLanHang5 = SoLanHang5 + 1
        return tongTien + tienCuoc * (3 - huong5)


# -----------------------------Khác---------------------------------#
########################################################################
stoptime = -1


def Spell(spellName):
    global map
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6
    global huong1, huong2, huong3, huong4, huong5
    global SoLuongQuayDau, SoLuongDungLai, SoLuongHoanDoi, SoLuongVeDich
    global xeBiStop1, xeBiStop2, xeBiStop3
    global stoptime
    if spellName == 'QuayDau' and SoLuongQuayDau > 0:
        NhacQuayDau = pygame.mixer.Sound("NhacQuayDau.mp3")
        NhacQuayDau.play()
        if huong1 == 'trai':
            huong1 = 'phai'
        if huong1 == 'phai':
            huong1 = 'trai'
        if huong1 == 'len':
            huong1 = 'xuong'
        if huong1 == 'xuong':
            huong1 = 'len'

        if huong2 == 'trai':
            huong2 = 'phai'
        if huong2 == 'phai':
            huong2 = 'trai'
        if huong2 == 'len':
            huong2 = 'xuong'
        if huong2 == 'xuong':
            huong2 = 'len'

        if huong3 == 'trai':
            huong3 = 'phai'
        if huong3 == 'phai':
            huong3 = 'trai'
        if huong3 == 'len':
            huong3 = 'xuong'
        if huong3 == 'xuong':
            huong3 = 'len'

        if huong4 == 'trai':
            huong4 = 'phai'
        if huong4 == 'phai':
            huong4 = 'trai'
        if huong4 == 'len':
            huong4 = 'xuong'
        if huong4 == 'xuong':
            huong4 = 'len'

        if huong5 == 'trai':
            huong5 = 'phai'
        if huong5 == 'phai':
            huong5 = 'trai'
        if huong5 == 'len':
            huong5 = 'xuong'
        if huong5 == 'xuong':
            huong5 = 'len'
        SoLuongQuayDau = SoLuongQuayDau - 1
    elif spellName == 'HoanDoi' and SoLuongHoanDoi > 0:
        NhacHoanDoi = pygame.mixer.Sound("NhacHoanDoi.mp3")
        NhacHoanDoi.play()
        k = random.randrange(1, 2)
        if k == 1:
            x1 = x2
            y1 = y2
            huong1 = huong2
            x2 = x3
            y2 = y3
            huong2 = huong3
            x3 = x4
            y3 = y4
            huong3 = huong4
            x4 = x5
            y4 = y5
            huong4 = huong5
            x5 = x1
            y5 = y1
            huong5 = huong1
        elif k == 2:
            x1 = x3
            y1 = y3
            huong1 = huong3
            x2 = x4
            y2 = y4
            huong2 = huong4
            x3 = x5
            y3 = y5
            huong3 = huong5
            x4 = x1
            y4 = y1
            huong4 = huong1
            x5 = x2
            y5 = y2
            huong5 = huong2
        SoLuongHoanDoi = SoLuongHoanDoi - 1
    elif spellName == 'Stop' and SoLuongDungLai > 0:
        NhacStop = pygame.mixer.Sound("NhacStop.mp3")
        NhacStop.play()
        stoptime = 50
        xeBiStop1 = random.randrange(1, 5)
        xeBiStop2 = random.randrange(1, 5)
        xeBiStop3 = random.randrange(1, 5)
        SoLuongDungLai = SoLuongDungLai - 1
    elif spellName == 'VeDich' and SoLuongVeDich > 0:
        NhacVeDich = pygame.mixer.Sound("NhacVeDich.mp3")
        NhacVeDich.play()
        k = random.randrange(1, 5)
        if k == 1:
            if map == 1:
                x1, y1 = 325, 350
                huong1 = 'trai'
            elif map == 2:
                x1, y1 = 1210, 100
                huong1 = 'phai'
            elif map == 3:
                x1, y1 = 85, 665
                huong1 = 'xuong'
            elif map == 4:
                x1, y1 = 35, 315
                huong1 = 'trai'
            elif map == 5:
                x1, y1 = 845, 185
                huong1 = 'trai'
        elif k == 2:
            if map == 1:
                x2, y2 = 325, 350
                huong2 = 'trai'
            elif map == 2:
                x2, y2 = 1210, 100
                huong2 = 'phai'
            elif map == 3:
                x2, y2 = 85, 665
                huong3 = 'xuong'
            elif map == 4:
                x2, y2 = 35, 315
                huong4 = 'trai'
            elif map == 5:
                x2, y2 = 845, 185
                huong5 = 'trai'
        elif k == 3:
            if map == 1:
                x3, y3 = 325, 350
                huong3 = 'trai'
            elif map == 2:
                x3, y3 = 1210, 100
                huong3 = 'trai'
            elif map == 3:
                x3, y3 = 85, 665
                huong3 = 'xuong'
            elif map == 4:
                x3, y3 = 35, 315
                huong3 = 'trai'
            elif map == 5:
                x3, y3 = 845, 185
                huong3 = 'trai'
        elif k == 4:
            if map == 1:
                x4, y4 = 325, 350
                huong4 = 'trai'
            elif map == 2:
                x4, y4 = 1210, 100
                huong4 = 'phai'
            elif map == 3:
                huong4 = 'xuong'
                x4, y4 = 85, 665
            elif map == 4:
                x4, y4 = 35, 315
                huong4 = 'trai'
            elif map == 5:
                x4, y4 = 845, 185
                huong4 = 'trai'
        elif k == 5:
            if map == 1:
                x5, y5 = 325, 350
                huong5 = 'trai'
            elif map == 2:
                x5, y5 = 1210, 100
                huong5 = 'phai'
            elif map == 3:
                x5, y5 = 85, 665
                huong5 = 'xuong'
            elif map == 4:
                x5, y5 = 35, 315
                huong5 = 'trai'
            elif map == 5:
                x5, y5 = 845, 185
                huong5 = 'trai'
        SoLuongVeDich = SoLuongVeDich - 1


huong1tam = huong2tam = huong3tam = huong4tam = huong5tam = 'phai'


def SpellStop():
    global huong1, huong2, huong3, huong4, huong5
    global xeBiStop1, xeBiStop2, xeBiStop3
    global huong1tam, huong2tam, huong3tam, huong4tam, huong5tam
    global stoptime

    if (stoptime > 0) and (
            huong1 != 'stop' and huong2 != 'stop' and huong3 != 'stop' and huong4 != 'stop' and huong5 != 'stop'):
        if xeBiStop1 == 1 or xeBiStop2 == 1 or xeBiStop3 == 1:
            huong1tam = huong1
            huong1 = 'stop'
        if xeBiStop1 == 2 or xeBiStop2 == 2 or xeBiStop3 == 2:
            huong2tam = huong2
            huong2 = 'stop'
        if xeBiStop1 == 3 or xeBiStop2 == 3 or xeBiStop3 == 3:
            huong3tam = huong3
            huong3 = 'stop'
        if xeBiStop1 == 4 or xeBiStop2 == 4 or xeBiStop3 == 4:
            huong4tam = huong4
            huong4 = 'stop'
        if xeBiStop1 == 5 or xeBiStop2 == 5 or xeBiStop3 == 5:
            huong5tam = huong5
            huong5 = 'stop'
    stoptime = stoptime - 1

    if stoptime == 0:
        if xeBiStop1 == 1 or xeBiStop2 == 1 or xeBiStop3 == 1:
            huong1 = huong1tam
        if xeBiStop1 == 2 or xeBiStop2 == 2 or xeBiStop3 == 2:
            huong2 = huong2tam
        if xeBiStop1 == 3 or xeBiStop2 == 3 or xeBiStop3 == 3:
            huong3 = huong3tam
        if xeBiStop1 == 4 or xeBiStop2 == 4 or xeBiStop3 == 4:
            huong4 = huong4tam
        if xeBiStop1 == 5 or xeBiStop2 == 5 or xeBiStop3 == 5:
            huong5 = huong5tam


# ----------------------------MinigameZone-------------------#
#############################################################
#############################################################
def MiniGame():
    global tongTien
    k = 1
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("T-Rex Game")
    font = pygame.font.Font('FreeSansBold.ttf', 20)
    backx = 0
    backy = 0
    drax = 50
    dray = 275
    backvelo = 0
    treex = 650
    treey = 282
    walkpoint = 0
    gravity = 7
    game = False
    gameover = False
    jump = False
    money = 0

    white = (255, 255, 255)
    black = (0, 0, 0)

    while True:

        tree = pygame.image.load("tree.png")
        tree = pygame.transform.scale(tree, (70, 50))
        tree1 = pygame.image.load("tree1.png")
        tree1 = pygame.transform.scale(tree1, (100, 60))
        tree2 = pygame.image.load("tree2.png")
        tree2 = pygame.transform.scale(tree2, (90, 60))
        tree3 = pygame.image.load("tree3.png")
        tree3 = pygame.transform.scale(tree3, (45, 60))
        tree4 = pygame.image.load("tree4.png")
        tree4 = pygame.transform.scale(tree4, (70, 60))
        # tree5=pygame.image.load("tree5.png")
        # tree5=pygame.transform.scale(tree5,(70,50))
        background = pygame.image.load("background.png")
        dragon = pygame.image.load("dra1.png")
        dragon = pygame.transform.scale(dragon, (50, 50))
        dragon2 = pygame.image.load("dra2.png")
        dragon2 = pygame.transform.scale(dragon2, (50, 50))
        dragon3 = pygame.image.load("dra3.png")
        dragon3 = pygame.transform.scale(dragon3, (50, 50))
        dragon4 = pygame.image.load("dra4.png")
        dragon4 = pygame.transform.scale(dragon4, (50, 50))
        dragon5 = pygame.image.load("dra6.png")
        dragon5 = pygame.transform.scale(dragon5, (50, 50))

        walk = [dragon, dragon, dragon, dragon, dragon2, dragon2, dragon2, dragon2, dragon3, dragon3, dragon3, dragon3,
                dragon4, dragon4, dragon4, dragon4]

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    if dray == 275:
                        backvelo = 8
                        jump = True
                        game = True
                if event.key == K_ESCAPE:
                    MainMenu()

        if backx == -600:
            backx = 0
        if treex < -600:
            treex = 650
        # jump

        if 276 > dray > 125:
            if jump == True:
                dray -= 7
        else:
            jump = False
        print(dray)
        if dray < 275:
            if jump == False:
                dray += gravity

        # collision
        if treex < drax + 50 < treex + 70 and treey < dray + 50 < treey + 50:
            backvelo = 0
            walkpoint = 0
            game = False
            gameover = True

        if treex + 400 < drax + 50 < treex + 470 and treey < dray + 50 < treey + 50:
            backvelo = 0
            game = False
            gameover = True
            walkpoint = 0
        if treex + 900 < drax + 50 < treex + 970 and treey < dray + 50 < treey + 50:
            backvelo = 0
            game = False
            gameover = True
            walkpoint = 0
        if treex + 1300 < drax + 50 < treex + 1370 and treey < dray + 50 < treey + 50:
            backvelo = 0
            game = False
            gameover = True
            walkpoint = 0
        if treex + 1700 < drax + 50 < treex + 1770 and treey < dray + 50 < treey + 50:
            backvelo = 0
            game = False
            gameover = True
            walkpoint = 0
        if game == True:
            money += 1

        backx -= backvelo
        treex -= backvelo

        screen.fill(white)
        # TEXT:
        text = font.render("Money: " + str(int(money / 10)), True, black)
        text1 = font.render("Số tiền bạn kiếm được là: " + str(int(money / 10)), True, black)
        text2 = font.render("Ấn phím ESC để về MainMenu!", True, black)
        #
        screen.blit(background, [backx + 600, backy])
        screen.blit(background, [backx, backy])
        screen.blit(text, [400, 10])
        if gameover == True:
            screen.blit(text2, [150, 100])
            screen.blit(text1, [150, 180])
            if k == 1:
                tongTien = tongTien + int(money / 10)
                k = 2
        screen.blit(walk[walkpoint], [drax, dray])
        if game == True:
            walkpoint += 1
            if walkpoint > 15:
                walkpoint = 0

        screen.blit(tree, [treex, treey])
        screen.blit(tree2, [treex + 400, treey - 8])
        screen.blit(tree3, [treex + 1300, treey - 8])
        screen.blit(tree4, [treex + 1700, treey - 2])
        pygame.display.update()


if __name__ == '__main__':
    main()
