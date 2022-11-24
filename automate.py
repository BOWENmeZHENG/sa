import write_script as w
import os, glob
import pandas as pd
import matplotlib.pyplot as plt


def run_model(index, r_out, r_in, width, spoke_width, num_spokes, init_angle, E, load, meshsize, vis=False):
    filename = w.write_pymodel(index=index, r_out=r_out, r_in=r_in, width=width,
                               spoke_width=spoke_width, num_spokes=num_spokes, init_angle=init_angle,
                               E=E, load=load, meshsize=meshsize)
    os.system(f"abaqus cae noGUI={filename}")
    os.remove(filename + '.py')
    for f in glob.glob("wheel_compression.*"):
        os.remove(f)
    for f in glob.glob("abaqus.rp*"):
        os.remove(f)

    # Visualize
    if vis:
        nodes = pd.read_csv(f"{filename}_nodes.csv")
        x, y, z = nodes.x, nodes.y, nodes.z
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        sca = ax.scatter(x, y, z, c=nodes.s11)
        plt.colorbar(sca, pad=0.1)
        plt.show()
    return index
