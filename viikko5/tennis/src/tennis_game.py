class TennisGame:
    score_terms = {
        0:"Love",
        1:"Fifteen",
        2:"Thirty",
        3:"Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_p1 = 0
        self.score_p2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score_p1 += 1
        if player_name == self.player2_name:
            self.score_p2 += 1

    def get_score(self):
        winner = self._winner()
        if winner:
            return f"Win for {winner}"

        if self._advantage_phase():
            if self.score_p1 > self.score_p2:
                return f"Advantage {self.player1_name}"
            elif self.score_p2 > self.score_p1:
                return f"Advantage {self.player2_name}"
            else:
                return "Deuce"
        if self.score_p1 == self.score_p2:
            return f"{self.score_terms[self.score_p1]}-All"
        score_term_p1 = self.score_terms[self.score_p1]
        score_term_p2 = self.score_terms[self.score_p2]
        return f"{score_term_p1}-{score_term_p2}"

    def _winner(self):
        if max(self.score_p1, self.score_p2) >= 4 and abs(self.score_p1 - self.score_p2) > 1:
            return self.player1_name if self.score_p1 > self.score_p2 else self.player2_name
        return None

    def _advantage_phase(self):
        return self.score_p1 >= 4 or self.score_p2 >= 4
