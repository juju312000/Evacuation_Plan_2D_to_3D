import Interface
import LineDetector
import ObjectDetection
import detectPlanLegend

print("a")
# SELECT FILE
pathfile = Interface.SelectImage()

# INIT CLASS
detected = detectPlanLegend.detectPlanLegend(pathfile)
#detected = detectPlanLegend.detectPlanLegend("data/plans/esiee.jpg")

# DETECT PLAN AND LEGEND
detected.findLegendAndPlan()

# LABELIZED LOGOS
detected.findLogos()

# DETECT LOGOS IN PLAN
#detected.DetectLogo()  # function qui marche moins bien
ObjectDetection.main("data/plans/plan.jpg")

# RETURN LINES COORD
LineDetector.line("/data/result.jpg")









