import random

print("===  턴제 보스전 게임 ===")

# 초기 상태 설정
player_hp = 100
boss_hp = 120
turn = 1

# [제어문 1] while 문: 둘 중 하나라도 체력이 0 이하가 될 때까지 반복
while player_hp > 0 and boss_hp > 0:
    print(f"\n--- [Turn {turn}] ---")
    print(f"내 체력: {player_hp} | 보스 체력: {boss_hp}")
    print("1. 일반공격 | 2. 필살기(50% 확률) | 3. 체력회복")

    choice = input("행동 선택 (1~3): ")

    # [제어문 2] match-case 문: 유저의 입력값에 따른 행동 분기
    match choice:
        case "1":
            damage = random.randint(15, 25)
            boss_hp -= damage
            print(f"\n 일반공격 성공! 보스에게 {damage} 데미지!")
        case "2":
            # [제어문 3] if-else 문: 확률적 성공 조건 처리
            if random.random() < 0.5:
                damage = random.randint(35, 50)
                boss_hp -= damage
                print(f"\n 필살기 적중! 보스에게 {damage} 대폭딜!")
            else:
                print("\n 필살기 실패! 공격이 빗나갔습니다.")
        case "3":
            heal = random.randint(20, 30)
            player_hp += heal
            print(f"\n 체력 회복! 체력이 {heal}만큼 증가했습니다.")
        case _:
            print("\n 잘못된 입력으로 턴을 허비했습니다.")

    # [제어문 4] break 문: 보스 처치 시 루프 즉시 탈출
    if boss_hp <= 0:
        print("\n 보스를 처치했습니다! 승리!")
        break

    # 보스의 반격 턴
    boss_damage = random.randint(10, 25)
    player_hp -= boss_damage
    print(f" 보스의 반격! {boss_damage} 데미지를 입었습니다.")

    # 플레이어 패배 시 루프 탈출
    if player_hp <= 0:
        print("\n 당신은 쓰러졌습니다... 패배!")
        break

    turn += 1

print("=== 게임 종료 ===")