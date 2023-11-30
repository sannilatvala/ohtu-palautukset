POITNS_0 = "Love"
POINTS_15 = "Fifteen"
POINTS_30 = "Thirty"
POINTS_40 = "Forty"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score_player1 += 1
        else:
            self.score_player2 += 1

    def get_score(self):
        if self.score_player1 == self.score_player2:
            return self._get_equal_scores()
        
        if self.score_player1 >= 4 or self.score_player2 >= 4:
            return self._get_advantage_or_win()
        return self._get_other_scores()

    def _get_equal_scores(self):
        if self.score_player1 < 3:
            return [POITNS_0, POINTS_15, POINTS_30][self.score_player1] + "-All"
        return "Deuce"

    def _get_advantage_or_win(self):
        score_difference = self.score_player1 - self. score_player2

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        if score_difference == -1:
            return f"Advantage {self.player2_name}"
        if score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _get_other_scores(self):
        game_status = ""
        player_scores = [self.score_player1, self.score_player2]
        for player_score in player_scores:
            if game_status:
                game_status += "-"
            game_status += [POITNS_0, POINTS_15, POINTS_30, POINTS_40][player_score]

        return game_status
