import  minecraft_launcher_lib
v = minecraft_launcher_lib.forge.find_forge_version("1.18.2")
minecraft_launcher_lib.forge.install_forge_version(v, ".minecraft")