import minecraft_launcher_lib
import zipfile
import os
import requests
import subprocess
minecraft_directory = ".minecraft"
forge_version = '1.18.2-40.2.0'
home = os.environ.get('USERPROFILE')
if not os.path.exists(home+r"\.config\wangzhimeng"):
	os.mkdir(home+r"\.config")
	os.mkdir(home+r"\.config\wangzhimeng")
option_dir = home+r"\.config\wangzhimeng"
if not os.path.exists(home+r"\.config\wangzhimeng\user"):
	files = open(home+r"\.config\wangzhimeng\user", "w+")
	files.close()
current_max = 0
def set_status(status: str):
	print('\n\r'+status)
def set_progress(progress: int):
	if current_max != 0:
		print(f"\r{progress}/{current_max}", end='')

def set_max(new_max: int):
	global current_max
	current_max = new_max

callback = {
	"setStatus": set_status,
	"setProgress": set_progress,
	"setMax": set_max
}
runtime_version = "java-runtime-beta"
if os.path.exists(option_dir+r"\install"):
	FILE = open(option_dir+r"\install", 'r')
	LINE = FILE.readlines()
else:
	LINE = minecraft_directory
mcdir = LINE[0]
runtime = minecraft_launcher_lib.runtime.get_executable_path(runtime_version, mcdir)
if runtime == 'None':
	runtime = os.environ.get('JAVA_HOME')+r"\bin\java.exe"
else:
	runtime = minecraft_launcher_lib.runtime.get_executable_path(runtime_version, mcdir)
def installJDK(path: str):
	minecraft_launcher_lib.runtime.install_jvm_runtime(runtime_version, path, callback)

def cls():
	os.system('cls')
def launcher(player: str):
	options = minecraft_launcher_lib.utils.generate_test_options()
	options['username'] = player
	options['executablePath'] = runtime
	options["launcherName"] = 'WZM'
	options["launcherVersion"] = "114514"
	print('检查游戏完整性...',end='')
	minecraft_launcher_lib.install.install_minecraft_version('1.18.2', mcdir, callback)
	if os.path.exists(mcdir+r'\versions\1.18.2-forge-40.2.0'):
		print('forge已安装！')
		forgeinput = input(r'是否使用forge？（是/否）')
		if forgeinput == '是':
			command = minecraft_launcher_lib.command.get_minecraft_command("1.18.2-forge-40.2.0", mcdir, options)
		else:
			command = minecraft_launcher_lib.command.get_minecraft_command("1.18.2", mcdir, options)
	subprocess.run(command)
#install
def install():
	Dir = input("(默认安装目录：.minecraft)\n安装目录？(按回车选择默认)：")
	if Dir == '':
		print('安装中...',end='')
		minecraft_launcher_lib.install.install_minecraft_version("1.18.2", minecraft_directory, callback=callback)
		file = open(option_dir+r"\install",  "a+")
		file.write(minecraft_directory)
		file.close()


	else:
		print('安装中...',end='')
		minecraft_launcher_lib.install.install_minecraft_version("1.18.2", Dir,callback=callback)
		file = open(option_dir+r"\install", "a+")
		file.write(Dir)
		file.close()

cls()
def info():
	print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
	print('输入1：启动minecraft')
	print(r'输入2：下载forge/服务器模组依赖')
	print('输入3：更改用户')
	print('输入4：更改安装目录')
	print('输入0：退出')
if os.path.exists(option_dir+r"\install"):
	print('已安装！')
else:
	print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
	Input = input("是否安装？（是/否）(已安装选择否）")
	if Input == '否':
		put = input('已安装？（是/否）：')
		if put == '是':
			Put = input("安装目录？：")
			file = open(option_dir+r"\install", "a+")
			file.write(Put)
			file.close()
			cls()
		else:
			exit()
	if Input == '是':
		install()
		cls()

#主要部分
def body():
	print('安装目录：'+mcdir)

	with open(option_dir+r"\user", "r") as file:
	# 读取文件内容
		content = file.read()
		if content == '':
			content = 'unknown'
		print('当前用户：'+content)
	info()
	Input = input('输入选项：')
	INput = int(Input)
	if INput == 0:
		exit()
	if INput == 3:
		cls()
		INPut = input('输入用户名：')
		user = open(option_dir+r'\user', "w+")
		user.write(INPut)
		user.close()
		cls()
		body()
	if INput == 2:
		with open(option_dir+r"\install", "r") as file:
			# 读取文件内容
			content = file.read()
			if not os.path.exists(content+r"\mods"):
				os.mkdir(content+r"\mods")
			print('安装forge中...',end='')
			minecraft_launcher_lib.forge.install_forge_version(forge_version, content, callback, runtime)
			if not os.path.exists(mcdir+r'\mods\mod.zip'):
				print("\n下载中...")
				get = requests.get("https://pan.miaoi.top/f/L2EDhB/mods.zip")
				open(content+r"\mods\mod.zip", "wb").write(get.content)
				Zipfile = zipfile.ZipFile(content+r"\mods\mod.zip", "r")
				for Files in Zipfile.namelist():
					Zipfile.extract(Files, content+r"\mods")
				Zipfile.close()
			cls()
			body()
	if INput == 1:
		with open(option_dir+r"\user", "r") as file:
			# 读取文件内容
			player = file.read()
			if player == '':
				player = 'unknown'
			print('当前用户：'+player)
			print('安装目录：'+mcdir)
			launcher(player)
		cls()
		body()
	if INput == 4:
		PUT = input('安装目录？')
		open(option_dir+r'\install','w+').write(PUT)
		cls()
		body()
body()