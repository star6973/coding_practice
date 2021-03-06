'''
    1077. 자바프로그래밍 실습시험 연습문제: 중복 존재???

    김상진 교수의 딸 소희는 포켓몬 카드를 수집한다. 이를 옆에서 본 소희 친구 수아도 소희처럼 카드 수집을 하기로 결심하였다.
    착한 소희는 자신이 가지고 있는 카드 중 중복된 카드를 수아에게 주고자 한다.
    포켓몬 카드를 정수로 표현할 때 중복된 카드가 있는지 여부부터 도와주세요.

    # 입력
        첫 줄에는 테스트 케이스의 수 T가 주어집니다.
        다음 줄부터는 각 테스트 케이스마다 포켓몬 카드의 수 N(32비트 정수)이 주어지며, 포켓몬 카드를 나타내는 N개의 정수가 주어진다.

    # 출력
        중복된 카드가 존재하면  true를 없으면 false를 출력하시오.
'''

T = int(input())

for t in range(T):
    N = int(input())
    card = list(input().split(' '))
    dup_card = list(set(card))

    if len(card) != len(dup_card):
        print('true')
    else:
        print('false')