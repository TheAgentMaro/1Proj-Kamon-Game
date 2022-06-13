from cx_Freeze import setup, Executable
import os.path

executables = [Executable(script = "main.py",icon = "kamon.ico", base = "Win32GUI" )]
  
buildOptions = dict( 
        includes = ["tkinter","PIL","pygame","math","random","socket","sys","_thread"], 
        
        include_files = ["kamon.ico" ,
                         "RUDE.ogg" ,
                         "assets/logo/kamon1.png",
                         "assets/logo/kamon2.png",
                         "assets/logo/kamon3.png",
                         "assets/logo/kamon4.png",
                         "assets/logo/kamon5.png",
                         "assets/logo/kamon6.png",
                         "assets/background.jpg",
                         "assets/back.png",
                         "assets/button_pause.png",
                         "assets/button_quitter.png",
                         "assets/button_relancer.png",
                         "assets/button_sauvegarder-et-quitter.png",
                         "assets/button_vs-ia.png",
                         "assets/button_vs-online.png",
                         "assets/button_vs.png",
                         "assets/parametre.png",
                         "assets/pausem.png",
                         "assets/play.png",
                         "assets/playmusic.png",
                         "assets/board.jpg"
                         ]
)
  
setup(
    name = "Play Kamon",
    version = "1.2",
    description = "Kamon Game",
    author = "Marwen Meddeb",
    options = dict(build_exe = buildOptions),
    executables = executables
)