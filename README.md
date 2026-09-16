# OOP Tkinter Practice

A Python practice project designed to demonstrate core Object-Oriented Programming (OOP) concepts through simple Tkinter-based graphical user interfaces.

This project focuses on practical implementation of:

- Inheritance
- Method Overriding
- Polymorphism
- `super()`
- Single Inheritance
- Hierarchical Inheritance
- Multilevel Inheritance
- Multiple Inheritance
- Basic GUI development using Tkinter
- Git and GitHub workflow

---

## Project Structure

```text
OOP-Tkinter-Practice/
│
├── task1_notification_system.py
├── task2_file_processing.py
├── task3_hospital_staff.py
├── task4_media_streaming.py
├── task5_delivery_management.py
├── README.md
└── .gitignore
```

---

## Task 1 — Notification System

This task demonstrates:

- Hierarchical Inheritance
- Method Overriding
- Runtime Polymorphism

### Classes

- `Notification`
- `EmailNotification`
- `SMSNotification`

The `Notification` class acts as the parent class.

`EmailNotification` and `SMSNotification` inherit from the parent class and override the `send()` method.

The same method name produces different behavior depending on the object being used.

### Example

```text
EmailNotification → Sending Email to user@example.com

SMSNotification → Sending SMS to 0812345678
```

The Tkinter interface allows the user to enter recipient information and display the notification result visually.

---

## Task 2 — File Processing System

This task demonstrates:

- Hierarchical Inheritance
- Method Overriding
- Runtime Polymorphism

### Classes

- `FileProcessor`
- `TextFile`
- `ImageFile`
- `AudioFile`

The `FileProcessor` class acts as the parent class.

The child classes override the `process()` method to provide behavior specific to different file types.

### Example

```text
TextFile  → Processing text file: notes.txt

ImageFile → Processing image file: photo.jpg

AudioFile → Processing audio file: song.mp3
```

The same `process()` method is called for different objects, demonstrating runtime polymorphism.

---

## Task 3 — Hospital Staff Management

This task demonstrates:

- Hierarchical Inheritance
- `super()`
- Method Overriding
- Runtime Polymorphism

### Classes

- `Staff`
- `Doctor`
- `Nurse`
- `Receptionist`

The `Staff` class contains common attributes such as:

- Name
- Staff ID

The child classes inherit these attributes and add their own specific information.

### Child-Class Attributes

- `Doctor` → Specialization
- `Nurse` → Ward
- `Receptionist` → Shift

The child classes use:

```python
super().__init__()
```

to reuse the constructor of the parent class.

Each child class also overrides the `work()` method.

### Example

```text
Dr. Sara is examining patients.

Nurse Ali is caring for patients.

Mia is managing appointments.
```

This demonstrates how the same method can behave differently depending on the object.

---

## Task 4 — Media Streaming System

This task demonstrates:

- Multilevel Inheritance
- `super()`
- Method Overriding
- Runtime Polymorphism

### Inheritance Structure

```text
Media
  ↓
Audio
  ↓
Podcast
```

`Media` is the parent class.

`Audio` inherits from `Media`.

`Podcast` inherits from `Audio`.

This creates a multilevel inheritance structure.

Each class overrides the `play()` method.

### Example

```text
Media
→ Playing media: Python Basics

Audio
→ Playing audio: Relaxing Music - 4 minutes

Podcast
→ Playing podcast: AI Today hosted by John
```

The same `play()` method produces different behavior for different objects.

---

## Task 5 — Delivery Management System

This task demonstrates:

- Single Inheritance
- Multiple Inheritance
- Method Overriding
- Runtime Polymorphism

### Classes

- `Delivery`
- `Trackable`
- `StandardDelivery`
- `ExpressDelivery`

### Single Inheritance

`StandardDelivery` inherits from `Delivery`.

```text
Delivery
   ↓
StandardDelivery
```

### Multiple Inheritance

`ExpressDelivery` inherits from both `Delivery` and `Trackable`.

```text
Delivery       Trackable
     \           /
      \         /
      ExpressDelivery
```

The `deliver()` method is overridden in both delivery classes.

### Example

```text
Standard Delivery
→ Order D101 will arrive at Bangkok in 3-5 days.

Express Delivery
→ Order D102 will arrive at Chiang Mai within 24 hours.

Tracking
→ Tracking order D102...
```

The same `deliver()` method behaves differently depending on the delivery object.

---

## Technologies Used

- Python 3.14
- Tkinter
- PyCharm
- Git
- GitHub

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/rahat-23/OOP-Tkinter-Practice.git
```

### 2. Open the Project Directory

```bash
cd OOP-Tkinter-Practice
```

### 3. Run Any Task

For example:

```bash
python3 task1_notification_system.py
```

or:

```bash
python3 task2_file_processing.py
```

or:

```bash
python3 task3_hospital_staff.py
```

or:

```bash
python3 task4_media_streaming.py
```

or:

```bash
python3 task5_delivery_management.py
```

Each program opens a Tkinter graphical user interface.

---

## Git Workflow Used

This project also demonstrates a basic Git and GitHub development workflow.

```text
Create or Modify Code
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
git push
        ↓
GitHub Repository
```

### Example

```bash
git status
```

Stage the changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Add new OOP practice task"
```

Push the changes to GitHub:

```bash
git push
```

---

## Basic Git Commands Practiced

### Initialize a Git Repository

```bash
git init
```

### Check Repository Status

```bash
git status
```

### Add Files to the Staging Area

```bash
git add .
```

### Create a Commit

```bash
git commit -m "Commit message"
```

### Connect Local Repository to GitHub

```bash
git remote add origin <repository-url>
```

### Push Code to GitHub

```bash
git push
```

### View Commit History

```bash
git log --oneline
```

---

## Learning Outcomes

After completing these exercises, students should be able to:

- Explain the concept of Object-Oriented Programming
- Identify parent and child classes
- Implement inheritance in Python
- Differentiate between different types of inheritance
- Apply single inheritance
- Apply hierarchical inheritance
- Apply multilevel inheritance
- Apply multiple inheritance
- Use `super()` to reuse parent-class constructors
- Implement method overriding
- Understand runtime polymorphism
- Create objects from classes
- Build simple GUI applications using Tkinter
- Organize Python programs into multiple files
- Use Git to track changes
- Create meaningful Git commits
- Push Python projects to GitHub
- Understand the basic Git and GitHub workflow

---

## Educational Purpose

This repository was created for educational and hands-on practice in Object-Oriented Programming using Python.

The exercises gradually combine OOP concepts with Tkinter GUI development so that students can understand how inheritance and polymorphism are applied in practical software applications.

The project also introduces students to Git and GitHub so that they can learn how source code is versioned, maintained, and stored in a remote repository.

---

## Instructor

**Rahat Izhar**

Object-Oriented Programming  
Python, Tkinter, Git and GitHub Practice
