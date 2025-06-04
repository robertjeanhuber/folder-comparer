import os
from tkinter import Tk, filedialog, messagebox

def get_folder(prompt_title):
    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)  # Bring dialogs to front

    messagebox.showinfo("Folder Selection", f"📁 Please select {prompt_title}")
    folder = filedialog.askdirectory(title=prompt_title)

    root.destroy()
    return folder

def get_filenames(folder_path):
    try:
        files = [
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')
        ]
        return sorted(files)
    except Exception as e:
        print(f"❌ Error accessing {folder_path}: {e}")
        return None

def compare_folders(folder1, folder2):
    files1 = get_filenames(folder1)
    files2 = get_filenames(folder2)

    if files1 is None or files2 is None:
        return

    print(f"\n📁 {folder1} contains {len(files1)} files")
    print(f"📁 {folder2} contains {len(files2)} files\n")

    if len(files1) != len(files2):
        print("❌ File counts do not match.")
    else:
        print("✅ File counts match.")

    only_in_1 = [f for f in files1 if f not in files2]
    only_in_2 = [f for f in files2 if f not in files1]

    if only_in_1:
        print(f"\n🔺 Files only in {folder1}:")
        for f in only_in_1:
            print(f"  - {f}")

    if only_in_2:
        print(f"\n🔺 Files only in {folder2}:")
        for f in only_in_2:
            print(f"  - {f}")

    if not only_in_1 and not only_in_2:
        print("\n✅ Filenames match exactly (including case).")

if __name__ == "__main__":
    print("📂 Folder Comparison Tool\n")

    folder1 = get_folder("your 1st folder")
    if not folder1:
        print("❌ No folder selected. Exiting.")
        exit()

    folder2 = get_folder("your 2nd folder")
    if not folder2:
        print("❌ No folder selected. Exiting.")
        exit()

    print("\n🔍 Comparing...\n")
    compare_folders(folder1, folder2)