# for i in range(1,51):
#     with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")



#클래스 수업#
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다." .format(name))
# print("체력 {0}, 공격력 {1}\n" .format(hp, damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다." .format(tank_name))
# print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다." .format(tank2_name))
# print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다." .format(self.name))
    
    def move(self, location):
       
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

class Attackunit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
             .format(self.name, location, self.damage))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
             .format(self.name, location, self.flying_speed))
        

#마린
class Marine(Attackunit):
    def __init__(self):
        Attackunit.__init__(self, "마린", 40, 1, 5)

        #스팀팩
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. [HP 10 감소]" .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다." .format(self.name))
#탱크
class Tank(Attackunit):
    #시즈모드
    seize_developed = False #시즈모드 개발여부


    def __init__(self):
        Attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        #시즈모드로 전환
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다." .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class FlyableAttackUnit(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        
        self.fly(self.name, location)
# 레이스   
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 (해제상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드로 해제합니다." .format(self.name))
            self.clocked = False
        else: #클로킹 모드로 전환
            print("{0} : 클로킹 모드로 전환합니다." .format(self.name))
            self.clocked = True

def game_start():
    print("게임을시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")


#게임 시작
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("탱크 시즈 모드 개발이 완료 되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해    
for unit in attack_units:
    unit.damaged(randint(5, 21))

#게임 종료
game_over()