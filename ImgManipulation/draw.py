from PIL import Image, ImageFont, ImageDraw


def writeOnImg(baseImgPath: str, outputFilePath: str, fontPath: str, fontSize: int, text1: str, x1: int, y1: int, hex1, text2: str = None, x2: int = None, y2: int = None, hex2=None):
    both = True
    if hex1 is None:
        hex1 = (0, 0, 0)
    if hex2 is None:
        hex2 = (0, 0, 0)
    if text2 is None:
        both = False
    baseImage = Image.open(baseImgPath)
    font = ImageFont.truetype(fontPath, fontSize)
    draw = ImageDraw.Draw(baseImage)
    draw.text((x1, y1), text1, hex1, font=font)
    if both:
        draw.text((x2, y2), text2, hex2, font=font)
    baseImage.save(outputFilePath)


def drawImgOnImg(baseImgPath: str, outputFilePath: str, overlayImgPath: str, x: int, y: int, resize=None):
    baseImage = Image.open(baseImgPath)
    overlayImage = Image.open(overlayImgPath)
    if resize != None:
        overlayImage.resize(resize)
    baseImage.paste(overlayImage, (x, y))
    baseImage.save(outputFilePath)
