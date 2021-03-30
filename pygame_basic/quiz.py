import pygame
######################################################################################################
#기본 초기화 (필수적인 것들)
pygame.init() #초기화 (반드기 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥피하기 게임")

#FPS
clock = pygame.time.Clock()
######################################################################################################

#1. 사용자 게임 초기화 (배경, 이미지, 좌표, 속도,  폰트 등)
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임화면 초당 프레임 수 설정

    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
        if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed #'to_x = to_x -5'랑 같은 의미
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed


             
    #3. 게임 캐릭터 위치 정의
  
    #4. 충돌 처리

    #5. 화면에 그리기

    pygame.display.update() #게임화면을 다시 그리기!

#pygame 종료
pygame.quit()