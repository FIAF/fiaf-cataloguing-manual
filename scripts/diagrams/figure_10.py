import cv2
import matplotlib.pylab as plt
import json
import numpy
import pandas
import pathlib
import pydash
import skimage
from PIL import Image, ImageDraw, ImageFont

def render():

    def font(weight, size):
        ''' Define a font object. '''

        font_path = pathlib.Path.cwd().parents[0] / 'font' / f'BrownStd{weight}.otf'
        if not font_path.exists():
            raise Exception('Font OTF does not exist.')

        return ImageFont.truetype(str(font_path), size)

    def calc_position(b):

        text = b['text']
        x_step = b['x_step']
        y_step = b['y_step']
        interval = b['interval']
        padding = b['padding']

        text = text.split('\n')
        for x in range(10):
            chunk = text[-1]
            for i, chunk in enumerate(text):
                if len(chunk) > 35:
                    space = [i for i,a in enumerate(chunk) if a == ' ']
                    myspace = max([x for x in space if x < 35])
                    text[i] = [chunk[:myspace], chunk[myspace+1:]]
            text = pydash.flatten(text)

        font_object = font(b['weight'], b['size'])
        text_array = list()
        for i,x in enumerate(text):
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

        b['text_array'] = text_array
        b['bbox'] = full_box

        return b

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

        return {'x': int(axis_x), 'y': int(axis_y)}

    with open(pathlib.Path.cwd() / 'figure_10.json') as data:
        data = json.load(data)

    for i, box in enumerate(data['boxes']):
        data['boxes'][i] = calc_position(box)

    for i, arrow in enumerate(data['arrows']):

        source_box = arrow['source_box']
        source_axis = arrow['source_axis']

        target_box = arrow['target_box']
        target_axis = arrow['target_axis']

        a = anchor(data['boxes'][source_box]['bbox'], source_axis)
        b = anchor(data['boxes'][target_box]['bbox'], target_axis)

        data['arrows'][i]['anchor'] = {'a': a, 'b': b}

    max_x = max([x['bbox'][2] for x in data['boxes']])
    max_y = max([x['bbox'][3] for x in data['boxes']])

    test_path = pathlib.Path.cwd() / 'figure_10.png'
    canvas_w, canvas_h = max_x+25, max_y+25
    canvas = numpy.zeros((canvas_h, canvas_w, 3), numpy.uint8)
    canvas[:, :] = (255, 255, 255)

    for b in data['boxes']:
        x1, y1, x2, y2 = b['bbox']
        cv2.rectangle(canvas, (x1, y1), (x2, y2), (0,0,0), 1)

    for a in data['arrows']:

        ax = a['anchor']['a']['x']
        ax += a['source_manual_x']
        ay = a['anchor']['a']['y']
        ay += a['source_manual_y']
        bx = a['anchor']['b']['x']
        bx += a['target_manual_x']
        by = a['anchor']['b']['y']
        by += a['target_manual_y']

        if a['type'] == 'multi_v':
            ay, by = ay+10, by-10
            new_end = (ax, int((ay+by)/2))
            new_start = (bx, int((ay+by)/2))
            cv2.line(canvas, new_start, new_end, (0,0,0), 1)
            cv2.line(canvas, new_end, (ax,ay), (0,0,0), 1)
            cv2.line(canvas, new_start, (bx,by), (0,0,0), 1)
            cv2.arrowedLine(canvas, (ax,ay+45), (ax,ay), (0,0,0), 1)
            cv2.arrowedLine(canvas, (bx,by-45), (bx,by), (0,0,0), 1)

        elif a['type'] == 'multi_h':
            ax, bx = ax+10, bx-10
            new_end = (int((ax+bx)/2), ay)
            new_start = (int((ax+bx)/2), by)
            cv2.line(canvas, new_start, new_end, (0,0,0), 1)
            cv2.line(canvas, new_end, (ax,ay), (0,0,0), 1)
            cv2.line(canvas, new_start, (bx,by), (0,0,0), 1)
            cv2.arrowedLine(canvas, (ax+45,ay), (ax,ay), (0,0,0), 1)
            cv2.arrowedLine(canvas, (bx-45,by), (bx,by), (0,0,0), 1)

    cv2.imwrite(test_path, canvas)

    image_data = Image.open(test_path)
    draw = ImageDraw.Draw(image_data)
    for x in data['boxes']:
        font_object = font(x['weight'], x['size'])
        for a in x['text_array']:
            draw.text((a['x1'],a['y1']), a['text'], font=font_object, fill="#000000")

    image_data.save(test_path)

if __name__ == "__main__":
    render()
