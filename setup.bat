rd /s /q dist
python3 setup.py sdist bdist_wheel
@REM python3 -m twine upload dist/*

python3 -m twine upload --username __token__ --password pypi-AgEIcHlwaS5vcmcCJDNkYjNkNzg1LTExZjAtNGQ3ZC04MWZhLWM4ZDc5ZjkzNzRmOAACKlszLCIzM2Y5NTBhMC05MDkxLTQwNzYtYjNiZS03YzU3MGQ2NTRlYmUiXQAABiAzU0OFf1cwLq0_Kg1jeC4QG-mVE9IpIiqx92bh4rtR4w dist/*