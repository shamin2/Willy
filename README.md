# 🐱 Willy the Virtual Cat

Willy, a virtual representation of my beloved white cat, offers a unique interactive experience designed to simulate the joys and responsibilities of pet ownership. Developed in Python, this project allows users to engage with Willy through a variety of activities that reflect real-life pet care dynamics. Inspired by my own experiences and motivated by a desire to share the charm of pet care, this application serves as both a fun and educational tool for those who are curious about pets but cannot commit to a real one, as well as for those who simply enjoy virtual companions.

## 🐱 Project Overview

Willy the Virtual Cat is an interactive application created to simulate various aspects of cat ownership. This project provides a user-friendly platform for users to learn about and engage with a virtual pet, making it a perfect tool for potential pet owners or those who love animals but cannot keep a real pet. Through daily care activities, users can experience the responsibility and joy of caring for a pet.

## 🐱 Features

- **Interactive Care**: Feed, groom, and play with Willy to keep her happy and healthy.
- **Day/Night Cycle**: Willy's behavior changes based on the time of day, offering different interactions in the morning, afternoon, and night.
- **Health and Happiness Tracking**: Keep an eye on Willy's needs through indicators for hunger, thirst, happiness, health, energy, and boredom.
- **Sound Effects**: Each action is accompanied by realistic cat sounds, enhancing the interactive experience.
- **State Persistence**: Willy's state is saved and loaded automatically, allowing you to pick up right where you left off.

## 🐱 Project Structure

- **`main.py`**: The main script for running the application, containing the GUI and game logic.
- **`pet.py`**: Defines the `Pet` class with methods for managing Willy's state and behaviors.
- **`pet_state.json`**: Stores the current state of Willy, including her health, happiness, and other attributes.
- **`Sounds/`**: Contains all the sound files used in the application, enhancing the gameplay with audio cues.

## 🐱 How to Fork and Set Up the Game

If you're interested in setting up Willy the Virtual Cat and play, you can fork the repository and run the game on your local machine. Here's how to do it:

1. **Fork the Repository**
   - Navigate to the GitHub page of the repository.
   - In the top-right corner of the page, click the "Fork" button. This creates a copy of the repository in your own GitHub account.

2. **Clone the Forked Repository**
   - Once forked, go to your GitHub account, open the forked repository, and click on "Code" to find the URL to clone.
   - Open your terminal or command prompt and run the following command:
     ```
     git clone [URL of the forked repository]
     ```
   - Replace `[URL of the forked repository]` with the URL you copied.

3. **Set Up the Virtual Environment**
   - Navigate into the cloned directory:
     ```
     cd willy-the-virtual-cat
     ```
   - Create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source venv/bin/activate
       ```

4. **Install Dependencies**
   - Install all required packages:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Game**
   - Start the game by running:
     ```
     python main.py
     ```
   - Follow the on-screen instructions to interact with Willy.

By following these steps, you can set up and start playing with Willy on your local system. Enjoy exploring and potentially enhancing Willy's virtual world!



## 🐱 How to Play

- **Feed Willy**: Click on the "Feed" button to decrease her hunger.
- **Hydrate Willy**: Click on the "Drink" button to keep her hydrated.
- **Entertain Willy**: Use the "Play" button to engage Willy and increase her happiness.
- **Care for Willy**: The "Groom" button helps maintain Willy's cleanliness and happiness.
- **Rest Willy**: Use the "Sleep" button to help Willy regain energy and improve her health.

## 🐱 Goals and Motivation

The primary goal of this project is to provide an engaging experience for users who are interested in pets but may not have one. By simulating the care and interaction with Willy, users can enjoy a glimpse of pet ownership and learn more about a cat's daily needs and behaviors. This project was inspired by my own pet, Willy, and aims to share the joy and responsibilities of pet care with a wider audience.

## Contact

For any questions or suggestions, please contact:

- **Name:** Shamin Yasar
- **Email:** shaminyasar2001@gmail.com
- **Portfolio:** [here](https://shamin-portfolio.netlify.app/)

---

Enjoy your time with Willy, exploring the rewarding experience of virtual pet care!
