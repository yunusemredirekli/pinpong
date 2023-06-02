# Kütüphaneleri içeri akatarıyoruz
from pygame import *
'''Gerekli Sınıflar'''

# sprite'lar için ebeveyn sınıfı
class GameSprite(sprite.Sprite):
   def __init__(self,player_image,player_x,player_y,player_speed,width,height):
       super().__init__()
       self.image = transform.scale(image.load(player_image),(width,height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   
   def reset(self):
       window.blit(self.image, (self.rect.x,self.rect.y))

# oyuncu'lar sınıfı 
class Player(GameSprite):
   # Right
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -=self.speed
       if keys[K_DOWN] and self.rect.y < win_height -80:
           self.rect.y +=self.speed
   # Left
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -=self.speed
       if keys[K_s] and self.rect.y < win_height -80:
           self.rect.y +=self.speed

# Oyun Sahnesi
back = (200,255,255) # arka plan rengini belirledik
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

# bir top ve 2 adet raket oluşturma
racket1 = Player("racket.png",30,200,4,50,150)
racket2 = Player("racket.png",520,200,4,50,150)
ball = GameSprite("tenis_ball.png",200,200,4,50,50)

# oyunun durumundan sorumlu bayraklar(flag)
game = True
finis = False
clock = time.Clock()
FPS = 60

# Ekrandaki yarışmacıları bilgilendirmek için yazılar
font.init()
font = font.Font(None,35)
lose1 = font.render("PLAYER 1 LOSE",True,(180,0,0))
lose2 = font.render("PLAYER 2 LOSE",True,(0,0,180))

# Topun hızını belirlenmesinde kullanılacak değişkenler
speed_x = 3
speed_y = 3

# oyun döngümüz
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finis != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        #Top ile raketin birleşmesi 
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *=-1 
            speed_y *=1
        # Top ekranın kenarlarına ulaşırsa hareket yönü değişir
        if ball.rect.y > win_height-50 or ball.rect.y<0:
            speed_y *=-1
        # ilk oyuncunun kaybetme durumun belirlenmesi
        if ball.rect.x < 0:
            finis = True
            window.blit(lose1,(200,200))
            game_over = True
        # ikinci oyuncunun kaybetme durumun belirlenmesi
        if ball.rect.x > win_width:
            finis = True
            window.blit(lose2,(200,200))
            game_over = True
        
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()



    else:
         # Reset game variables and objects
        time.delay(1000)
        finish = False
        speed_x = 3
        speed_y = 3
        racket1.rect.x = 30
        racket1.rect.y = 200
        racket2.rect.x = 520
        racket2.rect.y = 200
        ball.rect.x = 200
        ball.rect.y = 200
    clock.tick(FPS)





