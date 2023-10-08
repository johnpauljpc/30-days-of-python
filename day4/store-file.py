import os

base_dir = os.path.dirname(os.path.abspath(__file__))

files_dir = os.path.join(base_dir, "images")

if not(os.path.exists(files_dir)):
    os.makedirs(files_dir, exist_ok=False)
# os.makedirs(files_dir, exist_ok=True)
my_images = range(0, 10)

for i in my_images:
    fname = f"file-{i}.txt"
    file_path = os.path.join(files_dir, fname)

    if os.path.exists(file_path):
        print(f"skipped {fname}")
        continue

    with open(file_path, "w") as f:
        f.write("The Lord is my Shepherd!")
        f.close()
        print()
        print(f"{fname} created")