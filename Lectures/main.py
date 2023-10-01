
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Set the limits of the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
h
# Create a circle representing the ball
ball = plt.Circle((0, 2.5), 1, fc='yellow')
ax.add_patch(ball)

# Function to update the ball's position
def update(frame):
    x = frame * 0.1 # Adjust the speed by changing the multiplier
    ball.set_center((x, 2.5))
    return ball,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True)

# Display the animation
plt.show()
