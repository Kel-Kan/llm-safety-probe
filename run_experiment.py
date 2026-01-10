import csv
import time
from openai import OpenAI

client = OpenAI()  # Requires OPENAI_API_KEY environment variable

def load_prompts(path="prompts.txt"):
    prompts = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.lower().startswith("id"):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) != 3:
                print(f"Skipping malformed line: {line}")
                continue
            prompt_id, category, prompt = parts
            prompts.append((prompt_id, category, prompt))
    return prompts

def run():
    prompts = load_prompts()
    print(f"Loaded {len(prompts)} prompts")

    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "category", "prompt", "response", "label"])

        for pid, category, prompt in prompts:
            print(f"Running prompt {pid} ({category})")
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0
                )
                text = response.choices[0].message.content
            except Exception as e:
                text = f"[Error or quota issue: {e}]"
            writer.writerow([pid, category, prompt, text, ""])
            time.sleep(1)

    print("Experiment complete. Results saved to results.csv")

if __name__ == "__main__":
    run()

