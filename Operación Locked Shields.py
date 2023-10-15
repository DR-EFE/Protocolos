#este código comprime una carpeta especificada en un archivo ZIP y protege ese archivo con una contraseña
 #proporcionada. La carpeta comprimida se guarda en la ubicación especificada en output_zip_path.

import zipfile
import os

def zip_folder_with_password(folder_path, output_path, password):
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname=arcname)

        # Agregar contraseña al archivo zip
        with open(output_path, 'rb+') as zipf:
            zipf.write(password.encode())

        print(f"Carpeta comprimida con contrasena: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_to_compress = r"C:\Users\PC\OneDrive\Documentos\Pizz"
    output_zip_path = r"C:\Users\PC\OneDrive\Documentos\Comprimidos\archivo.zip"
    password = "12233"

    zip_folder_with_password(folder_to_compress, output_zip_path, password)
