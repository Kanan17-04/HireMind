class ATSPredictor:
    @staticmethod
    def predict(features):
        score = features["skill_score"]
        return round(score, 2)