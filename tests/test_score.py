from score import ScoreManager

# Separate users
sm_test_a = ScoreManager()
sm_test_b = ScoreManager()

sm_test_a.increment(2)
sm_test_b.increment(3)

print("Player A:", sm_test_a.get_score())
print("Player B:", sm_test_b.get_score())
