import re

def extract_session_id(session_str: str) -> str:
    match = re.search(r"/sessions/([^/]+)/contexts/", session_str)
    if match:
        print(type(match.group(1)))
        return match.group(1)
    return ""

def get_str_from_food_dict(food_dict : dict):
    return ", ".join([f"{int(value)} {key}" for key,value in food_dict.items()])

if __name__ == "__main__":
    print(extract_session_id("projects/gen-lang-client-0687868341/agent/sessions/e1df0853-68bf-92f4-45c8-f2c59017fe34/contexts/ongoing_order"))



