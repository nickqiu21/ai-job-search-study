import csv
import random

# how many agents you want
N = 150

output_file = "simulated_ai_survey_agents.csv"

ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
age_weights = [8, 12, 14, 14, 14, 12, 8, 4, 2, 2, 2]  # skewed toward 19–24

genders = ["Female", "Male", "Nonbinary"]
gender_weights = [0.47, 0.47, 0.06]

industries = ["Tech", "Finance", "Consulting", "Marketing", "Healthcare", "Education"]

ai_usage_levels = ["Rarely", "Sometimes", "Often", "Very often"]

def pick_age():
    return random.choices(ages, weights=age_weights)[0]

def education_from_age(age):
    if age <= 22:
        return "Bachelor's (in progress)"
    elif age <= 24:
        return random.choice(["Bachelor's (in progress)", "Bachelor's"])
    else:
        return random.choice(["Bachelor's", "Master's"])

def years_experience_from_age(age):
    if age <= 20:
        return 0
    elif age <= 22:
        return random.choice([0, 1])
    elif age <= 24:
        return random.choice([1, 2])
    else:
        return random.choice([2, 3, 4, 5])

def employment_status(age):
    if age <= 22:
        return random.choices(
            ["Actively applying", "Passively looking", "Already employed"],
            weights=[0.60, 0.20, 0.20]
        )[0]
    else:
        return random.choices(
            ["Actively applying", "Passively looking", "Already employed"],
            weights=[0.40, 0.25, 0.35]
        )[0]

def ai_usage_from_age(age):
    if age <= 22:
        return random.choices(ai_usage_levels, weights=[0.05, 0.20, 0.35, 0.40])[0]
    elif age <= 25:
        return random.choices(ai_usage_levels, weights=[0.10, 0.30, 0.35, 0.25])[0]
    else:
        return random.choices(ai_usage_levels, weights=[0.20, 0.40, 0.30, 0.10])[0]

def trust_from_usage(usage):
    if usage == "Very often":
        return random.choice([4, 5])
    elif usage == "Often":
        return random.choice([3, 4])
    elif usage == "Sometimes":
        return random.choice([2, 3])
    else:
        return random.choice([1, 2])

def fairness_from_trust(trust):
    if trust >= 5:
        return random.choice([4, 5])
    elif trust == 4:
        return random.choice([3, 4])
    elif trust == 3:
        return random.choice([2, 3])
    else:
        return random.choice([1, 2])

def confidence_from_status(status):
    if status == "Already employed":
        return random.choice([4, 5])
    elif status == "Passively looking":
        return random.choice([3, 4])
    else:
        return random.choice([2, 3, 4])

def get_friend_size_from_age(age):
    if age <= 22:
        return random.choice([5, 10, 15, 20])
    elif age <= 25:
        return random.choice([3, 7, 12, 18])
    else:
        return random.choice([1, 5, 10, 15])

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "agent_id",
        "age",
        "gender",
        "education_level",
        "years_experience",
        "industry",
        "employment_status",
        "ai_usage_frequency",
        "trust_in_ai_tools",
        "perceived_fairness_of_ai_hiring",
        "confidence_in_getting_interview",
        "connection_size"
    ])

    for i in range(1, N + 1):
        age = pick_age()
        gender = random.choices(genders, weights=gender_weights)[0]
        education = education_from_age(age)
        experience = years_experience_from_age(age)
        industry = random.choice(industries)
        status = employment_status(age)
        usage = ai_usage_from_age(age)
        trust = trust_from_usage(usage)
        fairness = fairness_from_trust(trust)
        confidence = confidence_from_status(status)
        friend_group = get_friend_size_from_age(age)
        
        writer.writerow([
            f"A{str(i).zfill(3)}",
            age,
            gender,
            education,
            experience,
            industry,
            status,
            usage,
            trust,
            fairness,
            confidence,
            friend_group
        ])

print(f"CSV generated successfully: {output_file}")