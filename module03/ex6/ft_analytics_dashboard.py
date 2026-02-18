
players = ['alice', 'bob', 'charlie', 'diana']
scores = [2300, 1800, 2150, 2050]
achievements = {
    'alice': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
              'boss_slayer'],
    'bob': ['first_kill', 'level_10', 'boss_slayer'],
    'charlie': ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                'collector', 'first_kill', 'speed_demon'],
    'diana': ['first_kill', 'level_10']
}
regions = ['north', 'east', 'central', 'north']

print("=== Game Analytics Dashboard ===\n")

high_scorers = [players[i] for i, score in enumerate(scores) if score > 2000]
scores_doubled = [score * 2 for score in scores]
active_players = [player for player, ach in achievements.items()
                  if len(ach) > 2]

print("=== List Comprehension Examples ===")
print("High scorers (>2000):", high_scorers)
print("Scores doubled:", scores_doubled)
print("Active players:", active_players)
print()


player_scores = {
    player: scores[players.index(player)]
    for player in active_players
}

score_categories = {
    'high': sum(1 for s in scores if s > 2000),
    'medium': sum(1 for s in scores if 1500 <= s <= 2000),
    'low': sum(1 for s in scores if s < 1500)
}
achievement_counts = {player: len(ach) for player, ach in achievements.items()}

print("=== Dict Comprehension Examples ===")
print("Player scores:", player_scores)
print("Score categories:", score_categories)
print("Achievement counts:", achievement_counts)
print()

unique_players = {player for player in players}
unique_achievements = {ach for ach_list in achievements.values()
                       for ach in ach_list}
active_regions = {region for region in regions}

print("=== Set Comprehension Examples ===")
print("Unique players:", unique_players)
print("Unique achievements:", unique_achievements)
print("Active regions:", active_regions)
print()

total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(scores) / len(scores)
top_index = scores.index(max(scores))
top_performer = players[top_index]
top_achievements = len(achievements[top_performer])

print("=== Combined Analysis ===")
print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print(f"Average score: {average_score}")
print(f"Top performer: {top_performer} ({scores[top_index]} points, "
      f"{top_achievements} achievements)")
