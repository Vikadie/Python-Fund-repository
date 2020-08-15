from functools import reduce

inp_line = input()

statistics = dict() # {player1: {position1: skill, position2: skill}, player2: {position1: skill, position2: skill} }

while inp_line != 'Season end':
    if ' -> ' in inp_line:
        player, position, skill_str = inp_line.split(' -> ')
        skill = int(skill_str)
        if player in statistics:
            if position in statistics[player]:
                if skill > statistics[player][position]:
                    statistics[player][position] = skill
            else:
                statistics[player][position] = skill
        else:
            pos_skill_dict = dict()
            pos_skill_dict[position] = skill
            statistics[player] = pos_skill_dict
    elif ' vs ' in inp_line:
        player1, player2 = inp_line.split(' vs ')
        if player1 in statistics and player2 in statistics:
            for position in statistics[player1]:
                if position in statistics[player2]:
                    sum_player_1 = reduce(lambda a,b: a+b, statistics[player1].values())
                    sum_player_2 = reduce(lambda a,b: a+b, statistics[player2].values())
                    if sum_player_1 > sum_player_2:
                        statistics.pop(player2)
                    elif sum_player_2 > sum_player_1:
                        statistics.pop(player1)
                    break

    inp_line = input()

players = dict()
for player in statistics:
    sum_player = reduce(lambda a, b: a + b, statistics[player].values())
    players[player] = sum_player

ordered_players = dict(sorted(players.items(), key = lambda x: (-x[1], x[0])))

for pl, tot_sk in ordered_players.items():
    print(f"{pl}: {tot_sk} skill")
    d = statistics[pl]
    ordered_positions = dict(sorted(d.items(), key = lambda x: (-x[1], x[0])))
    for pos, skill in ordered_positions.items():
        print(f"- {pos} <::> {skill}")
