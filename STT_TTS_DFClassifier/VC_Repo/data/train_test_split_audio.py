import os
import shutil
import random
os.chdir(os.path.join(os.getcwd(), "data\\raw\\cv_delta"))
# Assuming the human and ai folders are in the current working directory
human_dir = "clips"
ai_dir = "AIclips"

# Create the test and train folders if they don't exist
test_dir = "test"
train_dir = "train"
os.makedirs(test_dir, exist_ok=True)
os.makedirs(train_dir, exist_ok=True)

# Create subfolders for human and ai in test and train folders
test_human_dir = os.path.join(test_dir, human_dir)
test_ai_dir = os.path.join(test_dir, ai_dir)
train_human_dir = os.path.join(train_dir, human_dir)
train_ai_dir = os.path.join(train_dir, ai_dir)
os.makedirs(test_human_dir, exist_ok=True)
os.makedirs(test_ai_dir, exist_ok=True)
os.makedirs(train_human_dir, exist_ok=True)
os.makedirs(train_ai_dir, exist_ok=True)

# Define the train/test split ratio
split_ratio = 0.8

# Get the list of image files in human and ai folders
human_files = [f for f in os.listdir(human_dir) if f.endswith(".wav") or f.endswith(".mp3")]
ai_files = [f for f in os.listdir(ai_dir) if f.endswith(".wav") or f.endswith(".mp3")]

# Shuffle the files randomly
random.shuffle(human_files)
random.shuffle(ai_files)

# Split the files into train and test sets based on the split ratio
human_train_size = int(len(human_files) * split_ratio)
ai_train_size = int(len(ai_files) * split_ratio)

human_train_files = human_files[:human_train_size]
human_test_files = human_files[human_train_size:]
ai_train_files = ai_files[:ai_train_size]
ai_test_files = ai_files[ai_train_size:]

# Copy the files to the corresponding subfolders
for f in human_train_files:
    shutil.copy(os.path.join(human_dir, f), train_human_dir)

for f in human_test_files:
    shutil.copy(os.path.join(human_dir, f), test_human_dir)

for f in ai_train_files:
    shutil.copy(os.path.join(ai_dir, f), train_ai_dir)

for f in ai_test_files:
    shutil.copy(os.path.join(ai_dir, f), test_ai_dir)

print("Done!")