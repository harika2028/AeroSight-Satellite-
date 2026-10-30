import sqlite3
import datetime
from pathlib import Path

import cv2
import numpy as np
from ultralytics import YOLO

PHOTOS = Path("photos")
OUTPUTS = Path("outputs")
DB = "aerosight.db"


def classify_weather(img):
    """Version 1: simple colour rules. A trained AI classifier comes later."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    total = h.size
    blue = np.sum((h >= 90) & (h <= 130) & (s > 60) & (v > 100)) / total
    white = np.sum((s < 40) & (v > 170)) / total
    dark = np.sum(v < 80) / total

    if dark > 0.45:
        return "dark/stormy", round(min(0.5 + dark, 0.95), 2)
    if white > 0.40:
        return "cloudy", round(min(0.5 + white, 0.95), 2)
    if blue > 0.20:
        return "clear", round(min(0.5 + blue, 0.95), 2)
    return "unclear", 0.40


def main():
    PHOTOS.mkdir(exist_ok=True)
    OUTPUTS.mkdir(exist_ok=True)
    files = [p for p in PHOTOS.iterdir()
                if p.suffix.lower() in {".jpg", ".jpeg", ".jpe", ".png", ".jfif", ".webp", ".bmp"}]
    if not files:
        print("No photos found. Put .jpg or .png files in the photos folder.")
        return

    model = YOLO("yolov8n.pt")  # downloads automatically on first run
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS detections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT, photo TEXT, weather TEXT,
        weather_conf REAL, objects TEXT)""")

    for p in files:
        img = cv2.imread(str(p))
        if img is None:
            print(f"Skipped (cannot read): {p.name}")
            continue

        weather, conf = classify_weather(img)
        result = model(img, verbose=False)[0]
        names = [result.names[int(c)] for c in result.boxes.cls]
        objects = ", ".join(sorted(set(names))) or "none"

        con.execute(
            "INSERT INTO detections (time, photo, weather, weather_conf, objects) "
            "VALUES (?, ?, ?, ?, ?)",
            (datetime.datetime.now().isoformat(timespec="seconds"),
             p.name, weather, conf, objects))
        result.save(filename=str(OUTPUTS / p.name))
        print(f"{p.name}: {weather} ({conf:.0%}) | objects: {objects}")

    con.commit()
    con.close()
    print("Done. Results saved in aerosight.db and the outputs folder.")


if __name__ == "__main__":
    main()