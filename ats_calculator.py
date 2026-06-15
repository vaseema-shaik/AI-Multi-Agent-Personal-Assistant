def calculate_ats(text):

    skills = [
        "python",
        "machine learning",
        "sql",
        "pandas",
        "numpy"
    ]

    found = []

    for skill in skills:

        if skill.lower() in text.lower():

            found.append(skill)

    score = min(len(found) * 20, 100)

    return score, found