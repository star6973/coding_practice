'''
    1064. 마지막에 떨어지는 개미

    개미들이 막대 위에 놓어져 있습니다. 각각의 개미는 왼쪽과 오른쪽으로 1초에 1cm씩 이동을 하고 있는데, 서로 부딪 힐 경우 방향을 곧바로 반대로 꺽게 됩니다.
    최초의 위치와 이동 방향이 주어졌을 때 가장 마지막에 떨어지는 개미의 시간이 몇 초 인지 구하는 프로그램을 작성 해 주세요.

    문제를 간단히 하기 위해서 개미의 크기는 무시하기로 합니다.
    개미 A가 1의 위치에서 오른쪽으로 움직이기 시작했고, 개미 B가 3의 위치에서 왼쪽으로 움직이기 시작 했다면
    개미 A와 개미 B는 2의 위치에서 1초뒤에 부딪히게 되며 그 후 개미A 는 왼쪽으로, 개미B는 오른쪽으로 움직이기 시작합니다.

    # 입력
        첫 줄에는 테스트 케이스의 갯수 T (1 <= T <= 100)가 주어지며, 각 테스트 케이스마다 첫 줄에는 개미의 수 N (1 <= N <= 1,000)과 막대의 길이 L (1 <= L <= 100,000,000) 이 주어지며
        그 다음 줄 부터는 N줄에 거쳐 개미의 위치 P ( 0 <= P <= L)와 방향 D (-1 : 왼쪽, 1 : 오른쪽)가 주어집니다.

    # 출력
        각 테스트 케이스에 해당하는 가장 마지막에 떨어지는 개미의 시간을 출력 해 주세요. 가장 끝에 도달하면 바로 떨어진다고 가정해도 됩니다.
'''

T = int(input())

for t in range(T):
    N, L = map(int, input().split())

    length = 0
    max = 0
    for n in range(N):
        P, D = map(int, input().split())
        if D == 1:
            length = L - P
        elif D == -1:
            length = -P

        if max <= abs(length):
            max = abs(length)

    print(max)