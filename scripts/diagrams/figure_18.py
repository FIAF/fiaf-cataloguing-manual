import cv2
import json
import matplotlib.pylab as plt
import numpy
import pandas
import pathlib
import pydash
import skimage
from PIL import Image, ImageDraw, ImageFont

def draw():

    def font(weight, size):
        ''' Define a font object. '''

        font_path = pathlib.Path.cwd().parents[0] / 'font' / f'BrownStd{weight}.otf'
        if not font_path.exists():
            raise Exception('Font OTF does not exist.')

        return ImageFont.truetype(str(font_path), size)


    def text_box(text, weight, size, x_step, y_step, interval, padding):
        text = text.split('\n')
        # text =x [t]
        for x in range(10):
            chunk = text[-1]
            for i, chunk in enumerate(text):
                # print(chunk)
                if len(chunk) > 35:
                    space = [i for i,a in enumerate(chunk) if a == ' ']
                    myspace = max([x for x in space if x < 35])
                    text[i] = [chunk[:myspace], chunk[myspace+1:]]
            # print('@@@', text)
            text = pydash.flatten(text)

        font_object = font(weight, size)
        text_array = list()
        for i,x in enumerate(text):
            detect = font_object.getbbox(x)
            draw.text((x_step, y_step+(i*interval)), x, font=font_object, fill="#000000")
            detect = font_object.getbbox(x)
            text_array.append({
                'text': x,
                'x1': x_step,
                'y1': y_step+(i*interval),
                'x2': x_step+detect[2],
                'y2': y_step+(i*interval)+detect[3],
                })

        df = pandas.DataFrame(text_array)
        full_box = (min(df.x1)-padding, min(df.y1)-padding, max(df.x2)+padding, max(df.y2)+padding)
        draw.rectangle(full_box, outline='#000000', width=1)

        return full_box

    def anchor(box, axis):
        if axis == 'b':
            axis_x, axis_y = (box[2]+box[0])/2, box[3]
        elif axis == 't':
            axis_x, axis_y = (box[2]+box[0])/2, box[1]
        elif axis == 'l':
            axis_x, axis_y = box[0], (box[1]+box[3])/2
        elif axis == 'r':
            axis_x, axis_y = box[2], (box[1]+box[3])/2
        else:
            raise Exception(f'{axis} not understood.')

        # draw.rectangle((axis_x, axis_y,axis_x+10, axis_y+10), outline='#FF0000', width=1, fill='#FF0000')

        return (axis_x, axis_y)

    def arrow(t, start, end):
        if t == "elbow":
            draw.line([start, (start[0], end[1])], fill="#000000", width=1)
            draw.line([(start[0],end[1]), end], fill="#000000", width=1)
        elif t == 'multi':
            new_end = (start[0], (start[1]+end[1])/2)
            new_start = (end[0], (start[1]+end[1])/2)
            draw.line([start, new_end], fill="#000000", width=1)
            draw.line([new_start, end], fill="#000000", width=1)
            draw.line([new_start, new_end], fill="#000000", width=1)
        else:
            raise Exception("type not understood.")


    img_path = pathlib.Path.cwd() / 'figure_18.png'
    canvas_w, canvas_h = 1000, 1500
    canvas = numpy.zeros((canvas_h, canvas_w, 3), numpy.uint8)
    canvas[:, :] = (255, 255, 255)
    cv2.imwrite(img_path, canvas)

    image_data = Image.open(img_path)
    draw = ImageDraw.Draw(image_data)

    with open(pathlib.Path.cwd() / 'figure_18.json') as data:
        data = json.load(data)

    box_data = list()
    for x in data['boxes']:
        bounding = text_box(text=x['text'], weight=x['weight'], size=x['size'], x_step=x['x_step'], y_step=x['y_step'], interval=x['interval'], padding=x['padding'])
        box_data.append(bounding)

    for x in data['arrows']:
        arrow(
            x['type'],
            anchor(box_data[x['source_box']], x['source_axis']),
            anchor(box_data[x['target_box']], x['target_axis'])
        )

    image_data.save(img_path)


if __name__ == "__main__":
    draw()
