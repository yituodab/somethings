import minecraft_launcher_lib
import os
minecraft_directory = ".minecraft"
if not os.path.exists(r"C:\Program Files\wangzhimeng"):
	os.mkdir(r"C:\Program Files\wangzhimeng")
option_dir = r"C:\Program Files\wangzhimeng"
print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
def install():
	Dir = input("(默认安装目录：.minecraft)\n安装目录？(按回车选择默认)：")
	if Dir == '':
		print('安装中...')
		minecraft_launcher_lib.install.install_minecraft_version("1.18.2", minecraft_directory)
		print('安装forge中...')
		minecraft_launcher_lib.forge.install_forge_version("40.2.0", minecraft_directory)
		file = open(option_dir+r"install")
		file.write(minecraft_directory)
		file.close()
	else:
		print('安装中...')
		minecraft_launcher_lib.install.install_minecraft_version("1.18.2", Dir)
		print('安装forge中...')
		minecraft_launcher_lib.forge.install_forge_version("40.2.0", Dir)
		file = open(option_dir+r"install", "a+")
		file.write(Dir)
		file.close()
if os.path.exists(option_dir+r"install"):
	print('已安装！')
else:
	Input = input("是否安装？（是/否）")
	if Input == '否':
		exit()
	if Input == '是':
		install()
with open(option_dir+r"\install", "r") as file:
	# 读取文件内容
	content = file.read()
print('安装目录：')
"""
minecraft_directory = ".minecraft"
minecraft_launcher_lib.install.install_minecraft_version("1.18.2", minecraft_directory)
options = minecraft_launcher_lib.utils.generate_test_options()
minecraft_launcher_lib.microsoft_account.get_login_url(client_id：str，redirect_uri：str)
minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url:str)
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.18.2", minecraft_directory, options)
"""