import os
import sys
import subprocess
import re
from google import genai

# Your validated API key
API_KEY = "YOUR_API_KEY_HERE"
client = genai.Client(api_key=API_KEY)

def run_agent_cycle(task_directive):
    target_script = "generated_action.py"
    model_name = 'gemini-2.5-flash'
    
    system_instruction = (
        "You are an autonomous self-programming agent with direct access to the host OS.\n"
        "Write pure, executable Python code to accomplish the user's task.\n"
        "Do not include any explanations, markdown, or chat text outside the code block.\n"
        "Output ONLY raw code inside standard markdown python block delimiters."
    )
    
    attempts = 0
    max_attempts = 3
    error_feedback = ""
    current_prompt = task_directive
    
    while attempts < max_attempts:
        attempts += 1
        if attempts > 1:
            print(f"\n[SELF-REPAIR] Attempt {attempts}/{max_attempts}: Correcting previous errors...")
        else:
            print(f"\n[LOG] Contacting brain for task: '{task_directive}'...")
            
        try:
            # If a previous attempt failed, feed the error back to the brain
            if error_feedback:
                current_prompt = (
                    f"Task: {task_directive}\n\n"
                    f"Your previous code crashed with this error:\n{error_feedback}\n\n"
                    f"Please analyze this error, rewrite the code, and provide the corrected script."
                )
                
            response = client.models.generate_content(
                model=model_name,
                contents=current_prompt,
                config={
                    'system_instruction': system_instruction,
                    'temperature': 0.1
                }
            )
            
            raw_text = response.text if response.text else ""
            
            # Using hex bypass \x60\x60\x60 instead of physical backticks to prevent file cutoffs
            code_match = re.search(r"\x60\x60\x60(?:python)?(.*?)\x60\x60\x60", raw_text, re.DOTALL)
            if code_match:
                generated_code = code_match.group(1).strip()
            else:
                generated_code = raw_text.strip()

            # Write the script to disk
            with open(target_script, "w", encoding="utf-8") as f:
                f.write(generated_code)
                
            print("[LOG] Running generated script locally...")
            result = subprocess.run(
                [sys.executable, target_script],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("[SUCCESS] Task executed cleanly.")
                print(f"[OUTPUT]:\n{result.stdout}")
                return  # Exit cycle successfully
            else:
                print(f"[WARNING] Script execution failed on attempt {attempts}.")
                error_feedback = result.stderr
                print(f"[SYSTEM ERROR ENCOUNTERED]:\n{error_feedback}")
                
        except Exception as e:
            print(f"[ENGINE ERROR] Failed to process cycle: {e}")
            return
            
    print("[FAILURE] Agent could not resolve the task within the maximum repair attempts.")

if __name__ == "__main__":
    print("====================================================")
    print("      CORE AGENT SYSTEM ONLINE (18-MONTH CORE)      ")
    print("   SELF-HEALING SYSTEM: ENABLED  |  OS LINK: TRUE   ")
    print("====================================================")
    
    while True:
        user_input = input("\nEnter a task for the Agent (or type 'exit' to quit): ")
        
        if user_input.strip().lower() == 'exit':
            print("[SYSTEM] Shutting down agent loop. Goodbye, operator.")
            break
            
        if user_input.strip():
            run_agent_cycle(user_input)