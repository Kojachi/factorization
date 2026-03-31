# Integer Factorization Tool

## 🌍 English Version

This project implements various algorithms for the canonical factorization of large integers. It was developed during my undergraduate studies in Cybersecurity to demonstrate efficient computational methods for number theory.

**Supported Algorithms:**
* **Trial Division**: For finding small prime factors.
* **Pollard's rho algorithm**: Using Floyd's cycle-finding modification for improved efficiency.
* **Brillhart-Morrison Algorithm**: A sophisticated continued fraction method for factoring large composite numbers.

**Features:**
* Supports factorization of a single user-input integer.
* **Batch processing**: Capability to factorize multiple numbers stored in a user-specified `.csv` file.
* **Containerization**: Includes a Docker environment for easy deployment and reproduction of results.

---

### 🐳 How to Run via Docker

1. **Prepare the Data Directory:**
   * Create a folder named `nta_cp1` at `C:\Users\{username}\.docker\`
   * Place your `cp1_input.csv` file (containing the integers to be factorized) into this folder.

2. **Pull and Run the Container:**
   Open your terminal and execute the following commands:

   * **Pull the image:**
     ```bash
     docker pull jachiko/nta_cp:cp1
     ```
   * **Run with volume mapping:**
     ```bash
     docker run -it -v "C:\Users\{username}\.docker\nta_cp1":/mnt/mydata jachiko/nta_cp:cp1
     ```

3. **Inside the Application:**
   When the program prompts for the path to the `.csv` file, enter:
   `/mnt/mydata/cp1_input.csv`

---

**Note:** This project was originally developed in an academic context in Ukraine. While the documentation is provided in English, the source code comments and internal UI messages remain in Ukrainian.
