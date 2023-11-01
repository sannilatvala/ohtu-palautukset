from statistics_service import StatisticsService
from player_reader import PlayerReader
from sortby import SortBy


def main():
    data_url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    player_reader = PlayerReader(data_url)
    stats = StatisticsService(player_reader)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)
        

if __name__ == "__main__":
    main()
