# In-16
sdoc = params["input"]
tdoc = params["output"]

x_offset = 0
y_offset = 0
#try:
    #x_offset = params["xo"]
    #y_offset = params["yo"]
#except Exception:
    #pass

t0 = [
    [8,25,32,1],
    [-9,-24,-17,-16],
    [12,21,20,13],
    [-5,-28,-29,-4]
    ]

t1 = [
    [2,31,26,7],
    [-15,-18,-23,-10],
    [14,19,22,11],
    [-3,-30,-27,-6]
    ]

sinfo = pdf_info.extract(sdoc)
bbox = sinfo["page_size"][0][1]
pcount = sinfo["page_count"]
swidth = bbox["width"]
sheight = bbox["height"]

twidth = 8 * swidth
theight = 4 * sheight

imposition_plan = []
recto_pages = []
verso_pages = []

### recto ################################
for py in [0,1,2,3]:
    for px in [0,1,2,3]:
        rotate = False
        source_page = t0[py][px] * 1
        if source_page < 0:
            rotate = True
            source_page *= -1
        x = (px * swidth) + x_offset
        y = (py * sheight) + y_offset
        r = 0
        if rotate:
            r = 180
            x += swidth
            y += sheight
        recto_pages.append({
                "source_document" : sdoc,
                "source_page" : source_page - 1,
                "crop_box" : {"left":0,"bottom":0,"width":swidth, "height":sheight},
                "translate" : [x,y],
                "rotate" : r,
                "scale" : [1,1]
                })
                
for py in [0,1,2,3]:
    for px in [0,1,2,3]:
        rotate = False
        source_page = t0[py][px] * 1
        if source_page < 0:
            rotate = True
            source_page *= -1
        x = (px * swidth) + x_offset + (4 * swidth)
        y = (py * sheight) + y_offset
        r = 0
        if rotate:
            r = 180
            x += swidth
            y += sheight
        recto_pages.append({
                "source_document" : sdoc,
                "source_page" : source_page - 1 + 32,
                "crop_box" : {"left":0,"bottom":0,"width":swidth, "height":sheight},
                "translate" : [x,y],
                "rotate" : r,
                "scale" : [1,1]
                })

imposition_plan.append({
            "target_document" : tdoc,
            "target_page_width" : twidth,
            "target_page_height" : theight,
            "pages": recto_pages})
                
### end of recto ################################

### verso ################################
for py in [0,1,2,3]:
    for px in [0,1,2,3]:
        rotate = False
        source_page = t1[py][px] * 1
        if source_page < 0:
            rotate = True
            source_page *= -1
        x = (px * swidth) + x_offset + (4 * swidth)
        y = (py * sheight) + y_offset
        r = 0
        if rotate:
            r = 180
            x += swidth
            y += sheight
        verso_pages.append({
                "source_document" : sdoc,
                "source_page" : source_page - 1,
                "crop_box" : {"left":0,"bottom":0,"width":swidth, "height":sheight},
                "translate" : [x,y],
                "rotate" : r,
                "scale" : [1,1]
                })
                
for py in [0,1,2,3]:
    for px in [0,1,2,3]:
        rotate = False
        source_page = t1[py][px] * 1
        if source_page < 0:
            rotate = True
            source_page *= -1
        x = (px * swidth) + x_offset 
        y = (py * sheight) + y_offset
        r = 0
        if rotate:
            r = 180
            x += swidth
            y += sheight
        verso_pages.append({
                "source_document" : sdoc,
                "source_page" : source_page - 1 + 32,
                "crop_box" : {"left":0,"bottom":0,"width":swidth, "height":sheight},
                "translate" : [x,y],
                "rotate" : r,
                "scale" : [1,1]
                })

imposition_plan.append({
            "target_document" : tdoc,
            "target_page_width" : twidth,
            "target_page_height" : theight,
            "pages": verso_pages})
                
### end of verso ################################

