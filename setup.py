# from distutils.core import setup




# from cx_Freeze import setup, Executable

# # setup(
# # name = "hello",
# # version = "0.1",
# # executables = [Executable("jpmain.py")])



# buildOptions = dict(packages = [], excludes = [])

# base = 'Console'

# executables = [
#     Executable('file:///root/workspace/fetcher', base=base, targetName = 'Hello')
# ]

# setup(name='jpxa',
#       version = '1.0',
#       description = '',
#       options = dict(build_exe = buildOptions),
#       executables = executables)




import sys
from cx_Freeze import setup, Executable


buildOptions = dict(include_files = [
						"tcp.py",
						"tcpconn.py",
						"tcptimeout.py",
						"http.py",
						"httpstatus.py",
						"httpfilterstatus.py",
						"httpfilterurlstatus.py",
						"traffic.py",
						"jptemplate.py",
						"apdex.py",
						"httpfilterurldelay.py",
						"httpurlstatus.py",
						"httpurl.py",
						"errorrate.py",
						"httplatency.py",
						"dumper.py",
						"common.py",
						"newrelic_fetcher.py"
					], excludes = [])

build_exe_options = {"optimize": 2,
                     "include_files": [
						"tcp.py",
						"tcpconn.py",
						"tcptimeout.py",
						"http.py",
						"httpstatus.py",
						"httpfilterstatus.py",
						"httpfilterurlstatus.py",
						"traffic.py",
						"jptemplate.py",
						"apdex.py",
						"httpfilterurldelay.py",
						"httpurlstatus.py",
						"httpurl.py",
						"errorrate.py",
						"httplatency.py",
						"dumper.py",
						"common.py",
						"newrelic_fetcher.py"
					]}

base = 'Console'

flag = True
# flag = False

if flag :

	executables = [Executable(
					script='jpmain.py',
					base=base,
					targetName="iprobe_newrelic_fetcher")]
					

	setup(
			name='iprobe_newrelic_fetcher',
			version='0.1',
			description='Sample cx_Freeze wxPython script',
			options = dict(build_exe = buildOptions),
			executables=executables)
else :


	executables = [Executable(
					script='newrelic_fetcher.py',
					base=base,
					targetName="newrelic_fetcher")]
					

	setup(
			name='newrelic_fetcher',
			version='0.1',
			description='Sample cx_Freeze wxPython script',
			options = dict(build_exe = buildOptions),
			executables=executables)
