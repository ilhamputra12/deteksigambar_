

# Fungsi untuk mendeteksi bentuk
def detect_shapes(image):
    shapes = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Konversi ke grayscale
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  # Threshold untuk deteksi tepi
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Approximate kontur untuk mendeteksi bentuk
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
        x, y, w, h = cv2.boundingRect(approx)
        
        if len(approx) == 3:
            shapes.append(("Segitiga", (x, y, w, h)))
            cv2.putText(image, "Segitiga", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        elif len(approx) == 4:
            aspect_ratio = w / float(h)
            if 0.9 <= aspect_ratio <= 1.1:
                shapes.append(("Persegi", (x, y, w, h)))
                cv2.putText(image, "Persegi", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            else:
                shapes.append(("Persegi Panjang", (x, y, w, h)))
                cv2.putText(image, "Persegi Panjang", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        elif len(approx) > 10:
            shapes.append(("Lingkaran", (x, y, w, h)))
            cv2.putText(image, "Lingkaran", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            shapes.append(("Lainnya", (x, y, w, h)))
            cv2.putText(image, "Lainnya", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    return image, shapes

# Langkah 3: Unggah file gambar
from google.colab import files
uploaded = files.upload()

# Langkah 4: Baca dan deteksi bentuk dari gambar
for filename in uploaded.keys():
    image = cv2.imread(filename)
    image = cv2.resize(image, (600, 400))  # Ubah ukuran gambar agar mudah dilihat
    result_image, detected_shapes = detect_shapes(image)
    
    # Tampilkan hasil deteksi
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Hasil Deteksi Bentuk")
    plt.show()
    
    # Print bentuk yang terdeteksi
    print("Bentuk yang terdeteksi:")
    for shape, (x, y, w, h) in detected_shapes:
        print(f"- {shape} di koordinat x: {x}, y: {y}, lebar: {w}, tinggi: {h}")
