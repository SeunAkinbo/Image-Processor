from PIL import Image, ImageFilter

if __name__ == '__main__':
    try:
        with Image.open('./Pokedex/chamanda.jpg') as img:
            img.thumbnail((200, 200))
            img.save('thumbnail.jpg')
            print(img.size)

            # filtered_img = img.filter(ImageFilter.SMOOTH)
            # filtered_img = img.convert('L')
            # filtered_img.save('blur_chamanda.png', 'png')
            # edited = filtered_img.resize((120, 100))
            print(img.mode, img.size, img.format)
            # edited.show()
    except IOError as err:
        print(f'Cannot read image file - {err}')