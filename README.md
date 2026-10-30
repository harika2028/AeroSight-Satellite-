🛰️ AeroSight

Satellite Weather Detection & Orbital Object Tracking

<p align="center">
  <img src="assets/aerosight-cover.png" alt="AeroSight CubeSat above Earth" width="800"/>
</p><p align="center">
  <b>A Software-Only 3U CubeSat Digital Twin</b><br/>
  Exploring AI, satellite electronics, orbital simulation, and digital design with open-source tools.
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLOv8-111F68?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Verilog-Digital_Design-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/KiCad-PCB_Design-314CB0?style=for-the-badge&logo=kicad&logoColor=white"/>
</p><p align="center">
  <img src="https://img.shields.io/badge/Project-Engineering_Simulation-00A86B?style=flat-square"/>
  <img src="https://img.shields.io/badge/Hardware-Not_Required-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Prototype-orange?style=flat-square"/>
</p>---

🌍 Project Overview

AeroSight is a software-only digital twin of a 3U CubeSat (10 × 10 × 30 cm) designed to demonstrate how satellite subsystems can work together in a simulated environment.

It combines AI-based image analysis, orbital mechanics, satellite structure modeling, PCB design, antenna analysis, and Verilog-based digital logic. The system includes a Python processing pipeline, SQLite database, interactive dashboard, and 3D satellite visualization.

«💡 Mission: Explore the design and integration of a satellite system using a laptop and free, open-source engineering tools.»

🪐 Project Gallery

Add your actual project screenshots to the "assets/" folder and update these paths.

🛰️ Satellite Model| 🌎 Orbital Simulation
"3D Satellite" (assets/satellite-model.png)| "Orbit Map" (assets/orbit-map.png)
3U CubeSat structure| Simulated ground track

🤖 AI Detection| 📊 Dashboard
"AI Detection" (assets/object-detection.png)| "Dashboard" (assets/dashboard.png)
Object detection results| Analysis and orbital data

🔌 Power PCB| 💻 Digital Chip
"PCB Design" (assets/power-pcb.png)| "Verilog Waveform" (assets/beacon-waveform.png)
KiCad power board| Beacon timer simulation

✨ Key Features

- 🌦️ Weather Classification — Estimates weather conditions using image color-based rules.
- 🎯 Object Detection — Uses pretrained YOLOv8n to identify objects in images.
- 🗃️ Data Management — Records analysis results in SQLite.
- 📈 Interactive Dashboard — Displays metrics, charts, annotated images, and orbital tracks.
- 🌎 Orbit Simulation — Models a 500 km sun-synchronous orbit.
- 🧩 Satellite CAD Model — Designs the 3U satellite structure in FreeCAD.
- 🔋 Power Electronics — Designs and verifies a solar-input battery charging and regulation circuit.
- 📡 Antenna Analysis — Calculates the theoretical radiation pattern of a 437 MHz UHF dipole.
- ⚙️ Digital Logic — Implements and simulates a beacon timer using Verilog.
- 🎨 3D Visualization — Renders the satellite above Earth using Blender and Three.js.

🏗️ System Architecture

                   🛰️ AEROSIGHT
                        |
       +----------------+----------------+
       |                |                |
   🤖 AI Payload    🌎 Orbit Model   🔧 Satellite Design
       |                |                |
   Image Analysis    Ground Track     CAD / PCB / Antenna
       |                |                |
       +----------------+----------------+
                        |
                🐍 Python Processing
                        |
                  🗃️ SQLite Database
                        |
                 📊 Streamlit Dashboard
                        |
                 🎨 3D Visualization

🛠️ Technology Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/FreeCAD-CAD-418FDE?style=flat-square"/>
  <img src="https://img.shields.io/badge/KiCad-PCB-314CB0?style=flat-square&logo=kicad&logoColor=white"/>
  <img src="https://img.shields.io/badge/Verilog-HDL-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Yosys-Logic_Synthesis-7952B3?style=flat-square"/>
  <img src="https://img.shields.io/badge/Blender-3D_Design-E87D0D?style=flat-square&logo=blender&logoColor=white"/>
  <img src="https://img.shields.io/badge/Three.js-3D_Web-black?style=flat-square&logo=threedotjs&logoColor=white"/>
</p>Subsystem| Technologies
AI and image processing| Python, OpenCV, YOLOv8, PyTorch
Data and dashboard| SQLite, Pandas, Streamlit
Orbital simulation| Python, NumPy, Matplotlib
Satellite structure| FreeCAD
Power electronics| KiCad
Digital chip| Verilog, Icarus Verilog, Verilator, GTKWave, Yosys
Visualization| Blender, Three.js

🔄 How It Works

1. 📷 Input images are placed in the photos directory.
2. 🤖 The software estimates weather conditions and detects recognizable objects.
3. 🗃️ Results are stored in SQLite, and annotated images are saved.
4. 🌎 An orbital simulation generates satellite latitude and longitude coordinates.
5. 📊 The dashboard presents analysis results and the simulated ground track.
6. 🔧 Separate engineering modules model the satellite structure, PCB, antenna, and beacon timer.
7. 🎨 Blender and Three.js bring the virtual satellite and Earth into a visual overview.

📊 Simulation Results

Parameter| Result
Satellite size| 10 × 10 × 30 cm
Orbital altitude| 500 km
Orbital inclination| 97.4°
Orbital period| Approximately 94.6 minutes
Antenna frequency| 437 MHz
Beacon timer| Pulse every 8 clock cycles in simulation
Logic synthesis| 94 cells reported by Yosys
PCB verification| 0 DRC errors, 0 warnings, 0 unconnected items

Three test photographs were processed. Object detections were recorded for two images, while weather labels were generated for all three. These are initial simulation results, not evidence of flight performance.

📁 Repository Structure

AeroSight/
├── assets/                 # Project screenshots and images
├── photos/                 # Input photographs
├── outputs/                # Annotated images
├── chip/
│   ├── beacon.v            # Verilog timer
│   └── tb.v                # Testbench
├── detect.py               # Image processing pipeline
├── dashboard.py            # Streamlit dashboard
├── orbit.py                # Orbital simulation
├── antenna.py              # Antenna analysis
├── freecad_body.py         # Satellite CAD model
├── requirements.txt        # Python dependencies
└── README.md

Adjust the structure to match the files actually present in your repository.

🚀 Getting Started

Prerequisites

- Windows 11 and Python 3.12
- Visual Studio Code
- Python libraries: OpenCV, Ultralytics, PyTorch, NumPy, Pandas, Streamlit, and Matplotlib
- FreeCAD, KiCad, and Blender for the engineering models
- WSL2 Ubuntu and digital design tools for the Verilog workflow

Installation

git clone YOUR_REPOSITORY_URL
cd AeroSight

python -m venv venv

Activate the environment on Windows:

.\venv\Scripts\Activate.ps1

Install the Python dependencies:

pip install opencv-python ultralytics pandas streamlit matplotlib numpy
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

Run the image-processing pipeline

python detect.py

Launch the dashboard

streamlit run dashboard.py

Generate the orbit data

python orbit.py

Generate the antenna pattern

python antenna.py

The commands assume the files and module names match your local implementation. Add any missing setup steps needed by your actual repository.

⚠️ Limitations

- The satellite is a software-only digital twin.
- Weather classification uses color-based rules rather than a trained weather model.
- The orbit is idealized and does not include all real-world orbital perturbations.
- Antenna results are theoretical.
- The beacon chip has been simulated and synthesized but has not been fabricated or physically laid out.

🔮 Future Enhancements

- 🌦️ Train a weather classifier on real satellite imagery.
- 🛰️ Integrate real TLE-based orbit tracking.
- 🎯 Track objects across successive images.
- ⚙️ Explore RTL-to-GDSII implementation using OpenLane.
- 📡 Perform full-wave antenna simulation using openEMS.
- 🧠 Explore RISC-V-based onboard processing.
- 🌐 Add a ground-station communication workflow.

👩‍💻 Author

Niharika Yarasu
Electronics and Communication Engineering Graduate

- 💻 "GitHub" (https://github.com/harika2028)
- 🌐 "Portfolio" (https://harika2028.github.io/niha-portfolio/)
- 🔗 "LinkedIn" (https://www.linkedin.com/in/yarasu-neharika/)

🙏 Acknowledgements

Thanks to the developers and communities behind Python, OpenCV, PyTorch, Ultralytics, Streamlit, SQLite, FreeCAD, KiCad, Icarus Verilog, Verilator, GTKWave, Yosys, Blender, and Three.js.

---

<p align="center">
  <b>🛰️ AeroSight — Learned it. Built it. Did it.</b><br/>
  <i>Dreams don’t need a lab to start.</i>
</p># AeroSight-Satellite-
Developed AeroSight, a software-only 3U CubeSat digital twin integrating AI-based weather classification, YOLOv8 object detection, orbital simulation, satellite structure modeling, PCB design, and Verilog-based digital chip simulation, with an interactive dashboard and 3D visualization using open-source tools.
