class FeatureBuilder:
    @staticmethod
    def build(resume_data, jd_data):
        resume_skills = set(
            s.lower()
            for s in resume_data.get("skills", [])
        )
        jd_skills = set(
            s.lower()
            for s in jd_data.get("required_skills", [])
        )
        matching_skills = list(
            resume_skills & jd_skills
        )
        missing_skills = list(
            jd_skills - resume_skills
        )
        skill_score = 0
        if jd_skills:
            skill_score = (
                len(matching_skills)
                / len(jd_skills)
            ) * 100
        return {
            "skill_score": skill_score,
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
        }