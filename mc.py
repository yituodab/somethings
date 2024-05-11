import minecraft_launcher_lib
import zipfile
import os
import requests
import subprocess
minecraft_directory = ".minecraft"

if not os.path.exists(r"C:\Program Files\wangzhimeng"):
	os.mkdir(r"C:\Program Files\wangzhimeng")
option_dir = r"C:\Program Files\wangzhimeng"
if not os.path.exists(r"C:\Program Files\wangzhimeng\user"):
	files = open(r"C:\Program Files\wangzhimeng\user", "w+")
	files.close()
def installJDK(path: str):
	url = "https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.zip"
	jdk = requests.get(url)
	open(path, "wb").write(jdk.content)

def checkJDK():
	java = os.environ.get('JAVA_HOME')
	if java == 'None':
		print('%JAVA_HOME%未配置\n')
		return False
	else:
		return True
def cls():
	os.system('cls')
def launcher(player: str):
	options = minecraft_launcher_lib.utils.generate_test_options()
	dir = open(option_dir+r"\user", 'a+').read()
	options['username'] = player
	options['executablePath'] = os.environ.get('JAVA_HOME')+r"\bin/java.exe"
	command = minecraft_launcher_lib.command.get_minecraft_command('1.18.2', dir, options)
	subprocess.run(command)
#install
def install():
	Dir = input("(默认安装目录：.minecraft)\n安装目录？(按回车选择默认)：")
	if Dir == '':
		print('安装中...')
		minecraft_launcher_lib.install.install_minecraft_version("1.18.2", minecraft_directory)
		file = open(option_dir+r"install",  "a+")
		file.write(minecraft_directory)
		file.close()
		print('安装forge中...')
		minecraft_launcher_lib.forge.install_forge_version("1.18.2-40.2.0", minecraft_directory)

	else:
		print('安装中...')
		minecraft_launcher_lib.install.install_minecraft_version("1.18.2", Dir)
		file = open(option_dir+r"install", "a+")
		file.write(Dir)
		file.close()
		print('安装forge中...')
		minecraft_launcher_lib.forge.install_forge_version("1.18.2-40.2.0", Dir)

cls()
def info():
	print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
	print('输入1：启动minecraft')
	print(r'输入2：下载forge/服务器模组依赖')
	print('输入3：更改用户')
	print('输入0：退出')
if os.path.exists(option_dir+r"\install"):
	print('已安装！')
else:
	print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
	Input = input("是否安装？（是/否）")
	if Input == '否':
		exit()
	if Input == '是':
		install()
		cls()

#主要部分
def body():
	with open(option_dir+r"\install", "r") as file:
	# 读取文件内容
		content = file.read()
		print('安装目录：'+content)

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
		body()
	if INput == 1 or INput == 2:
		jdk = checkJDK()
		if jdk == False:
			INPUT = input('是否为您安装OPEN JDK17?(是/否）：')
			if INPUT == '是':
				installJDK(r"C:\Program Files\Java\jdk-17.zip")
				Zip = zipfile.ZipFile(r"C:\Program Files\Java\jdk-17.zip", 'r')
				for zipFile in Zip.namelist():
					Zip.extract(zipFile, r"C:\Program Files\Java")
				Zip.close()
				os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-17.0.11"
			if INPUT == '否':
				cls()
				body()
	if INput == 2:

		with open(option_dir+r"\install", "r") as file:
			# 读取文件内容
			content = file.read()
			if not os.path.exists(content+r"\mods"):
				os.mkdir(content+r"\mods")
			print('下载中...')
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
			content = file.read()
			if content == '':
				content = 'unknown'
			print('当前用户：'+content)
			launcher(content)
body()