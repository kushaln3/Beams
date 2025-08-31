import beams
import ops
from flask import Flask, request, render_template
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

app = Flask(__name__)



if __name__ == "__main__":
    beam = beams.Beam()
    printex = ops.Printex()
    while True:
        printex.Wellcome()

        beamtype = int(input("Choose a beam: "))

        if beamtype == 1:
            beam.simple()
        elif beamtype == 2:
            beam.canti()
        elif beamtype == 3:
            beam.mixed()

        ops.plt.show()
