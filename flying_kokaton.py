import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習7

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    kk_img = pg. transform.rotozoom(kk_img, 10, 1.0)

    kk_rct = kk_img.get_rect() #練習8
    kk_rct.center = 300, 200
    screen.blit(kk_img, kk_rct)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr % 3200) #練習6

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x + 1600, 0]) #練習7
        screen.blit(bg_img, [x + 3200, 0])
        screen.blit(bg_img2, [x + 4800, 0])
        key_lst = pg.key.get_pressed() #練習8-3
        kk_x, kk_y = 0, 0
        # if (key_lst[pg.K_LEFT] == False) and (key_lst[pg.K_DOWN] == False) and (key_lst[pg.K_UP] == False) and (key_lst[pg.K_RIGHT] == False): #演習課題1
        #     kk_rct.move_ip((-1, 0))
        # else: #演習課題2
        if key_lst[pg.K_UP]:
                kk_y -= 1
        if key_lst[pg.K_DOWN]:
                kk_y += 1
        if key_lst[pg.K_LEFT]:
                kk_x -= 1
        if key_lst[pg.K_RIGHT]:
                kk_x += 2
        kk_x -= 1      
        kk_rct.move_ip((kk_x, kk_y))

        # if key_lst[pg.K_UP]:
        #     kk_rct.move_ip((0, -1))
        # if key_lst[pg.K_DOWN]:
        #     kk_rct.move_ip((0, 1))
        # if key_lst[pg.K_LEFT]:
        #     kk_rct.move_ip((-1, 0))
        # if key_lst[pg.K_RIGHT]:
        #     kk_rct.move_ip((1, 0))

        # x = -(tmr % 3200) #練習6

        # screen.blit(bg_img, [x, 0])
        # screen.blit(bg_img2, [x + 1600, 0]) #練習7
        # screen.blit(bg_img, [x + 3200, 0])
        # screen.blit(bg_img2, [x + 4800, 0])
        # screen.blit(kk_img, [300, 200]) #練習4
        screen.blit(kk_img, kk_rct) #練習8-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()