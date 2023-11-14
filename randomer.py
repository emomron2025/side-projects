import random
chars = []
new = []
WORDLIST = r"C:\Users\emomron2025\OneDrive - Loyola Blakefield\ctfs\cognitohazard\randomize\wordlist.txt" #insert wordlist path here
INSERTED = r"C:\Users\emomron2025\OneDrive - Loyola Blakefield\ctfs\cognitohazard\randomize\brainfuck.txt" #insert path to string to be obfuscated
with open(WORDLIST, "r") as f:
    for line in f:
        chars.append(line.strip())
with open(INSERTED, "r") as f:
    orig = f.read()
for char in orig:
    new.append(char)
    for _ in range(random.randint(1, 20)):
        new.append(random.choice(chars))
print("".join(new))
      