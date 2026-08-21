
def generate_letter(template_path,profile,job,matched_skills):
    with open(template_path,"r",encoding="utf-8") as file:
        template = file.read()
    return template.format(
        name=profile["name"],
        companies=job["companies"],
        position=job["position"],

    )
