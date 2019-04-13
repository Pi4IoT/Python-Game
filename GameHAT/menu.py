import pygame
import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)      #UP
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)      #DOWN
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)         #x quit

pygame.init()

screen_width=640
screen_height=480
screen=pygame.display.set_mode((screen_width, screen_height))

pygame.mouse.set_visible(0)


def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

white=(255, 255, 255)
gray=(100, 100, 100)
background = (20, 40, 70)
yellow=(200, 200, 0)

fonts = "chintzy.ttf"
font = "chintzys.ttf"

clock = pygame.time.Clock()
FPS=30


def main():
	
	selected=1
	
	done = False
	GPIO.add_event_detect(5, GPIO.RISING, bouncetime=200)
	GPIO.add_event_detect(6, GPIO.RISING, bouncetime=200)
	GPIO.add_event_detect(16, GPIO.FALLING, bouncetime=500) #quit)

	while not done:
				
		if GPIO.event_detected(5):
			if selected > 1:
				selected -= 1
				
		elif GPIO.event_detected(6):
			if selected <3:
				selected += 1
					
		if GPIO.event_detected(16):
			if selected==1:
				print("Game 1")
				pygame.display.set_mode((1, 1))
				pygame.display.flip()
				os.system("python /home/pi/Menu/Game1.py")	
				pygame.display.set_mode((screen_width, screen_height))
				pygame.display.flip()
				
				
			if selected==2:
				print("Game 2")
				pygame.display.set_mode((1, 1))
				pygame.display.flip()
				os.system("python /home/pi/Menu/Game3.py")	
				pygame.display.set_mode((screen_width, screen_height))
				pygame.display.flip()
			
			if selected==3:
				pygame.quit()
				os.system('sudo shutdown -h now')
				quit()


		screen.fill(background)
		title=text_format("Your Games:", fonts, 70, yellow)
		
		if selected==1:
			text_Buttleship = text_format("Game 1", font, 40, white)
		else:
			text_Buttleship = text_format("Game 1", fonts, 40, gray)
	
		if selected==2:
			text_Game_2 = text_format("Game 2", font, 40, white)
		else:
			text_Game_2 = text_format("Game 2", fonts, 40, gray)			
			
					
		if selected==3:
			text_quit=text_format("QUIT", font, 50, white)
		else:
			text_quit = text_format("QUIT", fonts, 50, gray)

		title_rect=title.get_rect()
		Buttleship_rect=text_Buttleship.get_rect()
		Game_2_rect=text_Game_2.get_rect()
		quit_rect=text_quit.get_rect()


		screen.blit(title, (screen_width/2 - (title_rect[2]/2), 50))
		screen.blit(text_Buttleship, (screen_width/2 - (Buttleship_rect[2]/2), 200))
		screen.blit(text_Game_2, (screen_width/2 - (Game_2_rect[2]/2), 280))		
		screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
		pygame.display.update()
		clock.tick(FPS)
		pygame.display.set_caption("Main Menu")
		

if __name__ == '__main__':

    main()

