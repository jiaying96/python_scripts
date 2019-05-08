import cv2
import sys
import os
import numpy as np
import pyautogui
import math
import ctypes
from ctypes import wintypes, windll

path = sys.argv[1]
wndName = "ESC close, x next, z previous, c clean, w up, s down, a left, d right"
warpwndname = 'warped plate'
imgs = os.listdir(path)
total = len(imgs)
i = 0
box = []
pts = []
labels = []
n = 0
breakfile = 'lbreakpoint.txt'
cursor = wintypes.POINT()

lastx = 0
lasty = 0

alpha = 0
beta = 0

print("%d images loaded" % total)


if os.path.exists(breakfile):
    with open(breakfile, "r") as p:
        i = int(p.read())
        print('load breakpointL %d' % i)


def apply_brightness_contrast(input_img, brightness=0, contrast=0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf


def order_points(pot):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pot.sum(axis=1)
    rect[0] = pot[np.argmin(s)]
    rect[2] = pot[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pot[np.argmin(diff)]
    rect[3] = pot[np.argmax(diff)]

    # return the ordered coordinates
    return rect


def warpImage(img, opts):
    x0 = 0
    x1 = 120
    x2 = 120
    x3 = 0
    y0 = 0
    y1 = 0
    y2 = 48
    y3 = 48
    w = img.shape[1]
    h = img.shape[0]
    px = int(math.floor(h * 0.04 * 5))
    py = int(math.floor(h * 0.04 * 2))
    src = np.float32([[opts[0][0] - box[0][0], opts[0][1] - box[0][1]], [opts[1][0] - box[0][0], opts[1][1] - box[0][1]],
           [opts[2][0] - box[0][0], opts[2][1] - box[0][1]], [opts[3][0] - box[0][0], opts[3][1] - box[0][1]]])
    dst = np.float32([[x0 + px, y0 + py], [x1 + px, y1 + py], [x2 + px, y2 + py], [x3 + px, y3 + py]])
    warp_mat = cv2.getPerspectiveTransform(src, dst)
  
    warp_dst = cv2.warpPerspective(img, warp_mat, (120 + 2 * px, 48 + 2 * py))
    cv2.normalize(warp_dst, warp_dst, 255, 0, cv2.NORM_MINMAX)
    cv2.imshow(warpwndname, warp_dst)
    return warp_dst


def draw_pts(img):
    if len(box) == 2:
        cv2.rectangle(img, box[0], box[1], (0, 255, 0), 1)
    for p in pts:
        cv2.circle(img, p, 4, (0, 0, 255), -1)


def onMouse(event, x, y, flag, points):
    global dpoint, waitSecDown, wndName, epoint, cach

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(box) < 2:
            box.append((x, y))
            if len(box) < 2:
                cv2.line(cach, (0, y), (cach.shape[1], y), (255, 0, 0), 2)
                cv2.line(cach, (x, 0), (x, cach.shape[0]), (255, 0, 0), 2)
            else:
                cach = apply_brightness_contrast(orig, alpha, beta)
                draw_pts(cach)
                cv2.rectangle(cach, box[0], box[1], (0, 255, 0), 3)
        else:
            pts.append((x, y))
            cv2.circle(cach, (x, y), 4, (0, 0, 255), -1)
        cv2.imshow(wndName, cach)

        if len(box) == 2 and len(pts) == 4:
            opts = order_points(np.array(pts, dtype="float32"))
            with open('labels.txt', 'a+') as l:
                l.write('%s:%d,%d,%d,%d,%d,%d,%d,%d,###\n' % (imgs[i], opts[0][0], opts[0][1],opts[1][0], opts[1][1],opts[2][0], opts[2][1],opts[3][0], opts[3][1]))
            global n
            sub = orig[box[0][1]:box[1][1], box[0][0]:box[1][0]]
            with open(breakfile, "w") as p:
                p.write("%d" % i)
                n += 1
            pyautogui.press('x')

    elif event == cv2.EVENT_MOUSEMOVE:
        global cach2, lastx, lasty
        lastx = x
        lasty = y
        cach2 = np.copy(cach)
        cv2.line(cach2, (0, y), (cach.shape[1], y), (0, 255, 0), 2)
        cv2.line(cach2, (x, 0), (x, cach.shape[0]), (0, 255, 0), 2)
        cv2.imshow(wndName, cach2)


end = False

while not end:
    f = open(os.path.join(path, imgs[i]), mode='rb')
    bt = f.read()
    f.close()
    nn = np.frombuffer(bt, np.uint8)
    orig = cv2.imdecode(nn, 1)
    rw = orig.shape[1]
    rh = orig.shape[0]
    rs = max(rh, rw)
    scale = 800.0 / rs
    nh = int(rh * scale)
    nw = int(rw * scale)
    cach = np.copy(orig)
    cach2 = np.copy(cach)
    cv2.imshow(wndName, cach)
    cv2.setMouseCallback(wndName, onMouse)
    while True:
        key = cv2.waitKey()
        key = key & 0xFF

        if key == 0x1B:  # ESC
            end = True
            break

        if key == ord('c'):
            pts = []
            box = []
            alpha = beta = 0
            cach = np.copy(orig)
            cv2.imshow(wndName, cach)
            continue

        if key == ord('w'):
            # pyautogui.moveRel(0, -1)
            windll.user32.GetCursorPos(ctypes.byref(cursor))
            windll.user32.SetCursorPos(cursor.x, cursor.y - 1)
            continue

        if key == ord('a'):
            # pyautogui.moveRel(-1, 0)
            windll.user32.GetCursorPos(ctypes.byref(cursor))
            windll.user32.SetCursorPos(cursor.x - 1, cursor.y)
            continue

        if key == ord('s'):
            # pyautogui.moveRel(0, 1)
            windll.user32.GetCursorPos(ctypes.byref(cursor))
            windll.user32.SetCursorPos(cursor.x, cursor.y + 1)
            continue

        if key == ord('d'):
            # pyautogui.moveRel(1, 0)
            windll.user32.GetCursorPos(ctypes.byref(cursor))
            windll.user32.SetCursorPos(cursor.x + 1, cursor.y)
            continue

        if key == ord('z'):
            pts = []
            box = []
            alpha = beta = 0
            i -= 1
            if i < 0:
                i = 0
            break

        if key == ord('x'):
            pts = []
            box = []
            alpha = beta = 0
            i += 1
            print('%d/%d' % (i, total))
            if i == total:
                i = total - 1
            break

        if key == ord('f'):
            alpha += 32
            if alpha >= 127:
                alpha = 127
            tmp = apply_brightness_contrast(orig, alpha, beta)
            draw_pts(tmp)
            cach = tmp
            cv2.imshow(wndName, cach)

        if key == ord('g'):
            alpha -= 32
            if alpha <= -127:
                alpha = -127
            tmp = apply_brightness_contrast(orig, alpha, beta)
            draw_pts(tmp)
            cach = tmp
            cv2.imshow(wndName, cach)

        if key == ord('r'):
            beta += 32
            if beta >= 127:
                beta = 127
            tmp = apply_brightness_contrast(orig, alpha, beta)
            draw_pts(tmp)
            cach = tmp
            cv2.imshow(wndName, cach)

        if key == ord('t'):
            beta -= 32
            if beta <= -127:
                beta = -127
            tmp = apply_brightness_contrast(orig, alpha, beta)
            draw_pts(tmp)
            cach = tmp
            cv2.imshow(wndName, cach)
