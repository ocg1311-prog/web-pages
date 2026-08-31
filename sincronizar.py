import os
import shutil
import subprocess

CARPETA_ESCRITORIO = r"C:\Users\LATITUDE\Desktop\nuevas-webs"
REPOSITORIO_LOCAL = os.getcwd()

def main():
    print("=== INICIANDO SINCRONIZACIÓN MASIVA ===")
    if not os.path.exists(CARPETA_ESCRITORIO):
        os.makedirs(CARPETA_ESCRITORIO)
        print(f"[+] Se creó la carpeta de trabajo en el escritorio: {CARPETA_ESCRITORIO}")
    
    items = os.listdir(CARPETA_ESCRITORIO)
    carpetas = [i for i in items if os.path.isdir(os.path.join(CARPETA_ESCRITORIO, i))]
    
    if not carpetas:
        print("[-] La carpeta 'nuevas-webs' está vacía. Mete ahí las carpetas de tus páginas.")
        return
        
    print(f"[+] Encontradas {len(carpetas)} carpetas de páginas.")
    for p in carpetas:
        orig = os.path.join(CARPETA_ESCRITORIO, p)
        dest = os.path.join(REPOSITORIO_LOCAL, p)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(orig, dest)
        
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-lote: {len(carpetas)} páginas subidas"], check=True)
        print("\n¡Listo, bro! Las páginas se movieron y empaquetaron localmente con éxito.")
    except Exception as e:
        print("[-] Error en Git:", e)

if __name__ == "__main__":
    main()
