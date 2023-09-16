from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = "/content/gdrive/My Drive/"
pdf_folder_path = f'{root_dir}/legal_data/'
print(os.listdir(pdf_folder_path))