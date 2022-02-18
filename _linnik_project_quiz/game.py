# -*- coding: utf-8 -*-

import os
import pygame
import random

pygame.init()
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)

#переменные
x = []
score = 0
is_it_menu = True
is_it_fin = False
is_it_text = False
now = 0
time = 0
nowchoice = 0
spi = []
phrases = ['Как ты вообще смог открыть этот квиз?', 'Вам предстоит ещё много работы:)',
           'Треть - это на треть больше, чем ноль!', 'Половина - это отличный результат!',
           'Две трети - это на две трети больше, чем ноль!',
           'Вы - гений обществознания?', 'Вы просто отлино знаете обществознание! Возьмите перерыв:)']
q = open('questions.txt', encoding='utf-8')
for line in q:
    spi.append(line[:-1])
q.close()
f = pygame.font.Font(None, 60)
f2 = pygame.font.Font(None, 40)
f3 = pygame.font.Font(None, 30)

#функция загрузки спрайтов
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == 'yes':
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

#загрузка спрайтов
menu_for_quiz = pygame.sprite.Group()
the_quiz = pygame.sprite.Group()

a_menu = pygame.sprite.Sprite()
a_menu.image = load_image("menu.png")
a_menu.rect = a_menu.image.get_rect()
menu_for_quiz.add(a_menu)


q_bg0 = pygame.sprite.Sprite()
q_bg0.image = load_image("fra.png")
q_bg0.rect = q_bg0.image.get_rect()
the_quiz.add(q_bg0)
ktl_now = q_bg0

q_bg1 = pygame.sprite.Sprite()
q_bg1.image = load_image("fra1.png")
q_bg1.rect = q_bg1.image.get_rect()

q_bg2 = pygame.sprite.Sprite()
q_bg2.image = load_image("fra2.png")
q_bg2.rect = q_bg2.image.get_rect()

q_bg3 = pygame.sprite.Sprite()
q_bg3.image = load_image("fra3.png")
q_bg3.rect = q_bg3.image.get_rect()

q_bg4 = pygame.sprite.Sprite()
q_bg4.image = load_image("fra4.png")
q_bg4.rect = q_bg4.image.get_rect()

#остальное

def is_it_good_answer(nc, a):
    if spi[a + nc][0] == 1:
        return True
    return False

class Timer():
    def start(self):
        global time
        time = 41
    def change(self):
        global time
        if time - 1 >= 0:
            time -= 1
        return f.render(str(time), True, (250, 250, 250))
    def is_it_time(self):
        if time == 0:
            return True
        return False


#основная функция
clock = pygame.time.Clock()
pygame.display.set_caption('Квизер: обществознание')
running = True
while running:
    if is_it_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = event.pos
                if 260 < a < 705 and 345 < b < 412:
                    x = []
                    while len(x) < 6:
                        z = random.randint(1, 42) * 5 - 4
                        if z not in x:
                            x.append(z)
                    is_it_menu = False
        menu_for_quiz.draw(screen)
        pygame.display.flip()
    elif is_it_fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((60, 60, 120))
        tscore = f.render('Итог: ' + str(score) + '/6', True, (250, 250, 250))
        tt = f2.render(phrases[score], True, (250, 250, 250))
        screen.blit(tscore, (400, 300))
        screen.blit(tt, (70, 550))
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = event.pos
                if 25 < xx < 477:
                    if 320 < yy < 387:
                        the_quiz.add(q_bg1)
                        the_quiz.remove(ktl_now)
                        ktl_now = q_bg1
                        nowchoice = 1
                    elif 435 < yy < 505:
                        the_quiz.add(q_bg2)
                        the_quiz.remove(ktl_now)
                        ktl_now = q_bg2
                        nowchoice = 2
                elif 520 < xx < 968:
                    if 320 < yy < 387:
                        the_quiz.add(q_bg3)
                        the_quiz.remove(ktl_now)
                        ktl_now = q_bg3
                        nowchoice = 3
                    elif 435 < yy < 505:
                        the_quiz.add(q_bg4)
                        the_quiz.remove(ktl_now)
                        ktl_now = q_bg4
                        nowchoice = 4
                if 270 < xx < 720 and 540 < yy < 606:
                    if nowchoice == 0:
                        pass
                    elif spi[x[now - 1] + nowchoice][0] == '1':
                        score += 1
                        is_it_text = False
                    else:
                        is_it_text = False
        the_quiz.draw(screen)
        if not is_it_text:
            if now >= 6:
                is_it_fin = True
                now = 0
            else:
                the_quiz.remove(ktl_now)
                the_quiz.add(q_bg0)
                ktl_now = q_bg0
                nowque = str(spi[x[now]])
                nnowque = ''
                if len(nowque) > 70:
                    yaho = 4
                    while len(' '.join(nowque.split()[:yaho])) < 60:
                        yaho += 1
                    nnowque = ' '.join(nowque.split()[yaho:])
                    nowque = ' '.join(nowque.split()[:yaho])
                qu = f3.render(str(now + 1) + '. ' + nowque, True, (250, 250, 250))
                qu05 = f3.render(nnowque, True, (250, 250, 250))
                qu1 = f2.render('А: ' + str(spi[x[now] + 1])[1:], True, (0, 0, 0))
                qu2 = f2.render('Б: ' + str(spi[x[now] + 2])[1:], True, (0, 0, 0))
                qu3 = f2.render('В: ' + str(spi[x[now] + 3])[1:], True, (0, 0, 0))
                qu4 = f2.render('Г: ' + str(spi[x[now] + 4])[1:], True, (0, 0, 0))
                txtscore = f.render('Счёт: ' + str(score), True, (250, 250, 250))
                now += 1
                is_it_text = True
                nowchoice = 0
                Timer().start()
        else:
            if Timer().is_it_time():
                is_it_text = False
            screen.blit(Timer().change(), (855, 50))
            screen.blit(qu, (70, 110))
            screen.blit(qu05, (70, 140))
            screen.blit(qu1, (60, 340))
            screen.blit(qu2, (60, 460))
            screen.blit(qu3, (550, 340))
            screen.blit(qu4, (550, 460))
            screen.blit(txtscore, (750, 650))
            screen.blit(f.render('Ответить', True, (0, 0, 0)), (405, 555))
            pygame.display.flip()
            clock.tick(1)
if pygame.event.wait().type == pygame.QUIT:
    pygame.quit()



