from case_base import load_case_base, save_case_base, add_case
from similarity import calculate_similarity

def diagnose(symptoms):
    """Diagnoses a disease based on symptoms using CBR."""
    case_base = load_case_base()
    similarities = []
    for case in case_base:
        similarity = calculate_similarity(symptoms, case["symptoms"])
        similarities.append((similarity, case["disease"]))

    similarities.sort(reverse=True)

    if similarities and similarities[0][0] > 0:
        return similarities[0][1]
    else:
        return "No matching disease found, try to add that disease!"

def learn(symptoms, disease):
    """Adds a new case to the case base."""
    case_base = load_case_base()
    case_base = add_case(case_base, symptoms, disease)
    save_case_base(case_base)
    print(f"\033[94mLearned new case: Symptoms: {symptoms}, Disease: {disease}")

def main():
    while True:
        print("\033[94m1.\033[93m Diagnose Disease")
        print("\033[94m2.\033[93m Learn New Case")
        print("\033[94m3.\033[93m About")
        print("\033[94m4.\033[93m Exit")
        print("--————————————————————————--")
        choice = input("\033[94mEnter your choice:\033[93m ")

        if choice == "1":
            symptoms_input = input("\033[94mEnter symptoms (comma-separated):\033[93m ").split(",")
            symptoms = [s.strip() for s in symptoms_input]
            diagnosis = diagnose(symptoms)
            print("\033[94mDiagnosis:\033[93m", diagnosis)
        elif choice == "2":
            symptoms_input = input("Enter symptoms (comma-separated): ").split(",")
            symptoms = [s.strip() for s in symptoms_input]
            disease = input("Enter disease: ")
            learn(symptoms, disease)
        elif choice == "3":
            print("\033[94mMINI-CBR Diagnosis System developed by \033[93mDΛNGΞROUS ΛNGΞL.\nhttps://linktr.ee/DangerousAngel\n--————————————————————————————————————————————————--")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
