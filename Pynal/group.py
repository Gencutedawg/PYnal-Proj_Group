#pls do not remove comments, rreview ko pa for defense hehhe tytytyytytyy


from tkinter import Tk, Canvas, Label # Import Tkinter modules for GUI components
from PIL import Image, ImageTk, ImageDraw  # Import modules from PIL for image processing

class WeKpopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WeKpop")  # Set the title of the application window
        self.root.geometry("1920x1080+0+0")  # Set the size and position of the window
        self.create_canvas()  # Call function to create the main canvas
        self.run()  # Start the application loop

    def create_canvas(self):
        # Create the main canvas widget
        self.canvas = Canvas(self.root, width=1920, height=1080)
        self.canvas.pack()
        # Create two rows on the canvas with different colors
        self.create_row(0, "#343ab1", 1920)
        self.create_row(100, "Light yellow", 1920)

    def create_row(self, y_position, color, length):
        # Create a rectangle on the canvas to represent a row
        self.canvas.create_rectangle(0, y_position, length, y_position + 1080, fill=color, outline="")

    def create_labels(self):
        # Load and display the logo image
        logo_image = Image.open("whitecrown.png")
        logo_image = logo_image.resize((70, 70))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = Label(self.root, image=logo_photo, bg="#343ab1")
        logo_label.image = logo_photo
        logo_label.place(x=20, y=20)

        # Load and display the profile image
        profile_image = Image.open("profile.png")
        profile_image = profile_image.resize((70, 70))
        profile_photo = ImageTk.PhotoImage(profile_image)
        profile_label = Label(self.root, image=profile_photo, bg="#343ab1")
        profile_label.image = profile_photo
        profile_label.place(x=1830, y=15)

        # Create labels for application header and user information
        Label(self.root, text="WeKpop", font=("Cooper Black", 40), bg="#343ab1", fg="white").place(x=100, y=20)
        Label(self.root, text="Juan Dela Cruz", font=("TW Cen MT", 16), bg="#343ab1", fg="white").place(x=1650, y=20)
        Label(self.root, text="Logout", font=("TW Cen MT", 16), bg="#343ab1", fg="white").place(x=1750, y=50)

        # Define groups and their positions, load images, and display them with labels
        groups = ["BTS", "ENHYPEN", "New Jeans", "Stray Kids", "TXT", "Twice"]
        x_positions = [200, 800, 1400, 200, 800, 1400]
        y_positions = [400, 400, 400, 700, 700, 700]

        for i, group in enumerate(groups):
            image = Image.open(f"{group.lower()}.jpg")# Load the image corresponding to the current group
            image = image.resize((350, 200))# Resize the image to the desired dimensions
            radius = 20  # Define the radius for the rounded corners
            mask = Image.new("L", image.size, 0) # Create a mask for the rounded corners
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, image.size[0], image.size[1]), radius, fill=255)# Draw rounded rectangle on the mask
            image.putalpha(mask) # Apply the mask to the image
            photo = ImageTk.PhotoImage(image)# Convert the modified image to a PhotoImage
            image_label = Label(self.root, image=photo, bg="light yellow")# Create a label to display the image on the root window
            image_label.image = photo
            image_width = image.size[0] # Calculate the centered position for the image label
            x_centered = x_positions[i] + (175 - image_width // 2)
            image_label.place(x=x_centered, y=y_positions[i]) # Place the image label on the root window

            Label(self.root, text=group, font=("Cooper Black", 12), fg="#343ab1", bg="light yellow").place(x=x_positions[i] + 100, y=y_positions[i] + 230) # Create a label to display the group name below the image

    def run(self):
        # Create labels for the application content
        self.create_labels()
        # Create a label for the "GROUPS" section
        Label(self.root, text="GROUPS", font=("Cooper Black", 20), fg="pink", bg="light yellow").place(x=100, y=160)
        # Start the main event loop
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()# Create the Tkinter root window
    app = WeKpopApp(root)# Create an instance of the WeKpopApp class with the root window as argument

