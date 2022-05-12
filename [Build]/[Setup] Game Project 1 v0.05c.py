import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("[Game Project 1] Fall of Renais v0.05c.py")]

cx_Freeze.setup(
    name="Fall of Renais",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["BackgroundMenu.jpg","Background.png","character_selection.png","CYL_Eirika.png","CYL_Ephraim.png","eirika_masterlord_sword.png","eirika_masterlord_sword_reverse.png","ephraim_masterlord_lance.png","ephraim_masterlord_lance_reverse.png","scoreboard.png",
                                              "Combat_Preparations.mp3","Determination.mp3","Distant_Roads.mp3","In_Sorrows_Shadows.mp3","Truth_Despair_and_Hope.mp3",
                                              "Death.wav","Select 2.wav","Select 3.wav",
                                             "README.txt"]}},
    executables = executables

    )
