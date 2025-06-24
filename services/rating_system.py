K = 32  # Rating adjustment factor

def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

def update_rating(rating_a, rating_b, result):
    expected_a = expected_score(rating_a, rating_b)
    score_a = 1 if result == 'A' else 0
    delta = K * (score_a - expected_a)
    return rating_a + delta, rating_b - delta

def handle_singles(player_a, player_b, result):
    new_a, new_b = update_rating(player_a.rating, player_b.rating, result)
    player_a.rating = round(new_a)
    player_b.rating = round(new_b)

def handle_doubles(team_a, team_b, result):
    avg_a = sum(p.rating for p in team_a) / 2
    avg_b = sum(p.rating for p in team_b) / 2
    new_avg_a, new_avg_b = update_rating(avg_a, avg_b, result)
    for player in team_a:
        player.rating = round(player.rating + (new_avg_a - avg_a))
    for player in team_b:
        player.rating = round(player.rating + (new_avg_b - avg_b))
