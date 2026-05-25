 I’m a high schooler at an offline boarding school. I have until June 5th (end of break) to build a self-healing AI agent. This is my first big project, hope you all will support! 🚀

Hey ,

I’m a high school student at a boarding school where internet access is strictly prohibited. No phones, no Wi-Fi, nothing. 

Right now, I am on summer vacation, but I have a hard deadline: I go back to school on June 5th. This is my very first big programming project, and I've decided to commit to an 18-month roadmap to build a fully localized, offline, autonomous AI agent with direct system access and physical hardware safeguards (like a USB kill switch). Because I go completely offline on June 5th, I'll be coding like crazy and posting regular, rapid updates until then. I really hope you all will support me on this journey!

Today was Day 1, and against all odds, we got our persistent, self-healing loop running on my 4GB RAM laptop!

---

### 🔥 What is CoreAgent?
It’s a persistent Python program running in my terminal. I type a natural language command, it contacts the Gemini 2.5 API, writes the code, saves it as generated_action.py, executes it directly on my system, and prints the result. 

Instead of turning off after one run, it stays awake indefinitely waiting for commands.

---

### 🛠️ The Self-Repairing Loop
If the code crashes, the agent takes the command line error, feeds it back to the brain, and automatically patches its own code up to 3 times before asking me for help!

---

### 🗓️ The 18-Month Battle Plan
Because this is a long-term project, we are taking it step-by-step:
* Phase 1 (Now - June 5): Master the Windows environment, build a local SQLite database log, and implement multi-step task planning.
* Phase 2 (Next Vacation): Migrate completely to a minimal Linux partition to save RAM and get raw shell integration.
* Phase 3: Build a Physical Hardware Kill Switch—a background service that instantly shuts down the host OS if my physical authorization USB key is pulled out.
* Phase 4: Ditch the cloud API entirely. Get a dedicated GPU machine and run a fully quantized, open-weights LLM completely offline.

---

### 🤝 Join the Journey & Help Me Out!
I have exactly 10 days of internet access left before I go back to the offline boarding school vault. I will be coding and posting updates here daily until June 5th!

I’ve uploaded our raw, open-source script to GitHub. Since this is my first major project, I would love your feedback, tips on agent logic, or suggestions on how to improve our system!

* GitHub Repository: https://github.com/Saptak1234/CoreAgent
* Follow along: Leave a comment, check out the repo, and let's see what we can build before my internet gets cut!
