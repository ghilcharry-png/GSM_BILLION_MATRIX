import random
import json
import string
import os

def fast_identity_gen():
    # قوائم لتوليد أسماء تبدو حقيقية ومتنوعة
    prefixes = ["Alpha", "G", "Z", "Neo", "Soldier", "User", "GSA", "GSM"]
    suffixes = ["Matrix", "Hunter", "Prime", "Elite", "Force", "Unit"]
    
    username = f"{random.choice(prefixes)}_{random.choice(suffixes)}_{random.randint(100000, 999999)}"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    
    return {"u": username, "p": password, "s": "Vanguard"}

def build_empire(size=100000): # 100 ألف جندي في كل دورة
    army = [fast_identity_gen() for _ in range(size)]
    
    # حفظ البيانات بتنسيق مضغوط جداً لتوفير المساحة
    with open("THE_BILLION_MATRIX.json", "a") as f:
        for soldier in army:
            f.write(json.dumps(soldier) + "\n")
    print(f"✅ تم سحق الرقم القياسي: +{size} جندي تم تجنيدهم!")

if __name__ == "__main__":
    build_empire()
  
