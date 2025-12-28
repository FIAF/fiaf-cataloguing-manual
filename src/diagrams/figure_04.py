import cv2
import matplotlib.pylab as plt
import numpy
import pandas
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

    img_path = pathlib.Path.cwd() / 'figure_04.png'


    canvas_w, canvas_h = 1000, 1500
    canvas = numpy.zeros((canvas_h, canvas_w, 3), numpy.uint8)
    canvas[:, :] = (255, 255, 255)

    elements = dict()
    draw_rectangle('header', 25, 25, 950, 95, ((255/2)+(255/2),(168/2)+(255/2),(216/2)+(255/2)))

    box_colour = (255, 168, 216)
    draw_rectangle('layer_1', 125, 155+50, 850, 285*2, box_colour)
    draw_rectangle('box_1', 25, 145+50, 310, 310*2, box_colour)
    cv2.imwrite(img_path, canvas)

    image_data = Image.open(img_path)
    draw = ImageDraw.Draw(image_data)

    draw_text_by_anchor('header', 'No hierarchy model: 1 level', 'Regular', 40, True, 0, 0, "#000000", 1, 0)

    layer_1_text = [
        '• Identifier (international, in-house unique identifier number)',
        '• Type - Whole conditions (serial / standalone / component part)',
        '• Titles (original, alternative, series/serial)',
        '• Dates: copyright, production, release, object creation, object acquisition',
        '/ accession, de-accession, loan, transport',
        '• Content: Synopsis, Genre, Form, Subject',
        '• Agents: Cast, Credits, Rights holders',
        '• Type: pre-release, theatrical, non-theatrical, transmission, home-viewing,',
        'internet, restoration, not-for-release,',
        '• Language(s): original language, language of dialogue, subtitles, dubbing,',
        'intertitles, etc.',
        '• Instantiation type: e.g. original negative, dupe positive, Lavender,',
        'sound negative',
        '• Format/Item Specificss: 35mm film, Digital Cinema Package (DCP), Blu-ray, etc;',
        'carrier, base, gauge, format, digital file type, sound, sound systems,',
        'colour standards, etc.',
        '• Extent: physical, logical, temporal, e.g. duration, running time, footage, file size',
        '• Event(s): release, transmission, distribution, creation, acquisition, accession,',
        'de-accession, loan, transport, dates',
        '• Rights context: platforms, territories, dates, transfer of ownership',
        '• Agents: Creator, Broadcaster, Distributor, Publisher, Donor, Institution',
        'technicians/conservationists, etc.',
        '• Access conditions: Condition report - pristine, not for projection,',
        'heavy scratches, etc; storage location - home location, current location; Con-',
        'servation recommendations: urgent transfer required, relocate to sub-zero, etc',
        '• Acquisition: source, method, funding context, conditions of access, dates',
        '• Holding institution: name of the Item holder',
        ]

    layer_1_text = [{'text':x, 'offset':i-((len(layer_1_text)-1)/2)} for i,x in enumerate(layer_1_text)]
    for x in layer_1_text:
        draw_text_by_anchor('layer_1', x['text'], 'Regular', 14, False, x['offset'], -180, "#444444", 1, 0)

    # TODO
    # the by_anchor method worked great when font was predictable
    # but the need to have text of different fontsize co-existing means pre-compute, so now you are supporting both methods.
    # instead, switch everything to pre-compute and dynamic centering, and make background rects match that.


    bbox_array = list()
    bbox_array.append(draw_text_by_anchor('box_1', 'Work', 'Bold', 40, True, 0, 0, (68,68,68, 0), 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'Manifestation', 'Bold', 40, True, 2, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'Item', 'Bold', 40, True, 4, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'properties', 'Regular', 20, True, 6, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'expressed', 'Regular', 20, True, 7, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'in one record,', 'Regular', 20, True, 8, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'with abstract,', 'Regular', 20, True, 9, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'contextual', 'Regular', 20, True, 10, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'and object data', 'Regular', 20, True, 11, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'stored on a', 'Regular', 20, True, 12, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'single hierarchy', 'Regular', 20, True, 13, 0, "#444444", 0, 0))
    bbox_array.append(draw_text_by_anchor('box_1', 'level', 'Regular', 20, True, 14, 0, "#444444", 0, 0))

    df = pandas.DataFrame(bbox_array, columns=['x1', 'y1', 'x2', 'y2'])
    test_mid = ((min(df.y1)+max(df.y1))/2)
    box_mid =  ((145+50+310*2)/2)
    y_adjust = (box_mid - test_mid)/2

    draw_text_by_anchor('box_1', 'Work', 'Bold', 40, True, 0, 0, (68,68,68, 0), 1, y_adjust)
    draw_text_by_anchor('box_1', 'Manifestation', 'Bold', 40, True, 2, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'Item', 'Bold', 40, True, 4, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'properties', 'Regular', 20, True, 6, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'expressed', 'Regular', 20, True, 7, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'in one record,', 'Regular', 20, True, 8, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'with abstract,', 'Regular', 20, True, 9, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'contextual', 'Regular', 20, True, 10, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'and object data', 'Regular', 20, True, 11, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'stored on a', 'Regular', 20, True, 12, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'single hierarchy', 'Regular', 20, True, 13, 0, "#444444", 1, y_adjust)
    draw_text_by_anchor('box_1', 'level', 'Regular', 20, True, 14, 0, "#444444", 1, y_adjust)

    image_data.save(img_path)



if __name__ == "__main__":
    draw()
