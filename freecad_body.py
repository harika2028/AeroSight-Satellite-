import FreeCAD as App
import FreeCADGui
import Part

doc = App.newDocument("AeroSight")

# (name, shape, colour) - all sizes in millimetres, 3U = 100 x 100 x 300
parts = [
    ("Camera_1U",   Part.makeBox(100, 100, 100, App.Vector(0, 0, 0)),   (0.55, 0.45, 0.85)),
    ("Computer_1U", Part.makeBox(100, 100, 100, App.Vector(0, 0, 100)), (0.20, 0.70, 0.60)),
    ("Power_1U",    Part.makeBox(100, 100, 100, App.Vector(0, 0, 200)), (0.90, 0.50, 0.40)),
    ("Lens",        Part.makeCylinder(20, 10, App.Vector(50, 50, -10), App.Vector(0, 0, 1)), (0.30, 0.30, 0.30)),
    ("Solar_Panel_Right", Part.makeBox(3, 100, 300, App.Vector(100, 0, 0)), (0.10, 0.30, 0.70)),
    ("Solar_Panel_Left",  Part.makeBox(3, 100, 300, App.Vector(-3, 0, 0)),  (0.10, 0.30, 0.70)),
    ("Antenna",     Part.makeCylinder(1.5, 170, App.Vector(50, 50, 300), App.Vector(0, 0, 1)), (0.70, 0.70, 0.70)),
]

for name, shape, colour in parts:
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape
    obj.ViewObject.ShapeColor = colour

doc.recompute()
FreeCADGui.SendMsg("ViewFit")
FreeCADGui.activeDocument().activeView().viewIsometric()