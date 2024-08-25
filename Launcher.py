import os
import json
import minecraft_launcher_lib
import subprocess
version = "1.18.2"
launcher_version = '2.0.0'
home = os.environ.get('USERPROFILE')
config_path = home+"/.config/wzm/config.json"
if not os.path.exists(home+"/.config/wzm"):
	os.mkdir(home+"/.config")
	os.mkdir(home+"/.config/wzm")
if not os.path.exists(config_path):
	file = open(config_path, "w+")
	file.write("{\n}")
	file.close
#write_file = open(config_path,'w+')
file = open(config_path, "r+")
try:
	config_json = json.load(file)
	file.close()
except Exception as e:
	print(e)
	os.system('pause')
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
def install(path: str):
	minecraft_launcher_lib.install.install_minecraft_version(version, path, callback)
	print("安装完成！")
def body():
	print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
	print('输入1：启动minecraft')
	print('输入2：更改用户')
	print('输入3：更改安装目录')
	print('输入4：设置')
	print('输入0：退出')
	Input = int(input('输入：'))
	if Input == 1:
		if "installPath" in config_json:
			option = minecraft_launcher_lib.utils.generate_test_options()
			if 'user_name' in config_json:
				option['username'] = config_json['user_name']
			else:
				option['username'] = 'Unknown'
			option['launcherName'] = 'WZM Launcher'
			option['launcherVersion'] = launcher_version
			option['executablePath'] = minecraft_launcher_lib.runtime.get_executable_path("java-runtime-beta",config_json["installPath"])
			print('检查游戏完整性...')
			minecraft_launcher_lib.install.install_minecraft_version(version, config_json["installPath"], callback)
			minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version, str(config_json["installPath"]), option)
			subprocess.run(minecraft_command)
		else:
			print('您尚未安装Minecraft')
			Input = input('已安装？(是/否)')
			if Input == '是':
				Input = input('安装目录：')
				config_json['installPath'] = Input
				file = open(config_path, "w+")
				json.dump(config_json, file)
				file.close()
		body()
	elif Input == 2:
		config_json['user_name'] = input('用户名：')
		file = open(config_path, "w+")
		json.dump(config_json, file)
		file.close()
		body()
	elif Input == 3:
		config_json["installPath"] = input('安装目录：')
		file = open(config_path, "w+")
		json.dump(config_json, file)
		file.close()
		body()
	elif Input == 4:
		print('没写')
		body()
	else:
		exit()
body()