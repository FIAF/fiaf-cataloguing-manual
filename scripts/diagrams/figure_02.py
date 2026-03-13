import cv2
import matplotlib.pylab as plt
import numpy
import pathlib
import skimage
from PIL import Image, ImageDraw, ImageFont

def draw():

    def font(weight, size):
        ''' Define a font object. '''

        font_path = pathlib.Path.cwd().parents[0] / 'font' / f'BrownStd{weight}.otf'
        if not font_path.exists():
            raise Exception('Font OTF does not exist.')

        return ImageFont.truetype(str(font_path), size)

    def draw_rectangle(name, x, y, w, h, colour):

        ''' Define a rectangle shape. '''

        cv2.rectangle(canvas, (x, y), (x+w, y+h), (0,0,0), 2)
        cv2.rectangle(canvas, (x, y), (x+w, y+h), colour, -1)
        elements[name] = {'x':x, 'y':y, 'w':w, 'h':h}

    def draw_text_by_anchor(anchor, text, text_weight, text_size, center, y_offset_iterate, x_offset_manual, colour, opacity, manual_y):

        font_object = font(text_weight, text_size)
        anchor_coords = elements[anchor]
        center_x = anchor_coords['x']+(anchor_coords['w']/2)
        center_y = anchor_coords['y']+(anchor_coords['h']/2)

        text_bbox = font_object.getbbox(text[:4])
        center_y = center_y-(text_bbox[3]/2)

        center_y = center_y + (y_offset_iterate*20)

        center_x = center_x+x_offset_manual

        if center:
            text_bbox = font_object.getbbox(text)
            center_x = center_x-(text_bbox[2]/2)

        center_y = center_y+manual_y

        detect = font_object.getbbox(text)

        x1 = int(center_x) + detect[0]
        y1 = int(center_y) + detect[1]
        x2 = int(center_x) + detect[2]
        y2 = int(center_y) + detect[3]

        bbox = (x1,y1,x2,y2)
        # draw.rectangle(bbox, outline='#ff0000')

        if opacity:
            draw.text((int(center_x), int(center_y)), text, font=font_object, fill=colour)

        return bbox

    img_path = pathlib.Path.cwd() / 'figure_02.png'

    canvas_w, canvas_h = 1000, 1500
    canvas = numpy.zeros((canvas_h, canvas_w, 3), numpy.uint8)
    canvas[:, :] = (255, 255, 255)

    elements = dict()
    draw_rectangle('header', 25, 25, 950, 95, ((250/2)+(255/2),(206/2)+(255/2),(135/2)+(255/2)))

    box_colour = (250, 206, 135)

    draw_rectangle('layer_1', 125, 155+50, 850, 285, box_colour)
    draw_rectangle('layer_3', 125, 490+(50*2), 850, 285, box_colour)
    draw_rectangle('layer_4', 125, 825+(50*3), 850, 285, box_colour)

    draw_rectangle('box_1', 25, 145+50, 310, 310, box_colour)
    draw_rectangle('box_3', 25, 480+50+50, 310, 310, box_colour)
    draw_rectangle('box_4', 25, 815+50+50+50, 310, 310, box_colour)

    instep = 25+int(310/2)
    cv2.arrowedLine(canvas, (instep,(145+50+310)-25), (instep, 480+50+50+25), (0,0,255), 4)
    cv2.arrowedLine(canvas, (instep,(480+50+50+310)-25), (instep, 815+50+50+50+25), (0,0,255), 4)

    cv2.imwrite(img_path, canvas)

    image_data = Image.open(img_path)
    draw = ImageDraw.Draw(image_data)

    draw_text_by_anchor('header', 'Full hierarchy model: 3 levels', 'Regular', 40, True, 0, 0, "#000000", 1, 0)

    layer_1_text = [
        '• Type - Whole conditions (serial / standalone / component part)',
        '• Titles (original, alternative, series/serial)',
        '• Dates (copyright / production)',
        '• Language(s): original language of conception/presentation',
        '• Content: Synopsis, Genre, Form, Subject',
        '• Agents: Cast, Credits, Rights holders',
        '• Identifier (international, in-house unique identifier number)'
        ]

    layer_1_text = [{'text':x, 'offset':i-((len(layer_1_text)-1)/2)} for i,x in enumerate(layer_1_text)]
    for x in layer_1_text:
        draw_text_by_anchor('layer_1', x['text'], 'Regular', 14, False, x['offset'], -180, "#444444", 1, 0)

    layer_3_text = [
        '• Identifier (international, in-house unique identifier number)',
        '• Titles',
        '• Type: pre-release, theatrical, non-theatrical, transmission, home-viewing, inter-',
        'net, restoration, not-for-release, etc',
        '• Language: dialogue language, subtitles, dubbed, intertitles, etc.',
        '• Format: 35mm film, Digital Cinema Package (DCP) , Blu-ray, etc',
        '• Extent: physical, logical, temporal, e.g. duration, running time, length, etc.',
        '• Event: release, transmission, distribution, creation, dates',
        '• Rights context: platforms, territories, dates',
        '• Agents: Creator, Broadcaster, Distributor, Publisher'
    ]

    layer_3_text = [{'text':x, 'offset':i-((len(layer_3_text)-1)/2)} for i,x in enumerate(layer_3_text)]
    for x in layer_3_text:
        draw_text_by_anchor('layer_3', x['text'], 'Regular', 14, False, x['offset'], -180, "#444444", 1, 0)

    layer_4_text = [
        '• Identifier (inventory numbers)',
        '• Titles ((original, alternative)',
        '• Element Type : instantiation type, e.g. original negative, dupe positive, Lavender,',
        'sound negative',
        '• Item specifics: carrier, base, gauge, format, digital file type, sound, sound sys-',
        'tems, colour standards etc.',
        '• Extent: physical, temporal, e.g. footage, file size, duration',
        '• Access conditions: Condition report - pristine, not for projection, heavy scratch-',
        'es, etc; storage location - home location, current location; Conservation recom-',
        'mendations: urgent transfer required, relocate to sub-zero, etc',
        '• Event(s) (with Dates): creation, acquisition, accession, de-accession, loan, transport',
        '• Acquisition: source, method, funding context, conditions of access, dates',
        '• Agents: donors, archive technicians/conservationists, etc.',
        '• Holding institution: name of the Item holder'
    ]

    layer_4_text = [{'text':x, 'offset':i-((len(layer_4_text)-1)/2)} for i,x in enumerate(layer_4_text)]
    for x in layer_4_text:
        draw_text_by_anchor('layer_4', x['text'], 'Regular', 14, False, x['offset'], -180, "#444444", 1, 0)

    draw_text_by_anchor('box_1', 'Work', 'Bold', 40, True, 0, 0, "#444444", 1, 0)
    draw_text_by_anchor('box_1', 'abstract entity', 'Regular', 20, True, 2, 0, "#444444", 1, 0)

    draw_text_by_anchor('box_3', 'Manifestation', 'Bold', 40, True, 0, 0, "#444444", 1, 0)
    draw_text_by_anchor('box_3', 'realisation, release,', 'Regular', 20, True, 2, 0, "#444444", 1, 0)
    draw_text_by_anchor('box_3', 'exhibition or', 'Regular', 20, True, 3, 0, "#444444", 1, 0)
    draw_text_by_anchor('box_3', 'distribution entity', 'Regular', 20, True, 4, 0, "#444444", 1, 0)

    draw_text_by_anchor('box_4', 'Item', 'Bold', 40, True, 0, 0, "#444444", 1, 0)
    draw_text_by_anchor('box_4', 'physical or digital', 'Regular', 20, True, 2, 0, "#444444", 1, 0)
    draw_text_by_anchor('box_4', 'object', 'Regular', 20, True, 3, 0, "#444444", 1, 0)

    image_data.save(img_path)

if __name__ == "__main__":
    draw()
