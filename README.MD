# 🚧 Beam SFD & BMD Plotter 🚧

### Plot Shear Force and Bending Moment Diagrams for Beams using Python + Flask

🌐 **Live App:** [kushalnavodayan.azurewebsites.net](https://kushalnavodayan.azurewebsites.net/)  
💻 **Source Code:** [GitHub Repository](https://github.com/kushaln3/Beams)



---

## 🚀 Features

- Supports **3 types of beams**:
  - Simply supported beam  
  - Cantilever beam  
  - Mixed beam  

- Load handling:
  - Multiple point forces at any position  
  - Distributed loads with start & end points  
  - Distributed loads can follow equations:
    - Polynomial (`x^2 + 3x + 5`)  
    - Trigonometric (`sin(x)`, `cos(x)`)  
    - Exponential (`exp(x)`)  

- **Unstable systems** are detected and flagged.  
- **Matplotlib** plots for SFD and BMD.  
- Object-oriented design: all classes & methods can be reused in other projects.  

---

## 🛠️ Tech Stack

- **Python** (Core)  
- [Sympy](https://www.sympy.org) – symbolic math  
- [NumPy](https://numpy.org) – numerical computing  
- [Pandas](https://pandas.pydata.org) – tabular handling  
- [Matplotlib](https://matplotlib.org) – plotting  
- [Flask](https://flask.palletsprojects.com) – web framework  
- HTML + CSS + JS – frontend  

---

## ⚡ Installation & Usage

Clone the repo:

```bash
git clone https://github.com/kushaln3/Beams
cd Beams
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run Command-Line Version

```bash
python main.py
```

### Run Web App Locally

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🌐 Online Deployment

The project is deployed on **Microsoft Azure**:  
👉 [Try the Web App](https://kushalnavodayan.azurewebsites.net/)

---

## 🔮 Future Improvements

- More user-friendly input format (e.g., accept `5x` instead of `5*x`)  
- Add a proper unstable system error page in the web version  
- Better frontend UI/UX improvements  
- Add export options (PDF/PNG for diagrams)  

---

## 🙌 Acknowledgements

- Built as part of a **BTech 1st Year MnC Project** at IIT Guwahati.  
- Special thanks to faculty: Tapan K. Mankodi for guidance and encouragement.  
- No AI was used for the **algorithmic/logic part** – ChatGPT was used only for styling (colors, hover animations, buttons).  
- Developed by **Kushal N**

---
<img width="1896" height="876" alt="image" src="https://github.com/user-attachments/assets/e3c5d925-9f8e-4f46-a962-f30fa8fe5559" />
<img width="800" height="550" alt="image" src="https://github.com/user-attachments/assets/635d5734-2215-40c2-b537-1005ddcb00f4" />

<img width="800" height="550" alt="image" src="https://github.com/user-attachments/assets/2a10cec0-26b8-4831-a363-e289c7707c03" />


