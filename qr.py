import qrcode
# from PIL import Image
no = input("no:")
img=qrcode.make(f'https://api.issks.com/issksh5/?#/pages/chargeScanning/chargeScanning?outletNo={no}')
img.show()