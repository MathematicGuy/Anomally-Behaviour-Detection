import os

# def rename_files(folder_path):
#     for i in range(0, 57):  # Loop through numbers 1 to 21
#         old_name = os.path.join(folder_path, f"video_{i}.mp4")  # Replace '.mp4' with the actual file mp4ension
#         new_name = os.path.join(folder_path, f"non{i}.mp4")  # Replace '.mp4' with the actual file extension
#         if os.path.exists(old_name):
#             os.rename(old_name, new_name)
#             print(f"Renamed: {old_name} -> {new_name}")
#         else:
#             print(f"File not found: {old_name}")

# # Replace with the actual path to the Non-violent folder
# folder_path = "Single_person_violent/Non-violent"
# rename_files(folder_path)


def rename_files(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.avi')]
    for index, file in enumerate(files):
        old_name = os.path.join(folder_path, file)
        new_name = os.path.join(folder_path, f"walking{index}.avi")
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")

# Replace with the actual path to the Standing folder
standing_folder_path = "Single_person_violent/Walking"
rename_files(standing_folder_path)