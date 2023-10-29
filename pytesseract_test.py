from PIL import Image
import pytesseract
import os


def read_image(path, name, index):
    print('now start recognise ', index)
    # text = pytesseract.image_to_string(Image.open(path + '/' + name), lang='chi_sim')
    text = pytesseract.image_to_string(Image.open(path + '/' + name), lang='chi_sim', config='digits')
    # exclude_char_list = '.:\\|\'?!"[]()@#$%^&*<>/'
    # text = ''.join([x for x in text if x not in exclude_char_list])
    content = name + '   _____   ' + text
    print(content)
    fp2 = open('2020li.txt', 'a')

    fp2.write(content.encode('utf-8').decode('utf-8'))
    fp2.close()
    print('finish recognise ', index)


def main():
    path = "./ocrPic"
    for path, dir, file in os.walk(path):
        break
    # pic = []
    # for i in file:
    #     if (".png" in i):
    #         pic.append(i)
    for j in range(len(file)):
        read_image(path, file[j], j)


if __name__ == '__main__':
    main()
