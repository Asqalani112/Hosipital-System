# 🏥 Hospital Management System

A simple console-based Hospital Management System built using **Python**.  
This system simulates patient queuing and prioritization across multiple medical specializations.

## 📋 Features

- ➕ **Add a new patient** to a specialization with prioritization:  
  - 0 → Normal  
  - 1 → Urgent  
  - 2 → Super Urgent
- 📤 **Get next patient** by specialization (FIFO with priority-based ordering).
- ❌ **Remove a leaving patient** by name and specialization.
- 🧪 **Add dummy data** to test the system under different scenarios.

## 🧠 Concepts Used

- Queues with priority-based insertion.
- Simulation of real-world queue systems in hospitals.
- List operations and conditional logic.
- Modular code for testing and extension.

## 🧱 Project Structure

```
├── hospital_system.py        # Main Python script (your implementation)
└── README.md                 # Project documentation (this file)
```

## 🏥 System Rules

- There are **20 specializations** (e.g. Children, Surgery).
- Each specialization can have **up to 10 patients** in the queue.
- Patients are categorized by **status**:
  - `0 = Normal`: added at the end.
  - `1 = Urgent`: added before normal patients.
  - `2 = Super Urgent`: added before urgent and normal patients.
- When queue is full: system **rejects** adding new patients to that specialization.

## 🔍 Example Functionalities

```text
1. Add a new patient
2. Get next patient for a doctor
3. Remove a patient who left
4. Print all patients
5. Add dummy data
6. Exit
```

## 🧪 Testing Strategy

- Dummy data added to simulate:
  - Full queues.
  - Queues with mixed status types.
  - Removal edge cases.
- Manual input testing for every scenario.

---

> **"Acquire knowledge and impart it to the people."**  
> **"Seek knowledge from the cradle to the grave."**

---

## 👤 Developed for educational purposes  
by **Mostafa S. Ibrahim**  
AI & CV Researcher | PhD - Simon Fraser University  
BSc/MSc - Cairo University | ICPC World Finalist
