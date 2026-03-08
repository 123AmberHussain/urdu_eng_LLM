 # Urdu-English LLM - Development Journal

 ## Project Goal
 This LLM will translate between English and Urdu seemlessly, learning the "flavor" or essense of each language so that it can provide sophisticated translations, understanding nuance, colloquilisms, and cultural references that are often lost in translation. 

 ## Entry 1 - February 14, 2026
 Today I set up the virtual environment, the github repository, and created a python application to check if my PC has a GPU, and to find it CUDA version. 
 ### Things I learnt
 **Setting up a Virtual Environment**

 A virtual environment is an isolated environment to run and test python projects. 
 Allows coder to manage project specific dependencies without interfering with other projects or the original python installation. Its like a container, where each:
 * Has its own Python interpreter
 * Has its own set of installed packages
 * Is isolated from other virtual environments
 * Can have different versions of the same package

 Using virtual environments is important because:
 * It prevents package version conflicts between projects
* Makes projects more portable and reproducible
* Keeps your system Python installation clean
* Allows testing with different Python versions

***Setting up a virtual environment***

Creating a virtual environment named project1, first open cmd prompt

Command: python -m venv project1
- This sets up the venv and creates a folder called project1 with subfolders.

To activate the virtual environment:

Command: project1\Scripts\activate.bat
- When I ran this command, it did not work. I later found out it was because I was working in powershell rather than the command prompt. Then it worked

**Installing Libraries**
- pip install torch transformers

**Hardware check**

Created the check_system.py file, which checked if my PC has the nvidia gpu. 
At first it said the GPU was not found, which might've been just because the pop install torch used the CPU version to save space.
I typed this command to see if the systems were working

Command: nvidia-smi

Then i needed to uninstall the slow version
- pip uninstall torch torchvision torchaudio -y

uninstalls the CPU-only version of the pytorch library previously installed

update my pip because i have python 3.13

- python.exe -m pip install --upgrade pip
- pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124


Then i ran the check_system.py file again, and it worked.

**Git Repo**

I setup the .gitignore at the start before the venv. This just tells Git to ignore the venv folder and large data files.

Commands:

- git init
- echo "venv/" > .gitignore
- echo "*.pyc" >> .gitignore

To add all the code to a repository, I created a repo on github.com, and in the cmd prompt here, i gave the commands:
- git add .
- git commit -m "  "
- git remote add origin https://github.com/YOUR_USERNAME/urdu_english_LLM.git
- git branch -M main
- git push -u origin main

Once this was set up, I could commit to the repo whenever i want like this
- git add .
- git commit -m "  "
- git push

OR when wanting to make sure everything is up to date:
- git push -u origin main

## Entry 2 - March 7, 2026
Today, I started with building the tokenizer. 

### train_tokenizer.py ###
This file was set up as a test to see how the tokenizer chunks the words differently.

Next I set up the NOTES.md and filled it with my record of things I have done and researched and useful commands for me to go back to. 

### Things I learnt ###
**tokenizers by HuggingFace**
It's the biggest open source AI company. 
- Tokenizers library: tool so people don't have to write common AI components from scratch. To note, a tokenizer converts text to numbers and back to text again.

- The tokenizer trained today only had 4 sentences, so the BPE (Byte-Pair_encoding), did not learn much. It fell back to single characters (ex: "s", "o", "u", "l") because it did not have enough examples to see letters pair together. 
    - BPE looks at individual characters and asks which 2 chunks appear together most often and merges them. This is repeated thousands of times.

### Plans ###
I'm thinking of monitoring the loss curves, hardware health, and language quality as it goes. I haven't decided on how and when to do that but I would like to be able to moniter the behaviour of the LLM.