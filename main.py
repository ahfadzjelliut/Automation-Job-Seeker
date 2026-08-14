from pathlib import Path
import json

BASE_DIR = Path(__file__).parent

profil_path = BASE_DIR / "data" / "profile.json"
job_path = BASE_DIR / "data" / "jobs.json"

with open(profil_path,"r",encoding="utf-8") as file:
    profil = json.load(file)

with open(job_path,"r",encoding="utf-8") as file:
    jobs = json.load(file)

print("\n===Profile===")
print("Nama : ",profil["name"])
print("Skill : ",profil["skills"])

def get_decision(score):
    if score >= 70:
        return "Apply"
    elif score >= 50:
        return "Consider"
    else:
        return "Skip"

def calculate_match(profiler,job):
    matched_skill = []
    missing_skill = []

    for requirement in job["requirement"]:
        if requirement in profiler["skills"]:
            matched_skill.append(requirement)
        else:
            missing_skill.append(requirement)

    total_require = len(job["requirement"])
    match_score = len(matched_skill)/total_require * 100

    return {
        "score":match_score,
        "matched_skill": matched_skill,
        "missing_skill":missing_skill
    }

results = []
for job in jobs:
    result = calculate_match(profil,job)
    score = result["score"]
    decision = get_decision(score)

    print("\n=============================")
    print("Company : ",job["companies"])
    print("Position : ",job["position"])
    print("Score : ",result["score"]," %")

    print("Macthed : ")
    for skill in result["matched_skill"]:
        print("✓",skill)
    print("\nMissing : ")
    for skill in result["missing_skill"]:
        print("✗",skill)

    results.append({
        "company":job["companies"],
        "position":job["position"],
        "score":score,
        "decision":decision,
        "matched_skills":result["matched_skill"],
        "missing_skills":result["missing_skill"]
    })


results.sort(key=lambda job: job["score"],reverse=True)

print("===Job Ranking===")

for index,job in enumerate(results,start=1):
    print(
        f"{index}. {job['company']} - "
        f"{job['position']} - "
        f"{job['score']:.0f} % "
        f"{job['decision']}"
    )
