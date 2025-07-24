import json

def load_case_base(filename="case_base.json"):
    """Loads the case base from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_case_base(case_base, filename="case_base.json"):
    """Saves the case base to a JSON file."""
    with open(filename, "w") as f:
        json.dump(case_base, f, indent=4)

def add_case(case_base, symptoms, disease):
    """Adds a new case to the case base."""
    new_case = {"symptoms": symptoms, "disease": disease}
    case_base.append(new_case)
    return case_base

if __name__ == "__main__":
    case_base = load_case_base()
    save_case_base(case_base)
    print("Initial case base created and saved.")
