import time
import numpy as np
import matplotlib.pyplot as plt

banner = r"""
██████╗ ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗███████╗    ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║██╔════╝    ██╔══██╗╚██╗ ██╔╝
██████╔╝██████╔╝██║   ██║██║ █╗ ██║██╔██╗ ██║██║█████╗█████╗██████╔╝ ╚████╔╝ 
██╔══██╗██╔══██╗██║   ██║██║███╗██║██║╚██╗██║██║██╔══╝╚════╝██╔═══╝   ╚██╔╝  
██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝██║ ╚████║██║███████╗    ██║        ██║   
╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝╚══════╝    ╚═╝        ╚═╝   
                                                                             
2D Brownian Motion in Python
"""
print(banner)

### parameters
N = 100000          # number of steps
x, y = [0], [0]     # initial value
delta = 0.25        # random distribution tuner ; sigma = delta**2)*dt
dt = 0.1            # time step

### configuration
fig = plt.figure(figsize=(10, 10), dpi=300)
x = [x[-1]]
y = [y[-1]]

for i in range(1, N):
    # print step every 100
    if i%100 == 0: print(f"iter: {i:8}", end="\r", flush=True)
    # Brownian motion physics
    x.append(x[-1] + np.random.normal(loc = 0, scale = (delta**2)*dt))
    y.append(y[-1] + np.random.normal(loc = 0, scale = (delta**2)*dt))

### graphcis
plt.plot(x, y, "k", lw=1)
plt.axis('off')
### filename generator
name = time.ctime().replace(" ", "-").replace(":", "")
name = f"Brownian-{name}-{delta:.2f}-{dt:.3f}.png"
plt.savefig(name)