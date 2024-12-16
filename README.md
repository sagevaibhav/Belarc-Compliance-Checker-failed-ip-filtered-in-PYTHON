# Belarc Compliance Checker

✨ **Made with ❤️ by Vaibhav Mishra** ✨  

## Overview  
Belarc Compliance Checker ek Python-based tool hai jo automate karta hai Belarc Advisor ke HTML reports ka compliance analysis. Aap ek specific sentence search kar sakte ho, aur tool compliance images (`yes.gif` ya `no.gif`) ke basis par pass/fail compliance status detect karta hai. Yeh GUI `Tkinter` ke saath banaya gaya hai jo ise use karne mein super simple banata hai.

---

## Features  
- **Directory Selection:** Kisi bhi root directory ko browse aur select karo jisme Belarc HTML reports ho.  
- **Search Sentence:** Apna desired text input karo jo aapko search karna hai.  
- **Compliance Check:** Compliance status images ke basis par detect karo (`yes.gif` ya `no.gif`).  
- **IPv4 Address Filter:** Sirf fail hone wale files ke results ko IPv4 address ke sath display karta hai.  
- **Creative Output:** Results ko ek personal touch ke sath dikhata hai. ✨  

---

## How to Use  

1. **Clone Repository karo:**  
   ```
   git clone https://github.com/sagevaibhav/belarc-compliance-checker.git
   cd belarc-compliance-checker

2. **Dependencies Install karo:**  
   Make sure Python (3.8 ya uske upar) installed ho aur dependencies install karo:  
   ```
   pip install beautifulsoup4
   ```

3. **Tool Run karo:**  
   Script ko Python ke through run karo:  
   ```
   python belarc_compliance_checker.py
   ```

4. **GUI Follow karo:**  
   - Search sentence dalke directory select karo.  
   - `.html` reports ko analyze karo.  
   - Output section mein compliance results dekho.  

---

## GUI Screenshot  
![image](https://github.com/user-attachments/assets/e1197d61-bb58-430f-9ebb-1887626dd379)


---

## Requirements  
- Python 3.8 ya uske upar  
- Libraries:
  - `tkinter` (Python ke saath pre-installed aata hai)
  - `beautifulsoup4`
  - `re`

---

## Future Enhancements  
- Results ko CSV file mein export karne ka option.  
- Compliance reporting ko aur detailed banana additional image checks ke sath.  
- IPv6 support add karna.  

---

## Contributing  
Agar aapko lagta hai ki kuch features ya improvements add hone chahiye, toh feel free contribute karne ke liye. Pull request banaiye aur submit kariye.

---

## License  
Yeh project MIT License ke under open-source hai.  

---

## Contact  
Suggestions aur queries ke liye mujhe contact karein: **sagevaibhav555@gmail.com**  
Ya phir LinkedIn pe connect ho: [Vaibhav Mishra](https://www.linkedin.com/in/vaibhav555/)  
```
