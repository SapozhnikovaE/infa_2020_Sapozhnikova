import math
import pygame

BLACK_COLOR= (0,0,0)
WHITE_COLOR= (255,255,255)
RED_COLOR=   (255,0,0)

SKY_COLOR =  (180,242,253)
SEA_COLOR =  (63,36,214)
SAND_COLOR = (239,245,83)
SUN_COLOR =  (253,247,87)
SHIP_COLOR =  (173,86,33)
SHIP_PEN_COLOR =  (152,76,49)

DARK_GRAY_COLOR = (179,182,139)
LIGHT_GRAY_COLOR = (220,213,159)

UMBRELLA_COLOR1 = (213,133,57)
UMBRELLA_COLOR2 = (223,94,88)

def genarate_waves_poligon(rx,ry,rw,rh,wh= 7):
   points= []
   points.append([rx+rw,ry])
   points.append([rx+rw,ry+rh])
   points.append([rx,ry+rh])
   points.append([rx,ry])
   
   с = 2*math.pi/rw*7  # 7 волн
   for x in range(rw):
     y= wh*math.sin(с*x)    
     points.append([rx+x,ry-int(y)])
   return points  
   
def genarate_sun_poligon(px,py,r1,r2,ray_count=60):
   angle = 2*math.pi/60
   points= []
   
   for i in range(ray_count):
      x2= r2*math.sin(i*angle)    
      y2= r2*math.cos(i*angle) 
      x1= r1*math.sin(i*angle+angle/2)    
      y1= r1*math.cos(i*angle+angle/2) 
      points.append((px+int(x2),py-int(y2)))    
      points.append((px+int(x1),py-int(y1)))

   return points    

def draw_ship(surface):        
   width, height =  surface.get_rect()[2:]
   points = [] 
   
   r = int(0.2*height)   
   x1= r
   y1= height-r
   points.append((x1,y1))
   
   start_angle = 180
   stop_angle =  270
   for angle in range(start_angle,stop_angle):
     x = int(r*math.cos(math.radians(angle)))
     y = int(r*math.sin(math.radians(angle)))
     points.append((x1+x,y1-y))
   points.append((r,height))
   
   x2= width-int(0.2*width)
   y2= height 
   points.append((x2,y2))
   
   x3= width
   y3= height-r
   points.append((x3,y3))
          
   pygame.draw.polygon(surface, SHIP_COLOR, points)
   pygame.draw.polygon(surface, SHIP_PEN_COLOR, points, 1)
   
   pygame.draw.line(surface, SHIP_PEN_COLOR, (x1, y1), (x1, 0+height))
   pygame.draw.line(surface, SHIP_PEN_COLOR, (x2, y2), (x2, y1))
   
   x4= int(0.4*width)
   b= 7
   pygame.draw.rect(surface, BLACK_COLOR, pygame.Rect(x4, 0, b, y1))
     
   points = [ (x4+b,y1),(x4+b+y1//2,y1//2),(x4+b,0),(x4+b+y1//5,y1//2) ] 
   
   pygame.draw.polygon(surface, LIGHT_GRAY_COLOR, points)
   pygame.draw.polygon(surface, DARK_GRAY_COLOR, points, 1)
   pygame.draw.line(surface, DARK_GRAY_COLOR, (x4+b+y1//2,y1//2), (x4+b+y1//5,y1//2))
   
   eluminator_center = ( x2+10, int(height-r+r/3) )
   pygame.draw.circle(surface, WHITE_COLOR, eluminator_center, 5)
   pygame.draw.circle(surface,  BLACK_COLOR, eluminator_center, 6, 2)
   


def draw_umbrella(surface):
   width, height =  surface.get_rect()[2:]
   points = []   
   y1 = int(0.2*height)   
   
   b= 4
   x1= int(width//2 - b//2)
   x2= int(width//2 + b//2)
   
   points= [ (x1,0),  (x2,0), (width,y1), (0,y1)]
   pygame.draw.polygon(surface, UMBRELLA_COLOR2, points)
  
   pygame.draw.rect(surface, UMBRELLA_COLOR1, pygame.Rect(x1, y1, b, height-y1)) 
   pygame.draw.rect(surface, (183,76,70), pygame.Rect(x1, 0, b, y1),1) 
  
   d = int(width/7)
   for i in range(1,3):
     pygame.draw.line(surface, (183,76,70), (x1,0), (i*d,y1) )
     pygame.draw.line(surface, (183,76,70), (x2,0), (width-i*d,y1) )
   
def draw_cloud(surface):
   width, height =  surface.get_rect()[2:]
   r = height//3
   x= r
   for i in range(3):     
     pygame.draw.circle(surface, WHITE_COLOR, (x+r,r), r-1)
     pygame.draw.circle(surface, DARK_GRAY_COLOR, (x+r,r), r, 1)
   
     pygame.draw.circle(surface, WHITE_COLOR, (x,height-r), r-1)
     pygame.draw.circle(surface, DARK_GRAY_COLOR,(x,height-r), r, 1) 
     
     x += int(1.5*r)
   pygame.draw.circle(surface, WHITE_COLOR, (x,height-r), r-1)
   pygame.draw.circle(surface, DARK_GRAY_COLOR,(x,height-r), r, 1)           

def main():  
  height= 400
  width= int(height*1.5)
  
  pygame.init()
  screen = pygame.display.set_mode((width,height))
  
  done = False
  clock = pygame.time.Clock()

  waves_poligon= genarate_waves_poligon(0,int(0.75*height),width,int(0.75*height))
  sun_poligon=   genarate_sun_poligon(width-52-10,45+10,45,52)
  
  ship1_size = (220,120)
  ship1_surface= pygame.Surface(ship1_size)
  ship1_surface.fill(RED_COLOR)
  ship1_surface.set_colorkey(RED_COLOR)                 
  draw_ship(ship1_surface)  
  
  ship2_size= (ship1_size[0]//2,ship1_size[1]//2)
  ship2_surface= pygame.transform.scale(ship1_surface, ship2_size)
    
  umbrella1_size = (int(0.7*height//4),height//4)  
  umbrella1_surface= pygame.Surface(umbrella1_size)  
  umbrella1_surface.fill(RED_COLOR)
  umbrella1_surface.set_colorkey(RED_COLOR)    
  draw_umbrella(umbrella1_surface)
  
  umbrella2_size = umbrella1_size[0]*2//3,umbrella1_size[1]*2//3
  umbrella2_surface= pygame.transform.scale(umbrella1_surface, umbrella2_size)
  
  cloud1_size= (160, 71)
  cloud1_surface= pygame.Surface(cloud1_size)  
  cloud1_surface.fill(RED_COLOR)
  cloud1_surface.set_colorkey(RED_COLOR)      
  draw_cloud(cloud1_surface)  
  
  cloud2_size = int(0.7*cloud1_size[0]), int(0.7*cloud1_size[1])
  cloud3_size = int(0.9*cloud1_size[0]), int(0.7*cloud1_size[1])
  
  cloud2_surface = pygame.transform.scale(cloud1_surface, cloud2_size)
  cloud3_surface = pygame.transform.scale(cloud1_surface, cloud3_size)
  
  while not done:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              done = True
          
        screen.fill((0, 0, 0))        
        pygame.draw.rect(screen, SKY_COLOR, pygame.Rect(0, 0, width, height//2))
        pygame.draw.rect(screen, SEA_COLOR, pygame.Rect(0, height//2,width,height))
        
        pygame.draw.polygon(screen, SAND_COLOR, waves_poligon)
        pygame.draw.polygon(screen, SUN_COLOR, sun_poligon)
        
        screen.blit(ship1_surface, (width-ship1_size[0]-30, height//2-ship1_size[1]//2))                      
        screen.blit(ship2_surface, (width//2-ship2_size[0], height//2-ship2_size[1]//2))
        
        screen.blit(umbrella1_surface, (50,height-umbrella1_size[1]-40))
        screen.blit(umbrella2_surface, (150,height-umbrella2_size[1]-50))
        
        screen.blit(cloud1_surface, ( width//2-cloud1_size[0]//2, 10))        
        screen.blit(cloud2_surface, ( width//4-cloud2_size[0]+20, 10))        
        screen.blit(cloud3_surface, ( width//4-cloud3_size[0]+20, 70))
                
        pygame.display.flip()        
        clock.tick(60)
  
      
if __name__ == "__main__":
  main()    