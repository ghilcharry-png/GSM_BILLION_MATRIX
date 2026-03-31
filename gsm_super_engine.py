import json, random, string

def gsm_ultimate_power():
    # هدف الضغطة الواحدة: 10 ملايين حساب (مقسمة لتقليل الضغط)
    batch_size = 1000000 
    iterations = 10
    file_name = 'THE_BILLION_MATRIX.json'
    
    # فتح الملف مرة واحدة للاستمرار في الكتابة (Appending)
    with open(file_name, 'a') as f:
        for i in range(iterations):
            # توليد مليون حساب في الذاكرة دفعة واحدة
            army = [{"u": ''.join(random.choices(string.ascii_letters, k=3)), 
                     "p": ''.join(random.choices(string.digits, k=3))} for _ in range(batch_size)]
            
            # تحويل المليون إلى نصوص سريعة وحفظها
            for soldier in army:
                f.write(json.dumps(soldier) + "\n")
            
            print(f"🚀 GSM Batch {i+1}/10 Deployed (1 Million Added)")

if __name__ == "__main__":
    gsm_ultimate_power()
  
