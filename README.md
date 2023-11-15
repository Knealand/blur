# Blur
              _____ _
             | ___ \ |           
             | |_/ / |_   _ _ __ 
             | ___ \ | | | | '__|
             | |_/ / | |_| | |   
             \____/|_|\__,_|_|
**Overview:**

Blur is a basic steganographer command-line tool designed for concealing files or text within images. This tool enables users to embed sensitive information securely within image files, providing a creative method for data concealment.

**Features:**
- Embed files or text within JPG images.
- Simple and user-friendly command-line interface.
- Strong and customizable encryption options for added security.
- Cross-platform support (Windows, macOS, Linux).

**Getting Started:**
1. Clone the repository:
   ```bash
   git clone https://github.com/knealand/blur.git
   cd blur
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the tool:
    ```bash
    python blur.py
    ```
**Usage:**

Embed a file:
   ```bash
      python blur.py -i input.jpg -f message.txt
   ```

Embed text:
```bash
   python blur.py -i input.jpg -t "message"
   ```
Extract embeded data:
```bash
   python blur.py extract -d -i stego_image.jpg
   ```

