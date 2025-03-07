rd /s /q dist
rd /s /q build
rd /s /q lanzou_api_wind.egg-info
D:\Anaconda\envs\python_3_9_2\python setup.py sdist bdist_wheel
@REM D:\Anaconda\envs\python_3_9_2\python.exe -m twine upload dist/*

D:\Anaconda\envs\python_3_9_2\python -m twine upload --username __token__ --password pypi-AgEIcHlwaS5vcmcCJDNkYjNkNzg1LTExZjAtNGQ3ZC04MWZhLWM4ZDc5ZjkzNzRmOAACKlszLCIzM2Y5NTBhMC05MDkxLTQwNzYtYjNiZS03YzU3MGQ2NTRlYmUiXQAABiAzU0OFf1cwLq0_Kg1jeC4QG-mVE9IpIiqx92bh4rtR4w dist/*