import minecraft_launcher_lib
import os
minecraft_directory = ".minecraft"
if not os.path.exists(r"C:\Program Files\wangzhimeng"):
	os.mkdir(r"C:\Program Files\wangzhimeng")
if not os.path.exists(r"C:\Program Files\wangzhimeng\option"):
	op = open(r"C:\Program Files\wangzhimeng\option", "a")
	op.write("#This is mc options")
	op.close()
option_dir = r"C:\Program Files\wangzhimeng"
option_file = r"C:\Program Files\wangzhimeng\option"
print('Warning：本启动器为往之门服务器定制，且仅能使用离线用户')
file = open(option_file, "a")
lines = file.readlines()
for line in lines:
	if line.find("install=true") == -1:
		Input = input("是否安装？（是/否）")
		if Input == '否' :
			exit()
		if Input == '是' :
			Dir = input("(默认安装目录：.minecraft)\n安装目录？(按回车选择默认：")
			minecraft_launcher_lib.install.install_minecraft_version("1.18.2", minecraft_directory)
			file.write("install=true\n")

file.close()
"""
minecraft_directory = ".minecraft"
minecraft_launcher_lib.install.install_minecraft_version("1.18.2", minecraft_directory)
options = minecraft_launcher_lib.utils.generate_test_options()
minecraft_launcher_lib.microsoft_account.get_login_url(client_id：str，redirect_uri：str)
minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url:str)
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.18.2", minecraft_directory, options)
"""