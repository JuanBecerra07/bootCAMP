{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in /home/codespace/.local/lib/python3.12/site-packages (2.1.0)\n",
      "Requirement already satisfied: matplotlib in /home/codespace/.local/lib/python3.12/site-packages (3.9.2)\n",
      "Requirement already satisfied: pillow in /home/codespace/.local/lib/python3.12/site-packages (10.4.0)\n",
      "Requirement already satisfied: sounddevice in /usr/local/python/3.12.1/lib/python3.12/site-packages (0.5.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (1.2.1)\n",
      "Requirement already satisfied: cycler>=0.10 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (0.12.1)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (4.53.1)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (1.4.5)\n",
      "Requirement already satisfied: packaging>=20.0 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (24.1)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (3.1.2)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: CFFI>=1.0 in /home/codespace/.local/lib/python3.12/site-packages (from sounddevice) (1.17.0)\n",
      "Requirement already satisfied: pycparser in /home/codespace/.local/lib/python3.12/site-packages (from CFFI>=1.0->sounddevice) (2.22)\n",
      "Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "PortAudio library not found",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[12], line 9\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcm\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mcm\u001b[39;00m\n\u001b[1;32m      8\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mPIL\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Image, ImageTk\n\u001b[0;32m----> 9\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01msounddevice\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01msd\u001b[39;00m\n\u001b[1;32m     11\u001b[0m \u001b[38;5;66;03m# Para reproducir sonido\u001b[39;00m\n\u001b[1;32m     12\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mplay_sound\u001b[39m():\n",
      "File \u001b[0;32m/usr/local/python/3.12.1/lib/python3.12/site-packages/sounddevice.py:71\u001b[0m\n\u001b[1;32m     69\u001b[0m             \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[1;32m     70\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m---> 71\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mPortAudio library not found\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m     72\u001b[0m     _lib \u001b[38;5;241m=\u001b[39m _ffi\u001b[38;5;241m.\u001b[39mdlopen(_libname)\n\u001b[1;32m     73\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m:\n",
      "\u001b[0;31mOSError\u001b[0m: PortAudio library not found"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "%pip install numpy matplotlib pillow sounddevice\n",
    "\n",
    "import tkinter as tk\n",
    "from tkinter import filedialog\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.cm as cm\n",
    "from PIL import Image, ImageTk\n",
    "import sounddevice as sd\n",
    "\n",
    "# Para reproducir sonido\n",
    "def play_sound():\n",
    "    sd.play(np.random.uniform(-1, 1, 44100), 44100)  # Reproduce un sonido aleatorio\n",
    "\n",
    "class CancerDetectionApp:\n",
    "    def __init__(self, master):\n",
    "        self.master = master\n",
    "        master.title(\"Detección de Cáncer a través de Imágenes\")\n",
    "\n",
    "        self.label = tk.Label(master, text=\"Cargar una imagen:\")\n",
    "        self.label.pack()\n",
    "\n",
    "        self.load_button = tk.Button(master, text=\"Cargar Imagen\", command=self.load_image)\n",
    "        self.load_button.pack()\n",
    "\n",
    "        self.canvas = tk.Canvas(master)\n",
    "        self.canvas.pack()\n",
    "\n",
    "        self.image_path = None\n",
    "\n",
    "    def load_image(self):\n",
    "        self.image_path = filedialog.askopenfilename(title=\"Seleccionar Imagen\", filetypes=[(\"Image files\", \"*.png;*.jpg;*.jpeg\")])\n",
    "        if self.image_path:\n",
    "            self.process_image(self.image_path)\n",
    "\n",
    "    def process_image(self, path):\n",
    "        # Cargar la imagen\n",
    "        image = Image.open(path).convert('L')  # Convertir a escala de grises\n",
    "        image_array = np.array(image)\n",
    "\n",
    "        # Generar el mapa de colores\n",
    "        normed = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))\n",
    "        colored_image = cm.hot(normed)[:, :, :3]  # Usar mapa de colores 'hot'\n",
    "\n",
    "        # Guardar la imagen procesada\n",
    "        plt.imsave(\"colored_image.png\", colored_image)\n",
    "        self.display_image(\"colored_image.png\")\n",
    "\n",
    "    def display_image(self, path):\n",
    "        img = Image.open(path)\n",
    "        img = img.resize((300, 300), Image.ANTIALIAS)\n",
    "        self.tk_image = ImageTk.PhotoImage(img)\n",
    "        self.canvas.create_image(150, 150, image=self.tk_image)\n",
    "\n",
    "        # Reproducir sonido al pasar el mouse\n",
    "        self.canvas.bind(\"<Motion>\", lambda event: play_sound())\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    root = tk.Tk()\n",
    "    app = CancerDetectionApp(root)\n",
    "    root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3698173795.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[13], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    python cancer_detection_app.py\u001b[0m\n\u001b[0m           ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "python cancer_detection_app.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
