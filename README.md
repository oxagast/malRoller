# Usage

* Clone the git repo.
* Choose a decoy program, has to be .exe format.
* Copy the decoy program's .exe into the repo dir and rename it decoy.exe.
* Pick a payload, such as the rev_shell, and copy it to the repo root, renaming it payload.py.
* Edit the src of the payload's .py to reflect the host and port you want to connect back to.
* Run the build_script.bat file either from a shell, or just click on it.
* Now should appear a new directory named .\repacked\ with a .exe file in it.
* The file will be about 13mb to 15mb in size, plus however large the decoy.exe is.
* Locally run nc -l -p [port of choice] -v.
* Social engineer your victim into running the executable in the repacked dir.
* Wait for shell!

Enjoy!
