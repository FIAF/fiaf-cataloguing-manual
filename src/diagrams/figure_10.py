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



    # steps to take:
        # precompute boxes
        # render boxes and arrows via opencv
        # render text using pillow


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




    with open(pathlib.Path.cwd() / 'figure_10.json') as data:
        data = json.load(data)


    for i, box in enumerate(data['boxes']):

        data['boxes'][i] = calc_position(box)



    print('@@@', json.dumps(data, indent=4))



    # OLD CODE BELOW





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
            #draw.text((x_step, y_step+(i*interval)), x, font=font_object, fill="#000000")
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
        #draw.rectangle(full_box, outline='#000000', width=1)

        return full_box




    # small diagram, 1000 x 1000

    # reuse the text box setup, but with arrows (open cv!) This means you probably need to precompute Draw object prior
    # don't use JSON, use a data object.

    def anchor(box, axis, padding):
        #print(box)
        if axis == 'b':
            axis_x, axis_y = (box[2]+box[0])/2, box[3]
        elif axis == 't':
            axis_x, axis_y = (box[2]+box[0])/2, box[1]
        elif axis == 'l':
            axis_x, axis_y = box[0]-padding, (box[1]+box[3])/2
        elif axis == 'r':
            axis_x, axis_y = box[2]+padding, (box[1]+box[3])/2
        else:
            raise Exception(f'{axis} not understood.')

        # draw.rectangle((axis_x, axis_y,axis_x+10, axis_y+10), outline='#FF0000', width=1, fill='#FF0000')

        return (int(axis_x), int(axis_y))


    data = {"boxes":
          [ {
                "text": "Sabrina\n(1954) (Work)",
                "weight": "Light",
                "size": 15,
                "x_step": 25,
                "y_step": 25,
                "interval": 15,
                "padding": 10
            },

            {
                "text": "The Audrey Hepburn Collection\n(2008) (Work)",
                "weight": "Light",
                "size": 15,
                "x_step": 250,
                "y_step": 25,
                "interval": 15,
                "padding": 10
            },
         {
                "text": "Funny Face\n(1956) (Work)",
                "weight": "Light",
                "size": 15,
                "x_step": 600,
                "y_step": 25,
                "interval": 15,
                "padding": 10
            }

    ,
         {
                "text": "Breakfast at\nTiffanys\n(1961) (Work)",
                "weight": "Light",
                "size": 15,
                "x_step": 25,
                "y_step": 100,
                "interval": 15,
                "padding": 10
            }
    ,
         {
                "text": "The Audrey Hepburn Collection\n(DVD Manifestation, 2008) (Collection Aggregate)",
                "weight": "Light",
                "size": 15,
                "x_step": 300,
                "y_step": 300,
                "interval": 15,
                "padding": 10
            }
    ,
         {
                "text": "The Audrey Hepburn Collection\n(DVD Item)",
                "weight": "Light",
                "size": 15,
                "x_step": 300,
                "y_step": 500,
                "interval": 15,
                "padding": 10
            }



          ],


        "arrows": [
            {
                "type": "multi",
                "source_box": 0,
                "source_axis": "r",
                "target_box": 1,
                "target_axis": "l"
            },
                {
                "type": "multi",
                "source_box": 1,
                "source_axis": "r",
                "target_box": 2,
                "target_axis": "l"
            },
                {
                "type": "multi",
                "source_box": 3,
                "source_axis": "r",
                "target_box": 1,
                "target_axis": "l"
            },
                {
                "type": "multi",
                "source_box": 1,
                "source_axis": "b",
                "target_box": 4,
                "target_axis": "t"
            },
                {
                "type": "multi",
                "source_box": 4,
                "source_axis": "b",
                "target_box": 5,
                "target_axis": "t"
            }









            ]


          }

    # okay you need to precompute bounding box, so you can calculate arrows at open cv stage.

    box_data = list()
    for x in data['boxes']:
        bounding = text_box(text=x['text'], weight=x['weight'], size=x['size'], x_step=x['x_step'], y_step=x['y_step'], interval=x['interval'], padding=x['padding'])
        box_data.append(bounding)

    def calc_text(b):

        text = b['text']
        x_step = b['x_step']
        y_step = b['y_step']
        interval = b['interval']
        padding = b['padding']

    # def calc_text(text, weight, size, x_step, y_step, interval, padding):
        text = text.split('\n')
        # print(text)
    #     # text =x [t]
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

        font_object = font(b['weight'], b['size'])
        text_array = list()
        for i,x in enumerate(text):
            detect = font_object.getbbox(x)
            # draw.text((x_step, y_step+(i*interval)), x, font=font_object, fill="#000000")
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

    #     # draw.rectangle(full_box, outline='#000000', width=1)

        return b

    for i, box in enumerate(data['boxes']):

        data['boxes'][i] = calc_text(box)


    img_path = pathlib.Path.cwd() / 'figure_10.png'
    canvas_w, canvas_h = 1000, 1000
    canvas = numpy.zeros((canvas_h, canvas_w, 3), numpy.uint8)
    canvas[:, :] = (255, 255, 255)


    # TODO INCLUDE THIS FUNCTION!

    # def arrow(t, start, end):
    #     if t == "elbow":
    #         draw.line([start, (start[0], end[1])], fill="#000000", width=1)
    #         draw.line([(start[0],end[1]), end], fill="#000000", width=1)
    #     elif t == 'multi':
    #         new_end = (start[0], (start[1]+end[1])/2)
    #         new_start = (end[0], (start[1]+end[1])/2)
    #         draw.line([start, new_end], fill="#000000", width=1)
    #         draw.line([new_start, end], fill="#000000", width=1)
    #         draw.line([new_start, new_end], fill="#000000", width=1)
    #     else:
    #         raise Exception("type not understood.")


    for x in data['arrows']:

        #print(x['source_axis'])

        a = (anchor(box_data[x['source_box']], x['source_axis'], 10))

        b = (anchor(box_data[x['target_box']], x['target_axis'], 10))
        #print(a) # this should be box 0, r, axis x and axis y

        cv2.arrowedLine(canvas, a,b,(0,0,0), 1)
        cv2.arrowedLine(canvas, b,a,(0,0,0), 1)
        # cv2.rectangle(canvas,(384,0),(510,128),(0,255,0),3)
        # cv2.rectangle(canvas,(255,55),(255+10,55+10),(255,0,0),3)


        # cv.line(img,(0,0),(511,511),(255,0,0),5)
        # arrow(
        #     x['type'],
        #     anchor(box_data[x['source_box']], x['source_axis']),
        #     anchor(box_data[x['target_box']], x['target_axis'])
        # )
    # add arrows here.


    # cv2.line(canvas, (25+25,(145+310)-25), (25+25, 815+25), (0,0,255), 4)
    # cv2.arrowedLine(canvas, (25+25,(480+310)-25), (25+25, 815+25), (0,0,255), 4)
    # cv2.arrowedLine(canvas, (25+25,(815+310)-25), (25+25, 1150+25), (0,0,255), 4)
    # cv2.arrowedLine(canvas, (310,(145+310)-25), (310, 480+25), (255,0,0), 4)
    # cv2.arrowedLine(canvas, (310,(480+310)-25), (310, 815+25), (255,0,0), 4)






    cv2.imwrite(img_path, canvas)

    image_data = Image.open(img_path)
    draw = ImageDraw.Draw(image_data)


    for x in data['boxes']:
        # for b in x['boxes']:
        # print(x)

        font_object = font(x['weight'], x['size'])

        for a in x['text_array']:
            # print(a)
            draw.text((a['x1'],a['y1']), a['text'], font=font_object, fill="#000000")
        draw.rectangle(x['bbox'], outline='#000000', width=1)


    # print(json.dumps(data, indent=4))

    image_data.save(img_path)



if __name__ == "__main__":
    render()
