from Card import Card
from Dealer import Dealer
from Deck import Deck
from Game import Game
from Hand import Hand
from Player import Player

def main():
    cib = 100
    print("블랙잭 게임에 오신 것을 환영합니다!")
    name = input("이름을 입력해주세요: ")

    while True:
        if cib <= 0:
            print("칩이 모두 소진되었습니다. 게임 종료!")
            break

        print("\n────────── 새 게임 ──────────")
        print(f"보유 칩: {cib}")
        try:
            betting = int(input("배팅할 금액을 입력해 주세요: "))
        except ValueError:
            print("숫자로 입력해 주세요.")
            continue

        if betting > cib or betting <= 0:
            print("잘못된 금액입니다. 다시 입력해주세요.")
            continue

        cib -= betting

        game = Game()
        player = Player(game)
        dealer = Dealer(game, player.hand)

        # 출력: 딜러 카드 한 장만 공개
        visible_card = player.hand.dealer[0]
        dealer_str = f"{visible_card}, hidden"
        player_str = ', '.join(str(card) for card in player.hand.player)

        print(f"\n{name}의 카드: [{player_str}]")
        print(f"{name}의 초기 점수:", player.hand.score('player'))
        print(f"\n딜러의 카드: [{dealer_str}]")
        print("딜러 초기 점수:", visible_card.get_value())

        # 블랙잭 판정
        if player.hand.score('player') == 21:
            print("블랙잭! 이겼습니다!")
            cib += int(betting * 2.5)
        else:
            # 플레이어 턴
            while True:
                move = input("입력 (hit / stand): ").strip().lower()
                if move == 'hit':
                    score = player.Hit()
                    player_str = ', '.join(str(c) for c in player.hand.player)
                    print(f"{name}의 카드: {player_str}")
                    print("현재 점수:", score)
                    if score > 21:
                        print("버스트! 당신은 졌습니다.")
                        break
                elif move == 'stand':
                    print("턴 종료")
                    break
                else:
                    print("잘못된 입력입니다. hit 또는 stand를 입력하세요.")

            # 딜러 턴
            dealer.play()

            # 승패 판정
            player_score = player.hand.score('player')
            dealer_score = player.hand.score('dealer')

            print("\n[결과]")
            if player_score > 21:   
                print("버스트! 패배")
        
            elif dealer_score > 21 or player_score > dealer_score:
                print("이겼습니다!")
                cib += betting * 2
            
            elif player_score < dealer_score:
                print("딜러 승리!")
                # 칩 차감은 이미 됐음
            else:
                print("무승부!")
                cib += betting  # 환불

        cont = input("\n계속 하시겠습니까? (1: 계속 / 기타: 종료): ").strip()
        if cont != "1":
            print(f"게임 종료! 최종 칩: {cib}")
            break

if __name__ == "__main__":
    main()