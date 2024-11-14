import os
from app import app, UPLOAD_PATH

def find_image(id):
  for file_name in os.listdir(UPLOAD_PATH):
    if f'cape_{id}' in file_name:
      return file_name
  return 'default_image.jpg'

def delete_file(id):
  file = find_image(id)
  if file != 'default_image.jpg':
    os.remove(os.path.join(UPLOAD_PATH, file))