# Muhammad Abubakar
block = [1, 2, 3, 4, 5, 6, 7, 8, 9]
who_won_the_toss = input("Enter for the one who play first: ").upper()

if who_won_the_toss == "X":
    who_lost_the_toss = "0"
elif who_won_the_toss == "0":
    who_lost_the_toss = "X"

first_player = True
second_player = False
count = 0


def check_win():
    if block[0] == block[1] == block[2] or block[0] == block[3] == block[6]:
        print(block[0])
        return True
    elif block[3] == block[4] == block[5] or block[1] == block[4] == block[7]:
        print(block[4])
        return True
    elif block[6] == block[7] == block[8] or block[2] == block[5] == block[8]:
        print(block[8])
        return True
    elif block[0] == block[4] == block[8] or block[2] == block[4] == block[6]:
        print(block[4])
        return True


while count <= 9:
    print(f"""
     {block[0]} | {block[1]} | {block[2]}
    ---|---|---
     {block[3]} | {block[4]} | {block[5]}
    ---|---|---
     {block[6]} | {block[7]} | {block[8]} """)

    if check_win():
        print(f"is the winner")
        break

    elif first_player:
        block_number = int(input(f"play {who_won_the_toss}: "))
        block_number = block_number - 1
        block[block_number] = f"{who_won_the_toss}"
        first_player = False
        second_player = True
    elif second_player:
        block_number = int(input(f"play {who_lost_the_toss} : "))
        block_number = block_number - 1
        block[block_number] = f"{who_lost_the_toss}"
        second_player = False
        first_player = True

    count += 1
