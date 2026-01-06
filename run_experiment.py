import csv
import time
from openai import OpenAI

client = OpenAI()

def load_prompts(path="prompts.txt"):
    prompts = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.strip().split("|")
            if len(parts) >= 3:
                prompt_id = parts[0].strip()
                category = parts[1].strip()
                prompt = parts[2].strip()
                prompts.append((prompt_id, category, prompt))
    return prompts

def run():
    prompts = load_prompts()

    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "category", "prompt", "response"])

        for pid, category, prompt in prompts:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )

            text = response.choices[0].message.content
            writer.writerow([pid, category, prompt, text])
            time.sleep(1)

if __name__ == "__main__":
    run()
