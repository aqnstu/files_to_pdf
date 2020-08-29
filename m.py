# нужно еще поставить poppler (https://poppler.freedesktop.org/)
import os
import pdf2image
import glob

from PIL import Image


def main():
    # получаем картинки из всех .pdf в папке files
    pdfs_path = glob.glob(os.path.join('files', '*.pdf'))
    pics_from_pdfs = []
    for _path in pdfs_path:
        pics_from_pdfs.extend(pdf2image.convert_from_path(_path))

    # получаем все картинки из папки files
    pic_types = ('*.jpg', '*.jpeg', '*.png')
    pics_path = []
    for _type in pic_types:
        pics_path.extend(glob.glob(os.path.join('files', _type)))

    # перобразуем в объекты PIL Image
    pics = []
    for file in pics_path:
        pics.append(Image.open(file).convert('RGB'))

    # все картинки
    all_pics = [*pics, *pics_from_pdfs]

    # получаем файл .pdf
    all_pics[0].save(
        os.path.join('result', 'res.pdf'),
        save_all=True,
        append_images=all_pics[1:]
    )


if __name__ == "__main__":
    main()