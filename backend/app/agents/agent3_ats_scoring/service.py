from .feature_builder import FeatureBuilder
from .predictor import ATSPredictor
class ATSService:
    @staticmethod
    def score_resume(resume_data, jd_data):
        features = FeatureBuilder.build(
            resume_data,
            jd_data
        )
        ats_score = ATSPredictor.predict(
            features
        )
        return {
            "ats_score": ats_score,
            "matching_skills":
                features["matching_skills"],
            "missing_skills":
                features["missing_skills"]
        }