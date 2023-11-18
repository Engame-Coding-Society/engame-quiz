class ScoreManager:
    """
    Manages the scores of every player. Usage:
     * Create a new score manager
     * Increment score using `increment()`
     * Get their current score with `get_score()`
    """

    def __init__(self):
        """
        Creates a score manager for a player
        """
        self.score = 0

    def increment(self, i: int = 1):
        """
        Increases the current player's score by a given amount, one by default
        :param i: Amount to be increased by
        """
        self.score += i

    def get_score(self) -> int:
        """
        Get the score of the current player
        :return: Current score
        """
        return self.score
