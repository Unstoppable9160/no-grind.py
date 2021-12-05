from PIL import Image, ImageFont, ImageDraw


def writeOnImg(baseImgPath: str, outputFilePath: str, fontPath: str, fontSize: int, text1: str, x1: int, y1: int, hex1, text2: str, x2: int, y2: int, hex2):
    both = True
    if hex1 is None:
        hex1 = (0, 0, 0)
    if hex2 is None:
        hex2 = (0, 0, 0)
    if text2 is None:
        both = False
    baseImage = Image.open(baseImgPath)
    Font = ImageFont.truetype(fontPath, fontSize)
    draw = ImageDraw.Draw(baseImage)
    draw.text((x1, y1), text1, hex1, font=Font)
    if both:
        draw.text((x2, y2), text2, hex2, font=Font)
    baseImage.save(outputFilePath)