import minecraft_launcher_lib
import os
runtime_version = "java-runtime-beta"
mcdir = '.minecraft'
global runtime
runtime = minecraft_launcher_lib.runtime.get_executable_path(runtime_version, mcdir)
if runtime == 'None':
    runtime = os.environ.get('JAVA_HOME')+r"\bin\java.exe"
else:
    runtime = minecraft_launcher_lib.runtime.get_executable_path(runtime_version, mcdir)
minecraft_launcher_lib.forge.run_forge_installer('1.18.2-40.2.0', runtime)