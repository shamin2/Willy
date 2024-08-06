import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pet import Pet
import pygame
from datetime import datetime
import os

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Define the path to the sounds folder
sound_folder = "sounds"

# Load sound effects from the sounds folder
sound_meow = pygame.mixer.Sound(os.path.join(sound_folder, "meow.wav"))
sound_drink = pygame.mixer.Sound(os.path.join(sound_folder, "drink.wav"))
sound_sleep = pygame.mixer.Sound(os.path.join(sound_folder, "sleep.wav"))
sound_groom = pygame.mixer.Sound(os.path.join(sound_folder, "groom.wav"))
sound_feed = pygame.mixer.Sound(os.path.join(sound_folder, "meow.wav"))


class VirtualPetApp:
    def __init__(self, root):
        self.root = root
        self.pet = Pet()
        self.pet.load_state()

        # Set window size
        root.geometry("600x550")

        self.day_bg = 'lightblue'
        self.night_bg = 'darkblue'

        # Determine if it's day or night
        self.is_daytime = self.check_daytime()

        # Set initial background color
        root.configure(bg=self.day_bg if self.is_daytime else self.night_bg)

        self.status_frame = tk.Frame(root, bg=self.get_bg_color())
        self.status_frame.pack(pady=10)

        self.hunger_label = tk.Label(self.status_frame, text="Hunger:", font=('Arial', 12), bg=self.get_bg_color())
        self.hunger_label.grid(row=0, column=0, sticky='w')
        self.hunger_bar = ttk.Progressbar(self.status_frame, length=200, maximum=100, value=self.pet.hunger)
        self.hunger_bar.grid(row=0, column=1, padx=10)

        self.thirst_label = tk.Label(self.status_frame, text="Thirst:", font=('Arial', 12), bg=self.get_bg_color())
        self.thirst_label.grid(row=1, column=0, sticky='w')
        self.thirst_bar = ttk.Progressbar(self.status_frame, length=200, maximum=100, value=self.pet.thirst)
        self.thirst_bar.grid(row=1, column=1, padx=10)

        self.happiness_label = tk.Label(self.status_frame, text="Happiness:", font=('Arial', 12),
                                        bg=self.get_bg_color())
        self.happiness_label.grid(row=2, column=0, sticky='w')
        self.happiness_bar = ttk.Progressbar(self.status_frame, length=200, maximum=100, value=self.pet.happiness)
        self.happiness_bar.grid(row=2, column=1, padx=10)

        self.health_label = tk.Label(self.status_frame, text="Health:", font=('Arial', 12), bg=self.get_bg_color())
        self.health_label.grid(row=3, column=0, sticky='w')
        self.health_bar = ttk.Progressbar(self.status_frame, length=200, maximum=100, value=self.pet.health)
        self.health_bar.grid(row=3, column=1, padx=10)

        self.energy_label = tk.Label(self.status_frame, text="Energy:", font=('Arial', 12), bg=self.get_bg_color())
        self.energy_label.grid(row=4, column=0, sticky='w')
        self.energy_bar = ttk.Progressbar(self.status_frame, length=200, maximum=100, value=self.pet.energy)
        self.energy_bar.grid(row=4, column=1, padx=10)

        self.boredom_label = tk.Label(self.status_frame, text="Boredom:", font=('Arial', 12), bg=self.get_bg_color())
        self.boredom_label.grid(row=5, column=0, sticky='w')
        self.boredom_bar = ttk.Progressbar(self.status_frame, length=200, maximum=100, value=self.pet.boredom)
        self.boredom_bar.grid(row=5, column=1, padx=10)

        # Load cat images with transparent backgrounds
        self.images = {
            "hungry": Image.open("hungry.png"),
            "happy": Image.open("happy.png"),
            "sad": Image.open("sad.png")
        }

        self.pet_image = tk.Label(root, bg=self.get_bg_color())
        self.pet_image.pack(pady=10)
        self.pet_image.bind("<Button-1>", self.pet_clicked)  # Add click event handler
        self.update_pet_image()

        self.button_frame = tk.Frame(root, bg=self.get_bg_color())
        self.button_frame.pack(pady=10)

        self.feed_button = tk.Button(self.button_frame, text="Feed", command=self.feed_pet, font=('Arial', 12),
                                     bg='lightgreen')
        self.feed_button.grid(row=0, column=0, padx=10, pady=10)

        self.drink_button = tk.Button(self.button_frame, text="Drink", command=self.drink_pet, font=('Arial', 12),
                                      bg='lightblue')
        self.drink_button.grid(row=0, column=1, padx=10, pady=10)

        self.play_button = tk.Button(self.button_frame, text="Play", command=self.play_with_pet, font=('Arial', 12),
                                     bg='yellow')
        self.play_button.grid(row=0, column=2, padx=10, pady=10)

        self.groom_button = tk.Button(self.button_frame, text="Groom", command=self.groom_pet, font=('Arial', 12),
                                      bg='pink')
        self.groom_button.grid(row=1, column=0, padx=10, pady=10)

        self.sleep_button = tk.Button(self.button_frame, text="Sleep", command=self.sleep_pet, font=('Arial', 12),
                                      bg='lightgray')
        self.sleep_button.grid(row=1, column=1, padx=10, pady=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=root.quit, font=('Arial', 12), bg='red')
        self.quit_button.grid(row=1, column=2, padx=10, pady=10)

        # Message label to display feedback
        self.message_label = tk.Label(root, text="", font=('Arial', 12), bg=self.get_bg_color())
        self.message_label.pack(pady=10)

        # Start the timer to decrease happiness over time
        self.decrease_happiness()

    def stop_sounds(self):
        """Stop all currently playing sounds."""
        pygame.mixer.stop()

    def pet_clicked(self, event):
        """Handle clicks on the pet image to increase happiness and play grooming sound."""
        self.stop_sounds()  # Stop any currently playing sound
        if self.pet.happiness < 100:
            self.pet.happiness = min(100, self.pet.happiness + 5)
            sound_groom.play()  # Play grooming sound on click
            self.display_message("Willy enjoys the attention!")
            self.update_status()

    def display_message(self, message):
        """Display a message on the message label."""
        self.message_label.config(text=message)

    def check_daytime(self):
        """Determine if it is day or night based on the current hour."""
        current_hour = datetime.now().hour
        # Daytime is between 6 AM and 6 PM
        return 6 <= current_hour < 18

    def get_bg_color(self):
        """Return the background color based on the time of day."""
        return self.day_bg if self.is_daytime else self.night_bg

    def update_pet_image(self):
        """Update the displayed image of the pet based on its status."""
        if self.pet.hunger > 70:
            image = self.images["hungry"]
        elif self.pet.happiness > 70:
            image = self.images["happy"]
        else:
            image = self.images["sad"]

        image = image.resize((300, 300), Image.LANCZOS)  # Resize image
        image = ImageTk.PhotoImage(image)
        self.pet_image.config(image=image)
        self.pet_image.image = image

    def feed_pet(self):
        self.stop_sounds()  # Stop any currently playing sound
        if self.pet.hunger > 0:
            self.pet.feed()
            sound_feed.play()
            self.update_status()
            self.display_message("Willy is fed!")
        else:
            self.display_message("Willy is not hungry right now.")

    def drink_pet(self):
        self.stop_sounds()  # Stop any currently playing sound
        if self.pet.thirst > 0:
            self.pet.drink()
            sound_drink.play()
            self.update_status()
            self.display_message("Willy had a drink!")
        else:
            self.display_message("Willy is not thirsty right now.")

    def play_with_pet(self):
        self.stop_sounds()  # Stop any currently playing sound
        if self.pet.energy > 10:
            # Increase happiness more at night
            self.pet.happiness = min(100, self.pet.happiness + (15 if not self.is_daytime else 10))
            self.pet.energy = max(0, self.pet.energy - 10)
            self.pet.boredom = max(0, self.pet.boredom - 20)
            sound_meow.play()
            self.update_status()
            self.display_message("You played with Willy!")
        else:
            self.display_message("Willy is too tired to play.")

    def groom_pet(self):
        self.stop_sounds()  # Stop any currently playing sound
        self.pet.groom()
        sound_groom.play()
        self.update_status()
        self.display_message("Willy feels pampered!")

    def sleep_pet(self):
        self.stop_sounds()  # Stop any currently playing sound
        self.pet.sleep()
        sound_sleep.play()
        self.update_status()
        self.display_message("Willy is well-rested!")

    def update_status(self):
        # Update the progress bars
        self.hunger_bar['value'] = self.pet.hunger
        self.thirst_bar['value'] = self.pet.thirst
        self.happiness_bar['value'] = self.pet.happiness
        self.health_bar['value'] = self.pet.health
        self.energy_bar['value'] = self.pet.energy
        self.boredom_bar['value'] = self.pet.boredom

        self.update_pet_image()
        self.pet.save_state()

    def decrease_happiness(self):
        # Decrease happiness gradually over time
        if self.pet.happiness > 0:
            self.pet.happiness -= 1

        # Increase boredom gradually over time
        if self.pet.boredom < 100:
            self.pet.boredom += 1

        # Update thirst and hunger gradually over time
        if self.pet.hunger < 100:
            self.pet.hunger += 1

        if self.pet.thirst < 100:
            self.pet.thirst += 1

        # Check health
        if self.pet.hunger > 80 or self.pet.thirst > 80:
            self.pet.health = max(0, self.pet.health - 2)
            self.display_message("Willy's health is declining due to neglect!")

        self.update_status()

        # Schedule the function to run again after 5000 milliseconds (5 seconds)
        self.root.after(5000, self.decrease_happiness)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Willy")
    app = VirtualPetApp(root)
    root.mainloop()
