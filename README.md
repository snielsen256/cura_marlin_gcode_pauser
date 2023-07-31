# Cura Marlin G-code Pauser

## Introduction
When preparing a file for 3D printing, it first has to go through a slicer program. This produces a g-code file, which contains specific instructions on how the printer should move.

This program takes a g-code file, reads the number of layers, and inserts a pause command (M600) after a certain layer. This makes it much easier to change filaments.

This is specific to the Ultimaker Cura slicer, since it relies on it's commenting structure to detect layer changes.

## Resources

This program was built around the following resources. It may work with different ones, but no guarantees. 

In order of importance:
* G-code flavor: Marlin
* Slicer: Ultimaker Cura 4.13.1
* Printer: Creality Ender 3 Pro

## Links

* https://marlinfw.org/meta/gcode/
* https://3dprinterly.com/ultimate-marlin-g-code-guide-how-to-use-them-for-3d-printing/
* https://3dprintingwiz.com/gcode-pause/ 
* https://www.askpython.com/python/built-in-methods/modify-text-file-python


