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

class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다." .format(self.name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}" .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

class attackunit(unit):
    def __init__(self, damage):
      
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

#마린
class Marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, "마린", 40, 1, 5)

        #스팀팩
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. [HP 10 감소]" .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다." .format(self.name))
#탱크
class Tank(attackunit):
    #시즈모드
    seize_developed = False #시즈모드 개발여부


    def __init__(self):
        attackunit.__init__(self, "탱크", 150, 1, 35)
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
            