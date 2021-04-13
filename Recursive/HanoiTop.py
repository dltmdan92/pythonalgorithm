"""
개가튼 하노이의 탑

아래와 같은 패턴으로 하면 된다. 개같은거...

<1 1 3>
--> <0 1 x> <1 1 3> <0 x 3>

<2 1 3>
--> <1 1 2> + <2 1 3>  + <1 2 3>

<3 1 3>
--> <2 1 2> + <3 1 3> + <2 2 3>

<4 1 3>
--> <3 1 2> + <4 1 3> + <3 2 3>

<5 1 3>
--> <4 1 2> + <5 1 3> + <4 2 3>

"""

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks == 0:
        return
    else:
        mid_peg = 6 - start_peg - end_peg
        hanoi(num_disks - 1, start_peg, mid_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, mid_peg, end_peg)


# 테스트 코드 (포함하여 제출해주세요)
hanoi(4, 1, 3)